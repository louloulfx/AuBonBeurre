<template>
  <div class="container">
    <router-link
      class="box"
      v-for="(numeroUnite, i) in numerosUnite"
      :key="i + 1"
      v-bind:to="'/stats/' + numeroUnite"
    >
      <div class="number">
        <div class="title">Unité</div>
        <div class="unite">{{i + 1}}</div>
      </div>
    </router-link>
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
  padding: 50px 100px;
  text-decoration: none;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.box {
  text-decoration: none;
  color: white;
  margin: 50px 100px;
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50px;
  background-color: #272727;
  border: 2px solid #272727;
  transition: 0.4s ease-in-out;
}

.box:hover {
  filter: brightness(1.5);
  border: 2px solid white;
}

.number {
  border: 2px solid #616161;
  display: flex;
  align-items: center;
  border-radius: 10px;
  padding: 5px;
}

.title {
  padding: 0 10px;
}

.unite {
  font-size: 20px;
  padding: 5px 10px;
  border: 2px solid #616161;
  border-radius: 10px;
}
</style>
