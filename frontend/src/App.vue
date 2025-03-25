<script setup>
import { RouterView, RouterLink } from 'vue-router';
import Toaster from "@/components/ui/toast/Toaster.vue";
</script>

<template>
  <div>
    <Toaster />
    <main>
      <transition name="fade" mode="out-in">
        <RouterView />
      </transition>
    </main>
  </div>
</template>