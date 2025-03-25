<script lang="ts" setup>
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'
import { RouterLink, type RouterLinkProps } from 'vue-router'

const props = withDefaults(defineProps<RouterLinkProps & { class?: HTMLAttributes['class'] }>(), {
  custom: true,
})
</script>

<template>
  <RouterLink
    v-slot="{ href, navigate }"
    :to="props.to"
    :replace="props.replace"
    :custom="props.custom"
  >
    <a
      :href="href"
      class="transition-colors hover:text-foreground"
      @click="navigate"
    >
      <slot />
    </a>
  </RouterLink>
</template>

