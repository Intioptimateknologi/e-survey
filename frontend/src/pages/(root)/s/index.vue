<script setup lang="ts">
import Button from "@/components/ui/button/Button.vue";
import Input from "@/components/ui/input/Input.vue";
import { toast } from "@/components/ui/toast";
import useApiFetch from "@/composables/useFetch";
import DefaultLayout from "@/layouts/DefaultLayout.vue";
import { FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form'
import { toTypedSchema } from "@vee-validate/zod";
import { useForm } from "vee-validate";
import { useRouter } from "vue-router";
import { z } from "zod";

definePage({
  meta: {
    title: 'Filling a survey',
    description: 'Survey page'
  }
})

const router = useRouter()

const formSchema = toTypedSchema(z.object({
  code: z.string({ required_error: 'Please enter your survey code.' }).min(1, { message: 'Please enter your survey code.' }),
}))

const { handleSubmit } = useForm({
  validationSchema: formSchema
})

const onSubmit = handleSubmit(async (values) => {
  try {
    const { statusCode } = await useApiFetch(`/api/v1/survey/${values.code}/`)
      .patch(values)
      .json<any>();

    if (statusCode.value !== 200) {
      toast({
        variant: 'destructive',
        title: 'Error',
        description: 'Survey not found.',
      });
      return;
    }

    toast({
      variant: 'success',
      title: 'Success',
      description: 'Survey found, redirecting...',
    });

    setTimeout(() => {
      router.push(`/s/${values.code}`)
    }, 2000)
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
  <DefaultLayout>
    <div class="py-16 bg-gray-50 overflow-hidden lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white shadow sm:rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Enter your survey code
            </h3>
            <div class="mt-2 max-w-xl text-sm text-gray-600">
              <p>
                Please enter your survey code below.
              </p>
            </div>
            <form class="mt-5 space-y-6" @submit.prevent="onSubmit">
              <FormField v-slot="{ componentField }" name="code">
                <FormItem>
                  <FormLabel class="block text-sm font-medium text-gray-700">Survey code</FormLabel>
                  <FormControl>
                    <Input type="text" placeholder="Your survey code" v-bind="componentField"
                      class="block w-full sm:text-sm" />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              </FormField>
              <div>
                <Button type="submit"
                  class="w-full justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                  Enter
                </Button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>
