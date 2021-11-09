<template>
  <div id="app">
    <h1>App</h1>
    <input type="text">
    <p>appdata: </p>
    <p>parentData: </p>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;

  /* 테두리 설정 */
  border :1px solid black;
}
</style>
