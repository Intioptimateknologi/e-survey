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
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Info } from 'lucide-vue-next'
</script>

<template>
  <Dialog>
    <DialogTrigger as-child>
      <span class="ml-auto inline-block text-sm underline cursor-pointer">
        Forgot your password?
      </span>
    </DialogTrigger>
    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <!-- <DialogTitle>Forgot password</DialogTitle> -->
      </DialogHeader>
      <div class="grid gap-4 pt-4 text-center">
        <Info class="mx-auto h-16 w-16 text-primary" />
        <span class="text-2xl font-semibold text-primary">Forgot Your Password?</span>
        <DialogDescription>
          Please contact our admin to reset your password
        </DialogDescription>
        <Button
          as="a"
          href="https://wa.me/6285156151595"
          target="_blank"
          variant="default"
          class="block w-full text-center"
        >
          Click here to contact us via whatsapp
        </Button>
      </div>
      <DialogFooter>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>
