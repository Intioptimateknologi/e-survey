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

import useApiFetch from "@/composables/useFetch";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { Model } from "survey-core";

import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

definePage({
  meta: {
    title: 'Detail Respondent',
    description: 'Respondent detail page',
    requiresAuth: true,
  }
})

import { format } from 'date-fns';
import { id as localeId } from 'date-fns/locale';
import SurveyResultTable from "@/components/(dashboard)/survey/SurveyResultTable.vue";
import { ArrowLeft, Trash } from "lucide-vue-next";
import { toast } from "@/components/ui/toast";
import Button from "@/components/ui/button/Button.vue";

const router = useRouter()

const id = useRoute("/(dashboard)/respondents/[id]").params.id
const respondent = ref<Respondent | null>(null);
const survey = ref<Survey | null>(null);
const surveyJSON = ref(null);
const surveyModel = ref<Model | null>(null);

const getTime = (time: string) => format(new Date(time), "dd MMMM yyyy HH:mm", { locale: localeId })

async function fetchData() {
  try {
    const { data: result, error } = await useApiFetch(`/api/v1/respondent/${id}/`)
      .json<Respondent>();

    if (error.value) {
      console.error('-> Error fetching:', error.value);
      return;
    }

    if (result.value) {
      respondent.value = result.value
      survey.value = result.value.survey
      surveyJSON.value = JSON.parse(survey.value!!.json)
      surveyModel.value = new Model(surveyJSON.value)
    }
  } catch (error) {
    console.error('-> Unexpected error:', error);
  }
}

async function handleDelete() {
  try {
    const { error } = await useApiFetch(`/api/v1/respondent/${id}/`)
      .delete()
      .json<any>();

    if (error.value) {
      console.error("-> Error deleting:", error.value);
      return;
    }

    toast({
      variant: "success",
      title: 'Success',
      description: 'Respondent deleted successfully',
    })

    router.push('/respondents')
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

onMounted(async () => await fetchData());

</script>

<template>
  <DashboardLayout>
    <div class="flex justify-between mb-1">
      <div class="flex items-center">
        <span class="text-2xl">Detail Respondent</span>
      </div>
      <div class="flex items-center gap-2">
        <Button variant="outline" class="shadow" @click="$router.back()">
          <ArrowLeft class="w-3 h-3 me-1" />
          Back
        </Button>
        <AlertDialog>
          <AlertDialogTrigger>
            <Button variant="destructive" class="shadow">
              <Trash class="w-3 h-3 me-1" />
              Delete
            </Button>
          </AlertDialogTrigger>
          <AlertDialogContent>
            <AlertDialogHeader>
              <AlertDialogTitle>Delete Confirmation</AlertDialogTitle>
              <AlertDialogDescription>
                Are you sure you want to delete this data? This action cannot be undone.
              </AlertDialogDescription>
            </AlertDialogHeader>
            <AlertDialogFooter>
              <AlertDialogCancel>Cancel</AlertDialogCancel>
              <AlertDialogAction @click="handleDelete">Yes, Delete</AlertDialogAction>
            </AlertDialogFooter>
          </AlertDialogContent>
        </AlertDialog>
      </div>
    </div>

    <template v-if="respondent && survey">
      <div class="overflow-x-auto">
        <table class="table-auto border-collapse w-full">
          <tbody>
            <tr>
              <td class="border px-4 py-2 w-1/4">Name</td>
              <td class="border px-4 py-2">{{ respondent.bio?.name ?? '-' }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Email</td>
              <td class="border px-4 py-2">{{ respondent.bio?.email ?? '-' }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Survey</td>
              <td class="border px-4 py-2">
                <router-link to="/s/[code]" :params="{ code: survey?.code }">
                  {{ survey?.title ?? '-' }}
                </router-link>
              </td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Time</td>
              <td class="border px-4 py-2">{{ getTime(respondent.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="mt-3">
        <SurveyResultTable :survey="survey" :survey-model="surveyModel" :respondents="[respondent]" />
      </div>
    </template>

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
            <BreadcrumbLink to="/respondents">
              List Respondent
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator class="hidden md:block" />
          <BreadcrumbItem>
            <BreadcrumbPage>Detail</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>
  </DashboardLayout>
</template>