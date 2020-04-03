<template>
  <div id="app">
    <Navbar/>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Users/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'
import Users from './components/Users.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Navbar,
    Users
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
