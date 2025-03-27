<script setup lang="ts">
import { LineChart } from '@/components/ui/chart-line'
import CustomChartTooltip from './ChartTooltip.vue'

const props = defineProps({
  data: {
    type: Array as () => Array<Record<string, number | string>>,
    required: true,
  },
  index: {
    type: String,
    required: true,
  },
  categories: {
    type: Array as () => string[],
    required: true,
  },
  yFormatter: {
    type: Function,
    default: (tick: any, i: number) => {
      return typeof tick === 'number'
        ? `$ ${new Intl.NumberFormat('us').format(tick).toString()}`
        : ''
    },
  },
  customTooltip: {
    type: Object as () => typeof CustomChartTooltip,
    default: CustomChartTooltip,
  },
})
</script>

<template>
  <LineChart
    :data="props.data"
    :index="props.index"
    :categories="props.categories"
    :custom-tooltip="props.customTooltip"
  />
</template>