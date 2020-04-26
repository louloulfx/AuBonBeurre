import Vue from "vue";
import App from "./App.vue";
import vSelect from "vue-select";
import axios from "axios";
import router from "./routes/index";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);
Vue.component("v-select", vSelect);
Vue.config.productionTip = false;

new Vue({
    router,
    render: (h) => h(App),
}).$mount("#app");