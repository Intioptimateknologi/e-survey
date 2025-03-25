<script setup lang="ts">
import SettingLayout from "@/layouts/dashboard/SettingLayout.vue";

definePage({
  meta: {
    title: 'Settings Profile',
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
import { User } from "@/types/user";

const profileFormSchema = toTypedSchema(z.object({
  first_name: z
    .string({
      required_error: 'Please select a first name.',
    })
    .min(2, {
      message: 'First name must be at least 2 characters.',
    })
    .max(30, {
      message: 'First name must not be longer than 30 characters.',
    }),
  last_name: z
    .string()
    .max(30, {
      message: 'Last name must not be longer than 30 characters.',
    }),
  username: z
    .string({
      required_error: 'Please select a username.',
    })
    .min(2, {
      message: 'Username must be at least 2 characters.',
    })
    .max(30, {
      message: 'Username must not be longer than 30 characters.',
    }),
  email: z
    .string({
      required_error: 'Please select an email to display.',
    })
    .email(),
}))

const userData = useAuthStore().user

const userId = userData?.id

const { handleSubmit, resetForm } = useForm({
  validationSchema: profileFormSchema,
  initialValues: {
    first_name: userData?.first_name,
    last_name: userData?.last_name,
    username: userData?.username,
    email: userData?.email,
  },
})

const authStore = useAuthStore()

const onSubmit = handleSubmit(async (values) => {
  try {
    const { error } = await useApiFetch(`/api/v1/users/${userId}/`)
      .patch(values)
      .json<any>();

    if (error.value) {
      toast({
        variant: 'destructive',
        title: 'Error',
        description: 'Failed to update user information.',
      });
      return;
    }

    const oldUser = authStore.user;
    const newUser: User = {
      id: oldUser?.id!!,
      profile: oldUser?.profile!!,
      first_name: values.first_name,
      last_name: values.last_name,
      username: values.username,
      email: values.email,
    }

    authStore.setUser(newUser)

    toast({
      variant: 'success',
      title: 'Success',
      description: 'User information updated successfully.',
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
        Profile
      </h3>
      <p class="text-sm text-muted-foreground">
        This is how others will see you on the site.
      </p>
    </div>
    <Separator />
    <form class="space-y-8" @submit="onSubmit">
      <div class="grid grid-cols-2 gap-4">
        <FormField v-slot="{ componentField }" name="first_name">
          <FormItem>
            <FormLabel>First name</FormLabel>
            <FormControl>
              <Input type="text" placeholder="John" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>
        <FormField v-slot="{ componentField }" name="last_name">
          <FormItem>
            <FormLabel>Last name</FormLabel>
            <FormControl>
              <Input type="text" placeholder="Doe" v-bind="componentField" />
            </FormControl>
            <FormMessage />
          </FormItem>
        </FormField>
      </div>

      <FormField v-slot="{ componentField }" name="username">
        <FormItem>
          <FormLabel>Username</FormLabel>
          <FormControl>
            <Input type="text" placeholder="shadcn" v-bind="componentField" />
          </FormControl>
          <FormDescription>
            This is your public display name. It can be your real name or a pseudonym.
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>

      <FormField v-slot="{ componentField }" name="email">
        <FormItem>
          <FormLabel>Email</FormLabel>
          <FormControl>
            <Input type="text" placeholder="johndoe@gmail.com" v-bind="componentField" />
          </FormControl>
          <FormDescription>
            Please make sure an email you entered is an valid email address.
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>

      <div class="flex gap-2 justify-start">
        <Button type="submit">
          <SaveIcon class="mr-1 h-4 w-4" />
          Update profile
        </Button>

        <Button type="button" variant="outline" @click="resetForm">
          <XIcon class="mr-1 h-4 w-4" />
          Reset
        </Button>
      </div>
    </form>
  </SettingLayout>
</template>