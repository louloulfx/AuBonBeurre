import Vue from "vue";
import Router from "vue-router";
import HomePage from "../components/HomePage";
import Statistiques from "../components/Statistiques";

Vue.use(Router);

const router = new Router({
    mode: "history",
    base: process.env.BASE_URL,
    routes: [{
            path: "/",
            name: "home",
            component: HomePage
        },
        {
            path: "/stats/:id",
            name: "statistiques",
            component: Statistiques
        }
    ]
});

export default router;