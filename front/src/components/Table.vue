<template>
  <card-base :bgColor="bgColorCard">
    <div class="row">
      <div class="col-12 text-h6 text-white">
        {{ title }}
      </div>
      <div class="col-12">
        <q-separator dark></q-separator>
      </div>
      <div class="col-12 no-padding">
        <q-table
          dense
          :style="'background: '+bgColorCard+' !important'"
          :data="data"
          :columns="columns"
          row-key="name"
          class="no-shadow"
          separator="cell"
        >
          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td key="index" :props="props">
                <q-badge color="green" class="text-black">
                  {{ props.row.index }}
                </q-badge>
              </q-td>
              <q-td key="date" :props="props">
                <q-badge color="purple">
                  {{ format(props.row.date) }}
                </q-badge>
              </q-td>
              <q-td key="valor" :props="props">
                <q-badge color="orange" class="text-black">
                  {{ props.row.valor }}
                </q-badge>
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
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
    bgColorCard: {
      type: String
    },
    title: {
      type: String,
      required: true
    },
    predict: {
      type: Boolean,
      required: true
    }
  },
  data () {
    return {
      form: {
        date: date.formatDate(new Date(), 'YYYY-MM-DD')
      },
      columns: [
        { name: 'index', align: 'center', label: 'Id', field: 'index', sortable: true },
        { name: 'date', align: 'center', label: 'Data', field: 'date', sortable: true },
        { name: 'valor', align: 'center', label: 'Casos', field: 'valor', sortable: true }
      ],

      data: []
    }
  },
  mounted () {
    this.getValue()
  },
  methods: {
    getValue () {
      this.$axios.get(`predict?date=${this.form.date}`)
        .then((res) => {
          if (this.predict) this.data = res.data.predict
          else this.data = res.data.trueValue
        })
    },
    format (dat) {
      return date.formatDate(dat, 'DD/MM/YYYY')
    }
  }
}
</script>
