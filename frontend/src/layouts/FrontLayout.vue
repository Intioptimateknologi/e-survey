<script setup lang="ts">
import Navbar from "@/components/landing/Navbar.vue";
import Footer from "@/components/landing/Footer.vue";
</script>

<template>
  <Navbar />
  <slot />
  <Footer />
</template>