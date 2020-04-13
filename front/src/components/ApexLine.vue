<template>
  <card-base>
    <apexchart ref="realtimeChart" type="line" height="200" :options="chartOptions" :series="series" />
  </card-base>
</template>

<script>
import CardBase from 'components/CardBase'
import { date } from 'quasar'
export default {
  name: 'ApexLine',
  components: {
    CardBase
  },
  props: {
    title: {
      type: String,
      required: true
    },
    predict: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      form: {
        date: date.formatDate(new Date(), 'YYYY-MM-DD')
      },
      series: [{
        name: 'Desktops',
        data: []
      }],
      chartOptions: {
        colors: ['#FCCF31', '#17ead9', '#f02fc2'],
        chart: {
          height: 350,
          type: 'line'
        },
        grid: {
          show: true,
          strokeDashArray: 0,
          xaxis: {
            lines: {
              show: true
            }
          }
        },
        stroke: {
          curve: 'smooth'
        },
        dropShadow: {
          enabled: true,
          opacity: 0.3,
          blur: 5,
          left: -7,
          top: 22
        },
        dataLabels: {
          enabled: false
        },
        title: {
          text: this.title,
          align: 'left',
          style: {
            color: '#FFF'
          }
        },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
          labels: {
            style: {
              colors: '#fff'
            }
          }
        },
        yaxis: {
          labels: {
            style: {
              color: '#fff'
            }
          }
        }
      }
    }
  },
  async mounted () {
    // this.setDataLineChart()
    if (this.predict) this.getValuePredict()
    else this.getValue()
  },
  methods: {
    getValuePredict () {
      this.$axios.get(`predict?date=${this.form.date}`)
        .then((res) => {
          this.series[0].data.splice(0, 1)
          this.series[0].data = res.data.predict.filter((f) => f.valor !== '0').map((m) => {
            return { x: date.formatDate(m.date, 'DD/MM/YYYY'), y: m.valor }
          })
          this.updateSeriesLine()
        })
    },
    getValue () {
      this.$axios.get(`predict?date=${this.form.date}`)
        .then((res) => {
          console.log(this.chartOptions.xaxis.categories)
          this.series[0].data.splice(0, 1)
          this.series[0].data = res.data.trueValue.filter((f) => f.valor !== '0').map((m) => {
            return {
              x: date.formatDate(m.date, 'DD/MM/YYYY'),
              y: m.valor
            }
          })
          this.updateSeriesLine()
        })
    },
    getRandomArbitrary (min, max) {
      return Math.floor(Math.random() * 99)
    },
    // setDataLineChart () {
    //   setInterval(() => {
    //     this.series[0].data.splice(0, 1)
    //     this.series[0].data.push(this.getRandomArbitrary(0, 99))
    //     this.updateSeriesLine()
    //   }, 3000)
    // },
    updateSeriesLine () {
      this.$refs.realtimeChart.updateSeries([{
        data: this.series[0].data
      }], false, true)
    }
  }
}
</script>
