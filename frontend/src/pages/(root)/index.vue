<script setup lang="ts">
import Navbar from "@/components/landing/Navbar.vue";
import Hero from "@/components/landing/Hero.vue";
import Benefits from "@/components/landing/Benefits.vue";
import Features from "@/components/landing/Features.vue";
import Services from "@/components/landing/Services.vue";
import HowItWorks from "@/components/landing/HowItWorks.vue";
import Sponsors from "@/components/landing/Sponsors.vue";
import Testimonials from "@/components/landing/Testimonials.vue";
import Team from "@/components/landing/Team.vue";
import Pricing from "@/components/landing/Pricing.vue";
import Community from "@/components/landing/Community.vue";
import Contact from "@/components/landing/Contact.vue";
import FAQ from "@/components/landing/FAQ.vue";
import Footer from "@/components/landing/Footer.vue";
</script>

<template>
  <Navbar />
  <Hero />
  <!-- <Sponsors /> -->
  <Benefits />
  <Features />
  <Services />
  <HowItWorks />
  <!-- <Testimonials /> -->
  <!-- <Team /> -->
  <Community />
  <Pricing />
  <Contact />
  <FAQ />
  <Footer />
</template>

<!-- <script setup lang="ts">
import Button from "@/components/ui/button/Button.vue";
import DefaultLayout from "@/layouts/DefaultLayout.vue";

definePage({
  meta: {
    title: 'Home',
    description: 'Home page'
  }
})
</script>

<template>
  <DefaultLayout>
    <div class="py-16 bg-gray-50 overflow-hidden lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="relative lg:flex lg:items-center">
          <div class="hidden lg:block lg:w-0 lg:flex-1">
            <img class="w-96 h-auto" src="/images/illustrations/about.jpg" alt="survey illustration" />
          </div>
          <div class="relative px-4 sm:px-6 lg:px-0 lg:grid lg:grid-cols-1 lg:gap-x-16">
            <div>
              <h1 class="text-4xl font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
                E-Survey
              </h1>
              <p class="mt-3 max-w-md mx-auto lg:mt-5 lg:max-w-3xl">
                Create, send, and analyze online surveys. Get the insights you need to make informed business decisions.
              </p>
              <div class="mt-8 sm:max-w-lg sm:mx-auto sm:text-center lg:text-left lg:mt-0">
                <p class="text-xl">
                  E-Survey is a free, open source alternative to Google Forms.
                </p>
              </div>
              <div class="mt-5 sm:text-center lg:text-left lg:mt-8">
                <Button class="block w-full justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500" @click="$router.push('/s')">
                  Start Using Our Service
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DefaultLayout>
</template>
 -->
