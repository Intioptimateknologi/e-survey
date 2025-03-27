<script setup lang="ts">
import Breadcrumb from "@/components/ui/breadcrumb/Breadcrumb.vue";
import BreadcrumbItem from "@/components/ui/breadcrumb/BreadcrumbItem.vue";
import BreadcrumbLink from "@/components/ui/breadcrumb/BreadcrumbLink.vue";
import BreadcrumbList from "@/components/ui/breadcrumb/BreadcrumbList.vue";
import BreadcrumbSeparator from "@/components/ui/breadcrumb/BreadcrumbSeparator.vue";

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'

import DashboardLayout from "@/layouts/DashboardLayout.vue";

import { SurveyCreatorModel } from 'survey-creator-core';
import { ref } from "vue";
import Label from "@/components/ui/label/Label.vue";
import Input from "@/components/ui/input/Input.vue";
import Button from "@/components/ui/button/Button.vue";
import { ArrowLeft, Save } from "lucide-vue-next";
import useApiFetch from "@/composables/useFetch";
import router from "@/router";
import { toast } from "@/components/ui/toast";
import SurveyCreator from "@/components/surveyjs/SurveyCreator.vue";
import Switch from "@/components/ui/switch/Switch.vue";
import FormDescription from "@/components/ui/form/FormDescription.vue";

definePage({
  meta: {
    title: 'Survey Creation',
    description: 'Survey creation page',
    requiresAuth: true,
  }
})

// Prepare
const creator = new SurveyCreatorModel();

// creator.showToolbox = true;
// creator.showPropertyGrid = true;
// creator.isAutoSave = true

creator.saveSurveyFunc = async function (survey: any) {
  toast({
    variant: "success",
    title: 'Success',
    description: 'You clicked survey save button!',
  })
}

const form = ref({
  title: '',
  description: '',
  start_time: '',
  end_time: '',
  limit: 5,
  is_anonymous: false
})

async function handleSave(): Promise<void> {
  try {
    if (new Date(form.value.start_time) >= new Date(form.value.end_time)) {
      toast({
        variant: "destructive",
        title: 'Validation Error',
        description: 'End time must be before start time',
      });
      return;
    }

    const json = JSON.stringify(creator.JSON);
    const payload = {
      title: form.value.title,
      description: form.value.description,
      start_time: form.value.start_time,
      end_time: form.value.end_time,
      is_anonymous: form.value.is_anonymous,
      limit: form.value.limit,
      json: json,
    }

    console.log("Payload:", payload);

    const { data, error } = await useApiFetch("/api/v1/survey/")
      .post(payload)
      .json<Survey>();

    if (error.value) {
      console.error("Error saving survey:", error.value);
      return;
    }

    if (data.value) {
      console.log("Survey saved successfully:", data.value);
      toast({
        variant: "success",
        title: 'Success',
        description: 'Survey saved successfully',
      })
      router.push('/survey')
    }
  } catch (error) {
    console.error("Error saving survey:", error);
  }
}

</script>

<template>
  <DashboardLayout>
    <div class="hidden">
      <Button variant="outline" class="mr-2" @click="$router.back()">
        <ArrowLeft class="w-3 h-3" />
      </Button>
    </div>

    <div class="flex justify-between mb-1">
      <div class="flex items-center">
        <span class="text-2xl">Survey Creation</span>
      </div>

      <AlertDialog>
        <AlertDialogTrigger>
          <Button variant="default">
            <Save class="w-4 h-4 mr-1" />
            Save
          </Button>
        </AlertDialogTrigger>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Are you sure?</AlertDialogTitle>
            <AlertDialogDescription>
              Are you sure to save this survey?
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction @click="handleSave()">Save</AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>

    <form class="flex flex-col gap-8 mb-4" @submit.prevent>
      <div class="flex items-center">
        <Label for="title" class="w-24 text-start mr-4">Title</Label>
        <Input id="title" class="w-[41rem]" v-model="form.title" />
      </div>
      <div class="flex items-center">
        <Label for="description" class="w-24 text-start mr-4">Description</Label>
        <Input id="description" class="w-[41rem]" v-model="form.description" />
      </div>

      <div class="flex items-center">
        <Label for="limit" class="w-24 text-start mr-4">Limit</Label>
        <Input id="limit" class="w-[41rem]" v-model="form.limit" type="number" min="1" />
      </div>

      <div class="flex items-center">
        <Label for="is_anonymous" class="w-24 text-start mr-4">Anonymous Survey</Label>
        <div>
          <Switch class="block" :model-value="form.is_anonymous"
            @update:model-value="(value) => form.is_anonymous = value" />
          <span class="text-xs text-primary mt-2">
            If this enabled, the survey will be anonymous (not including user biodata form as default in the first
            page).
          </span>
        </div>
      </div>

      <div class="flex gap-8">
        <div class="flex items-center">
          <Label for="start-time" class="w-24 text-start mr-4">Start Time</Label>
          <Input type="datetime-local" id="start-time" v-model="form.start_time" class="w-64"
            :min="new Date().toISOString().split('T')[0] + 'T00:00'" />
        </div>
        <div class="flex items-center">
          <Label for="end-time" class="w-24 text-start mr-4">End Time</Label>
          <Input type="datetime-local" id="end-time" v-model="form.end_time" class="w-64" :min="form.start_time" />
        </div>
      </div>
    </form>

    <!-- <form class="grid grid-cols-2 gap-4 mb-4 me-5 pe-5">
      <div class="flex items-center">
        <Label for="code" class="mr-5">Code</Label>
        <Input id="code" class="w-full" />
      </div>
    </form> -->

    <SurveyCreator :model="creator" />

    <template #breadcrumb>
      <Breadcrumb>
        <BreadcrumbList>
          <BreadcrumbItem class="hidden md:block">
            <BreadcrumbLink to="/">
              E-SURVEY
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator class="hidden md:block" />
          <BreadcrumbItem>
            <BreadcrumbLink to="/survey/list">
              List Survey
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator class="hidden md:block" />
          <BreadcrumbItem>
            <BreadcrumbPage>Creation</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>
  </DashboardLayout>
</template>