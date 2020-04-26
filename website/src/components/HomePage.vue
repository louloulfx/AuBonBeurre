<template>
  <div class="container">
    <router-link class="boxContainer" v-for="(numeroUnite, i) in numerosUnite" :key="i + 1" v-bind:to="'/stats/' + numeroUnite">
      <div class="box">
        <p>Unité n°{{numeroUnite}}</p>
      </div>
    </router-link >
  </div>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      numerosUnite: [1, 2, 3, 4, 5, 6]
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
    text-decoration: none;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
  min-height: 95vh;
}
.boxContainer {
  width: 32%;
  margin-bottom: 2%;
  text-align: center;
}
.box {
  display: inline-block;
  padding: 100px;
  border: 1px solid black;
}
</style>
