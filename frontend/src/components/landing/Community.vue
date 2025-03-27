<script setup lang="ts">
import {
  Card,
  CardHeader,
  CardTitle,
  CardFooter,
  CardContent,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
</script>

<template>
  <section
    id="community"
    class="py-12"
  >
    <hr />
    <div class="container py-20 sm:py-20">
      <div class="lg:w-[60%] mx-auto">
        <Card
          class="bg-background shadow-none text-center flex flex-col items-center justify-center border-0"
        >
          <CardHeader>
            <CardTitle class="text-4xl md:text-5xl font-bold">
              Ready to use our
              <span
                class="text-transparent bg-gradient-to-r from-[#D247BF] to-primary bg-clip-text"
              >
                Service?
              </span>
            </CardTitle>
          </CardHeader>
          <CardContent class="lg:w-[80%] text-xl text-muted-foreground">
            Start creating surveys now! Connect with your audience, gather
            valuable insights, and grow your business. Click to dive in! 🚀
          </CardContent>

          <CardFooter>
            <Button as-child>
              <router-link
                to="/login"
              >
                Get Started
              </router-link>
            </Button>
          </CardFooter>
        </Card>
      </div>
    </div>
    <hr />
  </section>
</template>

