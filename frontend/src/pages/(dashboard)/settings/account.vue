<script setup lang="ts">
import SettingLayout from "@/layouts/dashboard/SettingLayout.vue";

definePage({
  meta: {
    title: 'Settings Account',
    description: 'Settings page',
    requiresAuth: true,
  }
})

import { FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Separator } from '@/components/ui/separator'

import { Textarea } from '@/components/ui/textarea'
import { toast } from '@/components/ui/toast'
import { toTypedSchema } from '@vee-validate/zod'
import { FieldArray, useForm } from 'vee-validate'
import * as z from 'zod'
import { SaveIcon, X, XIcon } from "lucide-vue-next";
import { useAuthStore } from "@/stores/auth";
import useApiFetch from "@/composables/useFetch";

const passwordFormSchema = toTypedSchema(z.object({
  current_password: z
    .string({
      required_error: 'Please enter your current password.',
    }),
  new_password: z
    .string({
      required_error: 'Please enter your new password.',
    })
    .min(8, {
      message: 'Password must be at least 8 characters.',
    }),
  confirm_password: z
    .string({
      required_error: 'Please enter your confirm password.',
    })
}).superRefine((data, ctx) => {
  if (data.new_password !== data.confirm_password) {
    ctx.addIssue({
      code: z.ZodIssueCode.custom,
      message: 'Passwords do not match.',
    });
  }
  return true;
})

)


const userId = useAuthStore().user?.id

const { handleSubmit, resetForm } = useForm({
  validationSchema: passwordFormSchema,
  initialValues: {
    current_password: '',
    new_password: '',
    confirm_password: '',
  },
})

const onSubmit = handleSubmit(async (values) => {
  try {
    const { error, statusCode, response, data } = await useApiFetch(`/api/v1/users/${userId}/update-password/`)
      .post(values)
      .json<any>();

    if (error.value || statusCode.value !== 200) {
      toast({
        variant: 'destructive',
        title: 'Error',
        description: error.value.error,
      });
      return;
    }

    toast({
      variant: 'success',
      title: 'Success',
      description: 'Password updated successfully.',
    });
  } catch (error) {
    toast({
      variant: 'destructive',
      title: 'Unexpected Error',
      description: 'An unexpected error occurred.',
    });
  }
})
</script>

<template>
  <SettingLayout>
    <div>
      <h3 class="text-lg font-medium">
        Account
      </h3>
      <p class="text-sm text-muted-foreground">
        Manage your account settings.
      </p>
    </div>
    <Separator />
    <form class="space-y-8" @submit="onSubmit">
      <FormField v-slot="{ componentField }" name="current_password">
        <FormItem>
          <FormLabel>Current password</FormLabel>
          <FormControl>
            <Input type="password" placeholder="Enter your current password" v-bind="componentField" />
          </FormControl>
          <FormMessage />
        </FormItem>
      </FormField>

      <FormField v-slot="{ componentField }" name="new_password">
        <FormItem>
          <FormLabel>New password</FormLabel>
          <FormControl>
            <Input type="password" placeholder="Enter your new password" v-bind="componentField" />
          </FormControl>
          <FormMessage />
        </FormItem>
      </FormField>

      <FormField v-slot="{ componentField }" name="confirm_password">
        <FormItem>
          <FormLabel>Confirm new password</FormLabel>
          <FormControl>
            <Input type="password" placeholder="Enter your confirm password" v-bind="componentField" />
          </FormControl>
          <FormMessage />
        </FormItem>
      </FormField>

      <div class="flex gap-2 justify-start">
        <Button type="submit">
          <SaveIcon class="mr-1 h-4 w-4" />
          Update Password
        </Button>

        <Button type="button" variant="outline" @click="resetForm">
          <XIcon class="mr-1 h-4 w-4" />
          Reset
        </Button>
      </div>
    </form>
  </SettingLayout>
</template>
