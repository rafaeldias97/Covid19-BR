<template>
  <b-card 
    border-variant="primary"
    align="center" 
    title="Prever por Data">
    <b-form inline>
      <b-form-datepicker id="example-datepicker" v-model="value" v-bind="labels['pt'] || {}" class="mb-2" locale="pt"></b-form-datepicker>
      <b-btn variant="warning" class="mb-2 ml-2" @click="predict(value)">Pesquisar</b-btn>
    </b-form>
    <apexchart
      ref="chart"
      v-if="series[0].data.length !== 0"
      type="line"
      height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </b-card>
</template>

<script>
import axios from "axios";
import VueApexCharts from "vue-apexcharts";
import moment from "moment";
export default {
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      value: '',
      labels: {
        pt: {
          labelNoDateSelected: 'Selecione uma data'
        }
      },
      series: [
        {
          name: "Likes",
          data: []
        }
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: "line"
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        xaxis: {
          type: "datetime",
          categories: []
        },
        title: {
          text: "Covid-19 Brasil",
          align: "left",
          style: {
            fontSize: "20px",
            color: "#2c3e50"
          }
        },
        fill: {
          type: "gradient",
          gradient: {
            shade: "dark",
            gradientToColors: ["#2c3e50"],
            shadeIntensity: 1,
            type: "horizontal",
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100, 100, 100]
          }
        },
        markers: {
          size: 4,
          colors: ["#002776"],
          strokeColors: "#fff",
          strokeWidth: 2,
          hover: {
            size: 7
          }
        },
        yaxis: {
          min: 0,
          max: 0,
          title: {
            text: "Casos"
          }
        }
      }
    };
  },
  // async mounted() {
  //   await this.predict('2020-04-20');
  // },
  methods: {
    async predict(date) {
      let { data } = await axios.get(
        `http://127.0.0.1:5000/api/predict?date=${date}`
      );
      this.chartOptions.yaxis.max = this.findMaxValue(data.predict);
      this.chartOptions.xaxis.categories = data.predict.map(m =>
        this.formatDate(m.date)
      );
      this.series[0].data = data.predict.map(m => parseInt(m.valor));
    },
    findMaxValue(array) {
      return Math.max.apply(
        Math,
        array.map(o => o.valor)
      );
    },
    formatDate(date) {
      return moment(date).format("MM/DD/YYYY");
    }
  }
};
</script>

<style lang="scss" scoped>
</style>