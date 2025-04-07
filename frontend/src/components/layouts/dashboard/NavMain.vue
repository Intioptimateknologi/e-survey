<script setup lang="ts">
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from '@/components/ui/collapsible'
import {
  SidebarGroup,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
} from '@/components/ui/sidebar'
import { useAuthStore } from "@/stores/auth";
import { ChevronRight, LayoutDashboardIcon, type LucideIcon } from 'lucide-vue-next'
import { computed } from "vue";

defineProps<{
  items: {
    title: string
    url: string
    icon?: LucideIcon
    isActive?: boolean
    onlyAdmin?: boolean,
    items?: {
      title: string
      url: string
    }[]
  }[]
}>()

const userType = computed(() => useAuthStore().user?.profile.role)
</script>

<template>
  <SidebarGroup>
    <SidebarGroupLabel>MENU</SidebarGroupLabel>
    <SidebarMenu>
      <SidebarMenuItem>
        <SidebarMenuButton tooltip="Dashboard">
          <LayoutDashboardIcon class="h-4 w-4" />
          <router-link to="/dashboard">Dashboard</router-link>
        </SidebarMenuButton>
      </SidebarMenuItem>
      <template v-for="item in items" :key="item.title">
        <Collapsible as-child :default-open="item.isActive" class="group/collapsible"
          v-if="!(item.onlyAdmin && userType === 'member')">
          <SidebarMenuItem>
            <CollapsibleTrigger as-child>
              <SidebarMenuButton :tooltip="item.title">
                <component :is="item.icon" v-if="item.icon" />
                <span>{{ item.title }}</span>
                <ChevronRight
                  class="ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
              </SidebarMenuButton>
            </CollapsibleTrigger>
            <CollapsibleContent>
              <SidebarMenuSub>
                <SidebarMenuSubItem v-for="subItem in item.items" :key="subItem.title">
                  <SidebarMenuSubButton as-child>
                    <router-link :to="subItem.url">
                      <span>{{ subItem.title }}</span>
                    </router-link>
                  </SidebarMenuSubButton>
                </SidebarMenuSubItem>
              </SidebarMenuSub>
            </CollapsibleContent>
          </SidebarMenuItem>
        </Collapsible>
      </template>
    </SidebarMenu>
  </SidebarGroup>
</template>
