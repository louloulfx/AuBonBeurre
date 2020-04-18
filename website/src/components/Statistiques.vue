<template>
  <div class="container">
    <div>
      <select>
        <option @click="random()" value="data1">data1</option>
        <option @click="random()" value="data2">data2</option>
        <option @click="random()" value="data3">data3</option>
        <option @click="random()" value="data4">data4</option>
        <option @click="random()" value="data5">data5</option>
        <option @click="random()" value="data6">data6</option>
      </select>
    </div>
    <line-chart :styles="myStyles" :chart-data="datacollection" />
    <div>
      <button @click="createPdf()" class="btn btn-default">
        Exporter en pdf
      </button>
    </div>
  </div>
</template>
<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  justify-content: center;
  text-align: end;
  min-height: 95vh;
}
</style>
<script>
import LineChart from "@/components/Chart";
import jsPDF from "jspdf";

export default {
  components: {
    LineChart,
  },
  data() {
    return {
      datacollection: null,
      label: [],
      data: [],
      automates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      automate: [],
    };
  },
  created() {
    this.random();
  },
  methods: {
    random() {
      this.automate = [];
      for (let j = 0; j < this.automates.length; j++) {
        this.data = [];
        this.label = [];
        let label = [];
        let data = [];
        for (let i = 1; i < 61; i++) {
          label.push(i);
          data.push(this.getRandomInt());
          this.label.push(i);
          this.data.push(this.getRandomInt());
        }
        this.automate.push(data);
      }

      this.fillData();
    },
    fillData() {
      this.datacollection = {
        labels: this.label,
        datasets: [
          {
            label: "Automate 1",
            backgroundColor: "#f87979",
            data: this.automate[0],
          },
          {
            label: "Automate 2",
            backgroundColor: "#e3b23c",
            data: this.automate[1],
            hidden: true,
          },
          {
            label: "Automate 3",
            backgroundColor: "#423e37",
            data: this.automate[2],
            hidden: true,
          },
          {
            label: "Automate 4",
            backgroundColor: "#611c35",
            data: this.automate[3],
            hidden: true,
          },
          {
            label: "Automate 5",
            backgroundColor: "#4da1a9",
            data: this.automate[4],
            hidden: true,
          },
          {
            label: "Automate 6",
            backgroundColor: "#2e5077",
            data: this.automate[5],
            hidden: true,
          },
          {
            label: "Automate 7",
            backgroundColor: "#4e8098",
            data: this.automate[6],
            hidden: true,
          },
          {
            label: "Automate 8",
            backgroundColor: "#092327",
            data: this.automate[7],
            hidden: true,
          },
          {
            label: "Automate 9",
            backgroundColor: "#767522",
            data: this.automate[8],
            hidden: true,
          },
          {
            label: "Automate 10",
            backgroundColor: "#e4572e",
            data: this.automate[9],
            hidden: true,
          },
        ],
      };
    },
    createPdf() {
      let canvas = document.getElementById("line-chart").toDataURL("image/png");
      let doc = new jsPDF("l", "mm", [1475, 425]);
      doc.addImage(canvas, "PNG", 10, 10);
      doc.save("yo.pdf");
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
  },
  computed: {
    myStyles() {
      return {
        height: "400px",
      };
    },
  },
};
</script>
