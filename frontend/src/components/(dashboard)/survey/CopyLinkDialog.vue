<script setup lang="ts">
import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import { Eye, Info } from 'lucide-vue-next'

defineProps({
  code: {
    type: String,
    required: true,
  },
})

const handleLink = (code: string) => {
  navigator.clipboard.writeText(code)
}
</script>

<template>
  <Dialog>
    <DialogTrigger as-child>
      <Button
        variant="outline"
        class="uppercase"
        size="sm"
        @click="() => handleLink(code)"
      >
        <Eye class="w-4 h-4 mr-1" />
        Copy link
      </Button>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <!-- <DialogTitle>Forgot password</DialogTitle> -->
      </DialogHeader>
      <div class="grid gap-4 pt-4 text-center">
        <Info class="mx-auto h-16 w-16 text-primary" />
        <span class="text-2xl font-semibold text-primary">Survey Link Copied</span>
        <DialogDescription>
          Click button below to visit survey url
        </DialogDescription>
        <Button
          as="a"
          :href="`/s/${code}`"
          target="_blank"
          variant="default"
          class="block w-full text-center"
        >
          Visit Survey
        </Button>
      </div>
      <DialogFooter>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
