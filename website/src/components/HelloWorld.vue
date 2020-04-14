<template>
  <div class="container">
    <div class="boxContainer" v-for="(numeroUnite, i) in numerosUnite" :key="i + 1">
      <div class="box">
      <p>Unité n°{{numeroUnite}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      numerosUnite: [1,2,3,4,5,6]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.boxContainer{
  width: 32%;
  margin-bottom: 2%;
  text-align: center;
}
.box {
  display: inline-block;
  width: 250px;
  height: 250px;
  border: 1px solid black;
}
</style>
