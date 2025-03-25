<script setup>
import { useRoute } from 'vue-router';
import DashboardLayout from "@/layouts/DashboardLayout.vue";

const route = useRoute("/(dashboard)/users/[id]");
const userId = route.params.id

</script>

<template>
  <DashboardLayout>
    <h1>Halaman User</h1>
    <p>ID User: {{ userId }}</p>
  </DashboardLayout>
</template>
