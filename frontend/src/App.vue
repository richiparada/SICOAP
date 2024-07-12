<template>
  <div id="app">
    <ProveedoresList />
  </div>
</template>

<script>
import ProveedoresList from './components/ProveedoresList.vue';

export default {
  name: 'App',
  components: {
    ProveedoresList
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
