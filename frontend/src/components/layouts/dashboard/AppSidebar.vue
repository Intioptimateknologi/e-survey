<script setup lang="ts">
import type { SidebarProps } from '@/components/ui/sidebar'

import NavMain from "./NavMain.vue"
import NavProjects from "./NavProjects.vue"
import NavUser from "@/components/layouts/dashboard/NavUser.vue"
import TeamSwitcher from "@/components/layouts/dashboard/TeamSwitcher.vue"

import Sidebar from "@/components/ui/sidebar/Sidebar.vue"
import SidebarContent from "@/components/ui/sidebar/SidebarContent.vue"
import SidebarFooter from "@/components/ui/sidebar/SidebarFooter.vue"
import SidebarHeader from "@/components/ui/sidebar/SidebarHeader.vue"
import SidebarRail from "@/components/ui/sidebar/SidebarRail.vue"

import {
  AudioWaveform,
  BookOpen,
  Bot,
  Command,
  Frame,
  GalleryVerticalEnd,
  Map,
  PieChart,
  Settings2,
  SquareTerminal,
  UsersRound,
} from 'lucide-vue-next'
import { useAuthStore } from "@/stores/auth";
import { computed } from "vue";

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: 'icon',
})

// This is sample data.
const data = {
  teams: [
    {
      name: 'Acme Inc',
      logo: GalleryVerticalEnd,
      plan: 'Enterprise',
    },
    {
      name: 'Acme Corp.',
      logo: AudioWaveform,
      plan: 'Startup',
    },
    {
      name: 'Evil Corp.',
      logo: Command,
      plan: 'Free',
    },
  ],
  navMain: [
    {
      title: 'Survey',
      url: '/survey',
      icon: BookOpen,
      isActive: true,
      items: [
        {
          title: 'List',
          url: '/survey',
        },
        {
          title: 'Creation',
          url: '/survey/add',
        },
      ],
    },
    {
      title: 'Respondent',
      url: '/respondent',
      icon: UsersRound,
      items: [
        {
          title: 'List',
          url: '/respondents',
        },
      ],
    },
    {
      title: 'User',
      url: '#',
      icon: UsersRound,
      items: [
        {
          title: 'List',
          url: '/user',
        },
        {
          title: 'Registration',
          url: '/user/registration',
        },
      ],
    },
    {
      title: 'Settings',
      url: '#',
      icon: Settings2,
      items: [
        {
          title: 'Profile',
          url: '/settings',
        },
        {
          title: 'Account',
          url: '/settings/account',
        },
      ],
      onlyAdmin: true
    },
  ],
  projects: [
    {
      name: 'Design Engineering',
      url: '#',
      icon: Frame,
    },
    {
      name: 'Sales & Marketing',
      url: '#',
      icon: PieChart,
    },
    {
      name: 'Travel',
      url: '#',
      icon: Map,
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <TeamSwitcher :teams="data.teams" />
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <!-- <NavProjects :projects="data.projects" /> -->
    </SidebarContent>
    <SidebarFooter class="pb-3">
      <NavUser />
    </SidebarFooter>
    <SidebarRail />
  </Sidebar>
</template>
