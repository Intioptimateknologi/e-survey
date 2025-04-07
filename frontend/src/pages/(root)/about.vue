<script setup lang="ts">
import DefaultLayout from "@/layouts/DefaultLayout.vue";
import FrontLayout from "@/layouts/FrontLayout.vue";

definePage({
  meta: {
    title: 'About',
    description: 'About page'
  }
})
</script>

<template>
  <FrontLayout>
    <div class="py-16 bg-gray-50 overflow-hidden lg:py-24">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex">
          <div class="w-full md:w-1/2">
          <img src="/images/illustrations/about.jpg" alt="About" class="w-full" />
        </div>
        <div class="w-full md:w-1/2 md:pl-12 py-24">
          <h1 class="text-3xl font-bold mb-4">About</h1>
          <p class="text-lg text-gray-600">
            This platform is a service that provides an easy-to-use online survey
            creation tool. With this platform, users can create surveys with a
            variety of questions and quickly distribute them to their audience.
            The platform also provides a data analysis tool to help users get
            insights from their survey results.
          </p>
          <p class="text-lg text-gray-600">
            By using this platform, users can save time and money compared to
            traditional survey methods. The platform is also easy to use and
            requires no programming skills.
          </p>
        </div>
        </div>
      </div>
    </div>
  </FrontLayout>
</template>
