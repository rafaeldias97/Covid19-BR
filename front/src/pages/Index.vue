<template>
  <q-page class="container" style="background: #343E59;">
    <div class="row q-col-gutter-md q-px-md q-pt-sm justify-center">
      <div class="col-md-3">
        <apex-line-small title="Infectados" :bgColorCard="colors[0]"></apex-line-small>
      </div>
      <div class="col-md-3">
        <apex-line-small title="Mortes" :bgColorCard="colors[1]"></apex-line-small>
      </div>
      <div class="col-md-3">
        <apex-line-small title="Taxa Letalidade" :bgColorCard="colors[2]"></apex-line-small>
      </div>
      <div class="col-md-3">
        <apex-line-small title="Taxa de Erro Treinamento" :bgColorCard="colors[3]"></apex-line-small>
      </div>
    </div>
    <div class="row q-col-gutter-md q-px-md q-py-md">
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-line title="Ocorrencias Baseadas em Regressão Linear" :predict="true"></apex-line>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-line title="Ocorrencias Reais de Corona" :predict="false"></apex-line>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <table-component title="Ocorrencias Baseadas em Regressão Linear" :predict="true" :bgColorCard="colors[4]"></table-component>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <table-component title="Ocorrencias Reais de Corona" :predict="false" :bgColorCard="colors[4]"></table-component>
      </div>
      <!-- <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-column></apex-column>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-donut></apex-donut>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-multiple-radial-bars></apex-multiple-radial-bars>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-heatmap></apex-heatmap>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-radial-bar></apex-radial-bar>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-bubble></apex-bubble>
      </div>
      <div class="col-md-6 col-sm-12 col-xs-12">
        <apex-radar></apex-radar>
      </div> -->
    </div>
  </q-page>
</template>

<script>
// import ApexColumn from 'components/ApexColumn'
// import ApexDonut from 'components/ApexDonut'
import ApexLine from 'components/ApexLine'
import TableComponent from 'components/Table'
// import ApexHeatmap from 'components/ApexHeatmap'
// import ApexMultipleRadialBars from 'components/ApexMultipleRadialBars'
// import ApexRadialBar from 'components/ApexRadialBar'
// import ApexBubble from 'components/ApexBubble'
// import ApexRadar from 'components/ApexRadar'
import ApexLineSmall from 'components/ApexLineSmall'
export default {
  name: 'PageIndex',
  components: {
    TableComponent,
    // ApexColumn,
    // ApexDonut,
    ApexLine,
    // ApexMultipleRadialBars,
    // ApexHeatmap,
    // ApexRadialBar,
    // ApexBubble,
    // ApexRadar,
    ApexLineSmall
  },
  data () {
    return {
      colors: [
        'linear-gradient( 135deg, #ABDCFF 10%, #0396FF 100%)',
        'linear-gradient( 135deg, #2AFADF 10%, #4C83FF 100%)',
        'linear-gradient( 135deg, #FFD3A5 10%, #FD6585 100%)',
        'linear-gradient( 135deg, #EE9AE5 10%, #5961F9 100%)',
        'linear-gradient( 135deg, #0396FF 10%, #FD6585 100%)'
      ]
    }
  }
}
</script>
