<script lang="ts">
export const description
  = 'A login page with two columns. The first column has the login form with email and password. There\'s a Forgot your passwork link and a link to sign up if you do not have an account. The second column has a cover image.'
export const iframeHeight = '800px'
export const containerClass = 'w-full h-full p-4 lg:p-0'
</script>

<script setup lang="ts">
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { useToast } from "@/components/ui/toast";
import { LogIn } from "lucide-vue-next";
import useApiFetch from "@/composables/useFetch";

definePage({
  meta: {
    title: "Register",
    description: "register page",
    requiresAuth: false,
    guestOnly: true
  },
});

const first_name = ref("");
const last_name = ref("");
const username = ref("");
const email = ref("");
const password = ref("");
const loading = ref(false);
const errorMessage = ref("");
const router = useRouter();
const { toast } = useToast()

async function handleRegister() {
  loading.value = true;
  errorMessage.value = "";

  try {
    const { data, error } = await useApiFetch("/api/v1/register/")
      .post({
        first_name: first_name.value,
        last_name: last_name.value,
        username: username.value,
        email: email.value,
        password: password.value,
      })
      .json();

    if (error.value) {
      errorMessage.value = "Invalid data";
      return;
    }

    if (data.value) {
      toast({
        variant: "success",
        title: 'Register successfully',
        description: 'You have successfully registered',
      });
      router.push("/login");
    }
  } catch (err) {
    errorMessage.value = "Something went wrong!";
  } finally {
    loading.value = false;
  }
}
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
      <form class="grid gap-4" @submit.prevent="handleRegister">
        <div class="grid grid-cols-2 gap-2">
          <div>
            <Label for="first_name">First Name</Label>
            <Input v-model="first_name" id="first_name" type="text" placeholder="John" required />
          </div>
          <div>
            <Label for="last_name">Last Name</Label>
            <Input v-model="last_name" id="last_name" type="text" placeholder="Doe" required />
          </div>
        </div>
        <div class="grid gap-2">
          <Label for="username">Username</Label>
          <Input v-model="username" id="username" type="text" placeholder="johndoe" required />
        </div>
        <div class="grid gap-2">
          <Label for="email">Email</Label>
          <Input v-model="email" id="email" type="email" placeholder="johndoe@example.com" required />
        </div>
        <div class="grid gap-2">
          <Label for="password">Password</Label>
          <Input v-model="password" id="password" type="password" required />
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