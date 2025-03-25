import { defineAsyncComponent } from "vue";

const layouts: Record<string, ReturnType<typeof defineAsyncComponent>> = {
  dashboard: defineAsyncComponent(
    () => import("@/layouts/DashboardLayout.vue")
  ),
  auth: defineAsyncComponent(() => import("@/layouts/AuthLayout.vue")),
  default: defineAsyncComponent(() => import("@/layouts/DefaultLayout.vue")),
};

export default function getLayout(
  name: string
): ReturnType<typeof defineAsyncComponent> {
  return layouts[name] || layouts.default;
}
