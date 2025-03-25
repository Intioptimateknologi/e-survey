<template>
  <div class="min-h-screen">
    <nav
      class="bg-green-700 shadow-lg flex justify-between p-4 w-full z-10"
    >
      <div class="flex items-center">
        <router-link to="/" class="flex items-center">
          <img src="/logo.png" class="h-8 w-8 mr-2" alt="Logo" />
          <span class="text-white font-bold text-2xl">E-SURVEY</span>
        </router-link>
      </div>
      <div class="hidden sm:block">
        <router-link
          v-for="route in routes"
          :key="route.name"
          :to="route.path"
          class="text-white mr-4 hover:text-white p-2 hover:border-2 hover:rounded-lg hover:border-green-400"
          exact-active-class="border-2 rounded-lg border-green-500"
        >
          {{ route.name }}
        </router-link>
      </div>
      <div class="sm:hidden">
        <button
          class="text-white hover:text-white hover:underline focus:outline-none"
          @click="isMenuOpen = !isMenuOpen"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>
        <transition
          enter-active-class="transition ease-out duration-100"
          enter-class="transform opacity-0 scale-95"
          enter-to-class="transform opacity-100 scale-100"
          leave-active-class="transition ease-in duration-75"
          leave-class="transform opacity-100 scale-100"
          leave-to-class="transform opacity-0 scale-95"
        >
          <div
            v-show="isMenuOpen"
            class="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1"
          >
            <router-link
              v-for="route in routes"
              :key="route.name"
              :to="route.path"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              :class="{ 'border-b-2 border-gray-300': $route.name === route.name }"
            >
              {{ route.name }}
            </router-link>
          </div>
        </transition>
      </div>
    </nav>
    <main :class="isSurvey ? 'pt-0' : 'pt-10'">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";

const isMenuOpen = ref(false);

const isSurvey = ref(false);

const authStore = useAuthStore();

const routes = [
  { name: "Home", path: "/" },
  { name: "About", path: "/about" },
  { name: "Fill Survey", path: "/s" },
  {
    name: authStore.isAuthenticated ? "Dashboard" : "Login/Register",
    path: authStore.isAuthenticated ? "/dashboard" : "/login",
  },
];
</script>


