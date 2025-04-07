<script lang="ts">
export const description
  = 'A login page with two columns. The first column has the login form with email and password. There\'s a Forgot your passwork link and a link to sign up if you do not have an account. The second column has a cover image.'
export const iframeHeight = '800px'
export const containerClass = 'w-full h-full p-4 lg:p-0'
</script>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useAuthStore } from "@/stores/auth";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { useToast } from "@/components/ui/toast";
import { Eye, EyeOffIcon, LogIn } from "lucide-vue-next";
import useApiFetch from "@/composables/useFetch";
import { toTypedSchema } from "@vee-validate/zod";
import { z } from "zod";
import { useForm } from "vee-validate";
import { FormField } from "@/components/ui/form";
import FormItem from "@/components/ui/form/FormItem.vue";
import FormLabel from "@/components/ui/form/FormLabel.vue";
import FormControl from "@/components/ui/form/FormControl.vue";
import FormMessage from "@/components/ui/form/FormMessage.vue";
import FormDescription from "@/components/ui/form/FormDescription.vue";
import { useRouter } from "vue-router";

definePage({
  meta: {
    title: "Register",
    description: "register page",
    requiresAuth: false,
    guestOnly: true
  },
});

const loading = ref(false);
const errorMessage = ref("");
const router = useRouter();
const { toast } = useToast()

const formSchema = toTypedSchema(z.object({
  first_name: z.string({ required_error: 'Please select a first name.' }).max(30, { message: 'First name must not be longer than 30 characters.' }),
  last_name: z.string().max(30, { message: 'Last name must not be longer than 30 characters.' }),
  username: z.string({ required_error: 'Please select a username.' }),
  email: z.string({ required_error: 'Please select an email to display.' }).email({ message: 'Please enter a valid email.' }),
  password: z.string(),
}))

const { handleSubmit } = useForm({
  validationSchema: formSchema,
  initialValues: {
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
  },
});

const showPassword = ref(false);
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
}

const onSubmit = handleSubmit(async (values) => {
  loading.value = true;
  errorMessage.value = "";

  try {
    const { data, statusCode, error } = await useApiFetch("/api/v1/register/")
      .post(values)
      .json();

      console.log('SC:', statusCode.value);
      console.log('DATA:', data.value);
      console.log('ERROR:', error.value);

    if (statusCode.value != 200 && error.value) {
      errorMessage.value = "Failed to register, please check your information.";
      toast({
        variant: 'destructive',
        title: 'Something Went Wrong',
        description: 'Failed to register, please check your information.',
      });
      return;
    }


      toast({
        variant: "success",
        title: 'Register successfully',
        description: 'You have successfully registered',
      });
      router.push("/login");
  } catch (err) {
    errorMessage.value = "Something went wrong!";
  } finally {
    loading.value = false;
  }
})
</script>

<template>
  <AuthLayout>
    <div class="mx-auto grid w-[350px] gap-6">
      <div class="grid gap-2 text-center">
        <h1 class="text-3xl font-bold">REGISTER</h1>
        <p class="text-balance text-muted-foreground">
          Enter your information below to register
        </p>
      </div>
      <form class="grid gap-4" @submit.prevent="onSubmit">
        <div class="grid grid-cols-2 gap-2">
          <FormField v-slot="{ componentField }" name="first_name">
            <FormItem>
              <FormLabel>First name</FormLabel>
              <FormControl>
                <Input type="text" placeholder="John" v-bind="componentField" required />
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
        <div class="grid gap-2">
          <FormField v-slot="{ componentField }" name="username">
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input type="text" placeholder="johndoe23" v-bind="componentField" required />
              </FormControl>
              <FormDescription>
                This is your public display name. It can be your real name or a pseudonym.
              </FormDescription>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>
        <div class="grid gap-2">
          <FormField v-slot="{ componentField }" name="email">
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input type="email" placeholder="johndoe@gmail.com" v-bind="componentField" required />
              </FormControl>
              <FormDescription>
                Please make sure an email you entered is an valid email address.
              </FormDescription>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>
        <div class="grid gap-2">
          <FormField v-slot="{ componentField }" name="password">
            <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <div class="relative w-full max-w-sm items-center">
                  <Input
                    :type="showPassword ? 'text' : 'password'"
                    v-bind="componentField"
                    required
                  />
                  <Button
                    type="button"
                    variant="outline"
                    size="icon"
                    className="absolute top-1 right-3 mt-2"
                    @click="togglePasswordVisibility"
                  >
                    <Eye v-if="showPassword" class="size-4 text-muted-foreground" />
                    <EyeOffIcon v-else class="size-4 text-muted-foreground" />
                    <span class="sr-only">Toggle password visibility</span>
                  </Button>
                </div>
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>
        <p v-if="errorMessage" class="text-red-500 text-sm">{{ errorMessage }}</p>
        <Button :disabled="loading" type="submit" class="w-full">
          <LogIn class="mr-1 h-4 w-4" />
          {{ loading ? "Registering..." : "Register" }}
        </Button>
      </form>
      <div class="mt-4 text-center text-sm">
        Already have an account?
        <router-link to="/login" class="underline"> Sign in</router-link>
      </div>
    </div>
  </AuthLayout>
</template>
