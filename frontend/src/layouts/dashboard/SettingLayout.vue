<script setup lang="ts">
import SidebarNav from "@/components/(dashboard)/settings/components/SidebarNav.vue";
import Separator from "@/components/ui/separator/Separator.vue";
import Breadcrumb from "@/components/ui/breadcrumb/Breadcrumb.vue";
import BreadcrumbItem from "@/components/ui/breadcrumb/BreadcrumbItem.vue";
import BreadcrumbLink from "@/components/ui/breadcrumb/BreadcrumbLink.vue";
import BreadcrumbList from "@/components/ui/breadcrumb/BreadcrumbList.vue";
import BreadcrumbSeparator from "@/components/ui/breadcrumb/BreadcrumbSeparator.vue";
import DashboardLayout from "../DashboardLayout.vue";

</script>

<template>
  <DashboardLayout>
    <div class="md:hidden">
      <!-- <VPImage
      alt="Forms"
      width="1280"
      height="1214" class="block" :image="{
        dark: '/examples/forms-dark.png',
        light: '/examples/forms-light.png',
      }"
    /> -->
    </div>
    <div class="hidden space-y-6 p-5 pb-16 md:block">
      <div class="space-y-0.5">
        <h2 class="text-2xl font-bold tracking-tight">
          Settings
        </h2>
        <p class="text-muted-foreground">
          Manage your account settings and set e-mail preferences.
        </p>
      </div>
      <Separator class="my-6" />
      <div class="flex flex-col space-y-8 lg:flex-row lg:space-x-12 lg:space-y-0">
        <aside class="-mx-4 lg:w-1/5">
          <SidebarNav />
        </aside>
        <div class="flex-1 lg:max-w-2xl">
          <div class="space-y-6">
            <slot />
          </div>
        </div>
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
            <BreadcrumbPage>Settings</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>
  </DashboardLayout>


</template>