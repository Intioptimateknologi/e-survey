<script setup lang="ts">
import ThemeToggle from "@/components/utils/ThemeToggle.vue";
</script>

<template>
  <div class="w-full lg:grid lg:grid-cols-2 min-h-screen">
    <div class="flex items-center justify-center py-12">
      <div>
        <div class="flex items-center justify-center">
          <router-link to="/">
            <img src="/logo.png" class="h-24 my-2" />
          </router-link>
        </div>
        <slot />
      </div>
    </div>
    <div class="hidden bg-muted lg:block">
      <!-- https://images.unsplash.com/photo-1605379399642-870262d3d051?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80 -->
      <img
        src="/images/auth-bg.jpg"
        alt="Image" width="1920" height="1080"
        class="h-full w-full object-cover object-center">
        <!-- dark:brightness-[0.2] dark:grayscale -->
    </div>
  </div>

  <footer class="fixed bottom-0 right-0 p-4">
    <div class="flex items-center justify-end gap-2 bg-background p-2 rounded-xl shadow-lg">
      <ThemeToggle />
    </div>
  </footer>
</template>
