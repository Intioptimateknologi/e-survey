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
  },
  // {
  //   title: 'Appearance',
  //   href: '/settings/appearance',
  // },
  // {
  //   title: 'Notifications',
  //   href: '/examples/forms/notifications',
  // },
  // {
  //   title: 'Display',
  //   href: '/examples/forms/display',
  // },
]
</script>

<template>
  <nav class="flex space-x-2 lg:flex-col lg:space-x-0 lg:space-y-1">
    <Button
      v-for="item in sidebarNavItems"
      :key="item.title"
      as="a"
      :href="item.href"
      variant="ghost"
      :class="cn(
        'w-full text-left justify-start',
        $route.path === `${item.href}` && 'bg-muted hover:bg-muted',
      )"
    >
      {{ item.title }}
    </Button>
  </nav>
</template>
