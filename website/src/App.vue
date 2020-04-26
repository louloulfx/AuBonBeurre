<template>
  <div>
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from "./components/Navbar";

export default {
  name: "App",
  components: {
    navbar
  }
};
</script>

<style>
body {
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
}
</style>
