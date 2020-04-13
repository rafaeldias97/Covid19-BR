<template>
  <card-base :bgColor="bgColorCard">
    <div class="row">
      <div class="col-12 text-h6 text-white">
        {{ title }}
      </div>
      <div class="col-12">
        <q-separator dark></q-separator>
        <apexchart ref="realtimeChart" type="line" height="90" :options="chartOptions" :series="series" />
      </div>
      <div class="col-12 text-h3 text-center text-white">
        50
      </div>
    </div>
  </card-base>
</template>

<script>
import CardBase from 'components/CardBase'
export default {
  name: 'ApexLine',
  components: {
    CardBase
  },
  props: {
    bgColorCard: {
      type: String
    },
    title: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      series: [{
        data: [10, 41, 35, 51, 260, 62, 69, 91, 600]
      }],
      chartOptions: {
        colors: ['#FFF', '#17ead9', '#f02fc2'],
        chart: {
          toolbar: {
            show: false
          }
        },
        grid: {
          show: false
        },
        stroke: {
          curve: 'smooth',
          width: 4
        },
        xaxis: {
          // categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
          axisBorder: {
            show: false
          },
          labels: {
            show: false,
            style: {
              colors: '#fff'
            }
          }
        },
        yaxis: {
          labels: {
            show: false,
            style: {
              color: '#fff'
            }
          }
        }
      }
    }
  },
  mounted () {
    // this.setDataLineChart()
    this.getMEA()
  },
  methods: {
    getMEA () {
      this.$axios.get('/medias')
        .then((res) => {
          console.log(res.data)
        })
    },
    getRandomArbitrary (min, max) {
      return Math.floor(Math.random() * 99)
    },
    setDataLineChart () {
      setInterval(() => {
        this.series[0].data.splice(0, 1)
        this.series[0].data.push(this.getRandomArbitrary(0, 99))
        this.updateSeriesLine()
      }, 3000)
    },
    updateSeriesLine () {
      this.$refs.realtimeChart.updateSeries([{
        data: this.series[0].data
      }], false, true)
    }
  }
}
</script>
