import { createApp } from "vue";

import "survey-core/survey-core.css";
import "survey-creator-core/survey-creator-core.css";

import "./assets/index.css";
import "./assets/custom.css";

import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
import { surveyPlugin } from "survey-vue3-ui";
import { surveyCreatorPlugin } from "survey-creator-vue";

const app = createApp(App);
const pinia = createPinia();

app.use(router);
app.use(pinia);
app.use(surveyPlugin);
app.use(surveyCreatorPlugin);
app.mount("#app");
