<script lang="ts">
export const description
  = 'A login page with two columns. The first column has the login form with email and password. There\'s a Forgot your passwork link and a link to sign up if you do not have an account. The second column has a cover image.'
export const iframeHeight = '800px'
export const containerClass = 'w-full h-full p-4 lg:p-0'
</script>

<script setup lang="ts">
import { ref } from "vue";
import { useFetch } from "@vueuse/core";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import AuthLayout from "@/layouts/AuthLayout.vue";
import { useToast } from "@/components/ui/toast";

definePage({
  meta: {
    title: "Login Aja",
    description: "Login page",
    requiresAuth: false,
    guestOnly: true
  },
});

const email = ref("");
const password = ref("");
const loading = ref(false);
const errorMessage = ref("");
const authStore = useAuthStore();
const router = useRouter();
const { toast } = useToast()

async function handleLogin() {
  loading.value = true;
  errorMessage.value = "";

  try {
    const { data, error } = await useFetch("http://localhost:8000/api/v1/token/")
      .post({ username: email.value, password: password.value })
      .json();

    if (error.value) {
      errorMessage.value = "Invalid username or password";
      return;
    }

    if (data.value) {
      authStore.setAuthData(data.value);
      toast({
        variant: "success",
        title: 'Login successfully',
        description: 'You have successfully logged in',
      });
      router.push("/dashboard");
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
        <h1 class="text-3xl font-bold">RESET PASSWORD</h1>
        <p class="text-balance text-muted-foreground">
          Enter your email or username below to login to your account
        </p>
      </div>
      <div class="grid gap-4">
        <div class="grid gap-2">
          <Label for="email">Email/Username</Label>
          <Input v-model="email" id="email" type="email" placeholder="m@example.com" required />
        </div>
        <div class="grid gap-2">
          <div class="flex items-center">
            <Label for="password">Password</Label>
            <router-link to="/forgot-password" class="ml-auto inline-block text-sm underline">
              Forgot your password?
            </router-link>
          </div>
          <Input v-model="password" id="password" type="password" required />
        </div>
        <p v-if="errorMessage" class="text-red-500 text-sm">{{ errorMessage }}</p>
        <Button :disabled="loading" @click="handleLogin" class="w-full">
          {{ loading ? "Logging in..." : "Login" }}
        </Button>
        <Button variant="outline" class="w-full">Login with Google</Button>
      </div>
      <div class="mt-4 text-center text-sm">
        Don't have an account?
        <router-link to="/register" class="underline"> Sign up </router-link>
      </div>
    </div>
  </AuthLayout>
</template>
