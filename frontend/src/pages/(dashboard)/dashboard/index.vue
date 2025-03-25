<script setup lang="ts">
import Breadcrumb from "@/components/ui/breadcrumb/Breadcrumb.vue";
import BreadcrumbItem from "@/components/ui/breadcrumb/BreadcrumbItem.vue";
import BreadcrumbLink from "@/components/ui/breadcrumb/BreadcrumbLink.vue";
import BreadcrumbList from "@/components/ui/breadcrumb/BreadcrumbList.vue";
import BreadcrumbSeparator from "@/components/ui/breadcrumb/BreadcrumbSeparator.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useAuthStore } from "@/stores/auth";
import { computed } from "vue";

definePage({
  meta: {
    title: 'Dashboard',
    description: 'Dashboard page',
    requiresAuth: true,
  }
})

const cards = [
  {
    title: 'Manage Users',
    description: 'Manage all users, including their roles and permissions.',
    icon: 'ph:user-list-light',
  },
  {
    title: 'Manage Roles',
    description: 'Manage all roles, including their permissions.',
    icon: 'ph:user-list-light',
  },
  {
    title: 'Manage Permissions',
    description: 'Manage all permissions, including their roles.',
    icon: 'ph:user-list-light',
  },
  {
    title: 'Manage Surveys',
    description: 'Manage all surveys, including their questions and options.',
    icon: 'ph:user-list-light',
  },
];

const userType = computed(() => useAuthStore().user?.profile.role)
</script>

<template>
  <DashboardLayout>

    <div
      :class="{ 'grid grid-cols-4 gap-4': userType === 'admin', 'grid grid-cols-2 gap-4': userType === 'member' }">
      <div v-for="(card, index) in cards" :key="index" class="rounded-xl bg-white p-4 shadow-lg">
        <div class="flex items-center space-x-4">
          <div class="h-6 w-6 flex-none rounded-full bg-primary text-white" :class="`i-${card.icon} i-2xl`" />
          <h2 class="text-lg font-semibold">{{ card.title }}</h2>
        </div>
        <p class="mt-2 text-muted-foreground">
          {{ card.description }}
        </p>
      </div>
    </div>

    <template #breadcrumb>
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem class="hidden md:block">
            <BreadcrumbLink to="/">
              E-SURVEY
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator class="hidden md:block" />
          <BreadcrumbItem>
            <BreadcrumbPage>Dashboard</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>
  </DashboardLayout>
</template>