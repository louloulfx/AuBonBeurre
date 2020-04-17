<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  name: "LineChart",
  props: {
    chartData: {
      type: Object,
      required: false
    }
  },
  data() {
    return {
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }
          ],
          xAxes: [
            {
              gridLines: {
                display: false
              }
            }
          ]
        },
        legend: {
          display: true
        },
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  mounted() {
    this.renderChart(this.chartData, this.options);
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: this.label,
        datasets: [
          {
            label: "Automate 1",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 2",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 3",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 4",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 5",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 6",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 7",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 8",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 9",
            backgroundColor: "#f87979",
            data: this.data
          },
          {
            label: "Automate 10",
            backgroundColor: "#f87979",
            data: this.data
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
