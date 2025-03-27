<script setup lang="ts">
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Badge } from "@/components/ui/badge";

enum ProService {
  YES = 1,
  NO = 0,
}

interface ServiceProps {
  title: string;
  pro: ProService;
  description: string;
}

const serviceList: ServiceProps[] = [
  {
    title: "Custom Domain Integration",
    description:
      "Host your survey on a custom domain to increase credibility and make your survey more discoverable.",
    pro: 0,
  },
  {
    title: "Survey Embedding",
    description:
      "Embed our surveys on your website or blog to increase engagement and reach a wider audience.",
    pro: 0,
  },
  {
    title: "Survey Analytics",
    description:
      "Get detailed insights into your survey's performance with our analytics feature. Track responses, completion rates, and other key metrics.",
    pro: 0,
  },
  {
    title: "Advanced Survey Features",
    description:
      "Unlock advanced features like conditional logic, survey branching, and more with our Pro plan.",
    pro: 0,
  },
];
</script>

<template>
  <section
    id="services"
    class="container py-24 sm:py-32"
  >
    <h2 class="text-lg text-primary text-center mb-2 tracking-wider">
      Services
    </h2>

    <h2 class="text-3xl md:text-4xl text-center font-bold mb-4">
      Reach Your Audience
    </h2>
    <h3 class="md:w-1/2 mx-auto text-xl text-center text-muted-foreground mb-8">
      From sharing on social media to integrating with your email marketing campaigns, we have the tools to help you reach your target audience.
    </h3>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4"></div>

    <div
      class="grid sm:grid-cols-2 lg:grid-cols-2 gap-4 w-full lg:w-[60%] mx-auto"
    >
      <div
        v-for="{ title, description, pro } in serviceList"
        :key="title"
      >
        <Card class="bg-muted/60 dark:bg-card h-full relative">
          <CardHeader>
            <CardTitle>{{ title }}</CardTitle>
            <CardDescription>{{ description }}</CardDescription>
          </CardHeader>
          <Badge
            v-if="pro === ProService.YES"
            variant="secondary"
            class="absolute -top-2 -right-3"
            >PRO</Badge
          >
        </Card>
      </div>
    </div>
  </section>
</template>

