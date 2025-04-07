<script lang="ts" setup>
import { ref } from "vue";

import { useColorMode } from "@vueuse/core";
const mode = useColorMode();
mode.value = "light";

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu";
import {
  Sheet,
  SheetContent,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

import { ChevronsDown, LayoutDashboardIcon, LogInIcon, Menu } from "lucide-vue-next";
import ToggleTheme from "./ToggleTheme.vue";
import { useAuthStore } from "@/stores/auth";

interface RouteProps {
  href: string;
  label: string;
}

interface FeatureProps {
  title: string;
  description: string;
}

const routeList: RouteProps[] = [
  // {
  //   href: "#testimonials",
  //   label: "Testimonials",
  // },
  // {
  //   href: "#team",
  //   label: "Team",
  // },
  {
    href: "#contact",
    label: "Contact",
  },
  {
    href: "#faq",
    label: "FAQ",
  },
  {
    href: "/about",
    label: "About",
  },
];

const featureList: FeatureProps[] = [
  {
    title: "Collect Insights",
    description:
      "Collect insights from your customers and users with our powerful survey tools.",
  },
  {
    title: "Analyze Results",
    description: "Analyze the results of your surveys with our powerful analytics tools.",
  },
  {
    title: "Make Data-driven Decisions",
    description:
      "Make data-driven decisions with the insights you collect from your surveys.",
  },
];

const isOpen = ref<boolean>(false);
const authStore = useAuthStore()
</script>

<template>
  <header :class="{
    'shadow-light': mode === 'light',
    'shadow-dark': mode === 'dark',
    'w-[90%] md:w-[70%] lg:w-[75%] lg:max-w-screen-xl top-5 mx-auto sticky border z-40 rounded-2xl flex justify-between items-center p-2 bg-card shadow-md': true,
  }">
    <router-link to="/" class="font-bold text-lg flex items-center">
      <img src="/logo.png" class="rounded-lg size-9 mr-2" />
      E-SURVEY</router-link>
    <!-- Mobile -->
    <div class="sm:flex items-center lg:hidden">
      <Sheet v-model:open="isOpen">
        <SheetTrigger as-child>
          <Menu @click="isOpen = true" class="cursor-pointer" />
        </SheetTrigger>

        <SheetContent side="left" class="flex flex-col justify-between rounded-tr-2xl rounded-br-2xl bg-card">
          <div>
            <SheetHeader class="mb-4 ml-4">
              <SheetTitle class="flex items-center">
                <router-link to="/" class="flex items-center">
                  <img src="/logo.png" class="rounded-lg size-9 mr-2" />
                  E-SURVEY
                </router-link>
              </SheetTitle>
            </SheetHeader>

            <div class="flex flex-col gap-2">
              <Button v-for="{ href, label } in routeList" :key="label" as-child variant="ghost"
                class="justify-start text-base">
                <a v-if="href.includes('#')" @click="isOpen = false" :href="'/' + href">
                  {{ label }}
                </a>
                <router-link v-else @click="isOpen = false" :to="href">
                  {{ label }}
                </router-link>
              </Button>
            </div>
          </div>

          <SheetFooter class="flex-col sm:flex-col justify-start items-start">
            <Separator class="mb-2" />

            <ToggleTheme />
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </div>

    <!-- Desktop -->
    <NavigationMenu class="hidden lg:block">
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavigationMenuTrigger class="bg-card text-base">
            Features
          </NavigationMenuTrigger>
          <NavigationMenuContent>
            <div class="grid w-[600px] grid-cols-2 gap-5 p-4">
              <img src="/images/survey.jpg" alt="Beach" class="h-full w-full rounded-md object-cover" />
              <ul class="flex flex-col gap-2">
                <li v-for="{ title, description } in featureList" :key="title"
                  class="rounded-md p-3 text-sm hover:bg-muted">
                  <p class="mb-1 font-semibold leading-none text-foreground">
                    {{ title }}
                  </p>
                  <p class="line-clamp-2 text-muted-foreground">
                    {{ description }}
                  </p>
                </li>
              </ul>
            </div>
          </NavigationMenuContent>
        </NavigationMenuItem>

        <NavigationMenuItem>
          <NavigationMenuLink asChild>
            <Button v-for="{ href, label } in routeList" :key="label" as-child variant="ghost"
              class="justify-start text-base">
              <a v-if="href.includes('#')" @click="isOpen = false" :href="'/' + href">
                {{ label }}
              </a>
              <router-link v-else @click="isOpen = false" :to="href">
                {{ label }}
              </router-link>
            </Button>
          </NavigationMenuLink>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>

    <div class="hidden lg:flex">
      <ToggleTheme />

      <Button as-child size="sm" variant="outline" aria-label="View features">
        <router-link to="/dashboard" v-if="authStore.isAuthenticated">
          <LayoutDashboardIcon class="h-4 w-4 mr-2" />
          Dashboard
        </router-link>
        <router-link to="/login" v-else>
          <LogInIcon class="h-4 w-4 mr-2" />
          Login
        </router-link>
      </Button>
    </div>
  </header>
</template>

<style scoped>
.shadow-light {
  box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.085);
}

.shadow-dark {
  box-shadow: inset 0 0 5px rgba(255, 255, 255, 0.141);
}
</style>
