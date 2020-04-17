<template>
  <div>
    <select>
      <option value="data1">data1</option>
      <option value="data2">data2</option>
      <option value="data3">data3</option>
      <option value="data4">data4</option>
      <option value="data5">data5</option>
      <option value="data6">data6</option>
    </select>
    <line-chart :chart-data="datacollection" />
  </div>
</template>
<script>
import LineChart from "@/components/Chart";

export default {
  components: {
    LineChart
  },
  data() {
    return {
      datacollection: null,
      label: [],
      data: [],
      automates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      automate: []
    };
  },
  created() {
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
      console.log(this.automate);
    }

    this.fillData();
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.label,
        datasets: [
          {
            label: "Automate 1",
            backgroundColor: "#f87979",
            data: this.automate[0]
          },
          {
            label: "Automate 2",
            backgroundColor: "#e3b23c",
            data: this.automate[1]
          },
          {
            label: "Automate 3",
            backgroundColor: "#423e37",
            data: this.automate[2]
          },
          {
            label: "Automate 4",
            backgroundColor: "#611c35",
            data: this.automate[3]
          },
          {
            label: "Automate 5",
            backgroundColor: "#4da1a9",
            data: this.automate[4]
          },
          {
            label: "Automate 6",
            backgroundColor: "#2e5077",
            data: this.automate[5]
          },
          {
            label: "Automate 7",
            backgroundColor: "#4e8098",
            data: this.automate[6]
          },
          {
            label: "Automate 8",
            backgroundColor: "#092327",
            data: this.automate[7]
          },
          {
            label: "Automate 9",
            backgroundColor: "#767522",
            data: this.automate[8]
          },
          {
            label: "Automate 10",
            backgroundColor: "#e4572e",
            data: this.automate[9]
          }
        ]
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    }
  }
};
</script>
