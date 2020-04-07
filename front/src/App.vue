<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" style="background-color: #fff;   box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);" fixed="top" sticky>
      <b-navbar-brand class="mx-auto" center href="#">
        <h2><b style="color: blue">Brasil</b><b style="color: yellow"> || </b><b style="color: green">Covid-19</b></h2>
      </b-navbar-brand>
    </b-navbar>
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
