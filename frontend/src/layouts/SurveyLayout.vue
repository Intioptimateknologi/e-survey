<script setup lang="ts">
import Footer from "@/components/landing/Footer.vue";
import ToggleTheme from "@/components/landing/ToggleTheme.vue";
import Button from "@/components/ui/button/Button.vue";
import { HomeIcon } from "lucide-vue-next";
</script>

<template>
  <header class="bg-white shadow-sm py-4 mt-16">
    <div class="px-60 mx-auto flex justify-between items-center">
      <div class="flex items-center">
        <router-link to="/">
          <h1 class="text-2xl font-bold text-green-600">E-SURVEY</h1>
        </router-link>
      </div>
      <div class="flex items-center">
        <Button variant="outline" size="sm">
          <router-link to="/">
            <HomeIcon class="w-4 h-4" />
          </router-link>
        </Button>
        <!-- <Button variant="ghost" size="sm">
          <ToggleTheme />
        </Button> -->
      </div>
    </div>
  </header>
  <slot />
</template>