<script setup lang="ts">
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

interface FAQProps {
  question: string;
  answer: string;
  value: string;
}

const FAQList: FAQProps[] = [
  {
    question: "Is E-Survey free?",
    answer: "Yes. E-Survey is a free, open source alternative to Google Forms.",
    value: "item-1",
  },
  {
    question: "What kind of questions can I ask?",
    answer:
      "You can ask multiple choice, short answer, paragraph, or rating scale questions.",
    value: "item-2",
  },
  {
    question: "Can I customize the design of my survey?",
    answer:
      "Yes. You can customize the design of your survey by using our built-in themes or by using your own CSS.",
    value: "item-3",
  },
  {
    question: "How do I get started?",
    answer: "Sign up for an account and start creating your survey.",
    value: "item-4",
  },
  {
    question: "Is E-Survey secure?",
    answer: "Yes. E-Survey is built with security in mind.",
    value: "item-5",
  },
];
</script>

<template>
  <section id="faq" class="container md:w-[700px] py-24 sm:py-32">
    <div class="text-center mb-8">
      <h2 class="text-lg text-primary text-center mb-2 tracking-wider">FAQS</h2>

      <h2 class="text-3xl md:text-4xl text-center font-bold">
        Common Questions
      </h2>
    </div>

    <Accordion type="single" collapsible class="AccordionRoot">
      <AccordionItem v-for="{ question, answer, value } in FAQList" :key="value" :value="value">
        <AccordionTrigger class="text-left"> {{ question }} </AccordionTrigger>

        <AccordionContent>{{ answer }}</AccordionContent>
      </AccordionItem>
    </Accordion>

    <h3 class="font-medium mt-4">
      Still have questions?
      <a href="#" class="text-muted-foreground">
        <a href="https://wa.me/6285156151595" target="_blank" class="text-primary">Contact us</a>
      </a>
    </h3>
  </section>
</template>
