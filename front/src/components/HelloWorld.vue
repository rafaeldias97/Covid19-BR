<template>
  <div class="hello">
    <b-row cols="1" cols-sm="2" cols-md="2" cols-lg="2" cols-xl="3" class="text-center ml-2 mb-5 mt-3 mr-2" style="font-size: 4rem;">
      <b-col class="mb-2">
        <chart-predict></chart-predict>
      </b-col>
      <b-col class="mb-2">
        <chart-predict></chart-predict>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import ChartPredict from '../components/ChartPredict'
export default {
  components: {
    ChartPredict
  },
  name: 'HelloWorld'
}
</script>
