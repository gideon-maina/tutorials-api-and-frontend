import Vue from "vue";
import Router from "vue-router";
import TutorialsList from "./components/TutorialsList"
import Tutorial from "./components/Tutorial"
import AddTutorial from "./components/AddTutorial"

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [{
            path: "/",
            alias: "/tutorials",
            name: "tutorials",
            component: TutorialsList
        },
        {
            path: "/tutorials/:id",
            name: "tutorial-details",
            component: Tutorial
        },
        {
            path: "/add",
            name: "add-tutorial",
            component: AddTutorial
        }
    ]
});
