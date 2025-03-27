<script setup lang="ts">
import Button from "@/components/ui/button/Button.vue";
import { cn } from '@/lib/utils'
import { useRoute } from "vue-router";

interface Item {
  title: string
  href: string
}

const $route = useRoute()

const sidebarNavItems: Item[] = [
  {
    title: 'Profile',
    href: '/settings',
  },
  {
    title: 'Account',
    href: '/settings/account',
  }
]
</script>

<template>
  <nav class="flex space-x-2 lg:flex-col lg:space-x-0 lg:space-y-1">
    <router-link v-for="item in sidebarNavItems" :to="item.href">
      <Button
        :key="item.title"
        variant="ghost"
        :class="cn(
          'w-full text-left justify-start',
          $route.path === `${item.href}` && 'bg-muted hover:bg-muted',
        )"
      >
        {{ item.title }}
      </Button>
    </router-link>
  </nav>
</template>
