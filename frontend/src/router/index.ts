import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";
import { routes } from "vue-router/auto-routes";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next("/");
  } else if (to.meta.guestOnly && authStore.isAuthenticated) {
    next("/dashboard");
  } else {
    next();
  }
});

router.afterEach((to) => {
  const pageTitle = to.meta?.title || "Beranda";
  const appSite = "E-SURVEY";
  document.title = pageTitle + " | " + appSite;
});

export default router;
