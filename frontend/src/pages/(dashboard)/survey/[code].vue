<script setup lang="ts">
import Breadcrumb from "@/components/ui/breadcrumb/Breadcrumb.vue";
import BreadcrumbItem from "@/components/ui/breadcrumb/BreadcrumbItem.vue";
import BreadcrumbLink from "@/components/ui/breadcrumb/BreadcrumbLink.vue";
import BreadcrumbList from "@/components/ui/breadcrumb/BreadcrumbList.vue";
import BreadcrumbSeparator from "@/components/ui/breadcrumb/BreadcrumbSeparator.vue";
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs'
import useApiFetch from "@/composables/useFetch";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { Model } from "survey-core";
import { SurveyComponent } from "survey-vue3-ui";

import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

definePage({
  meta: {
    title: 'Detail Survey',
    description: 'Survey detail page',
    requiresAuth: true,
  }
})

import { format } from 'date-fns';
import { id as localeId } from 'date-fns/locale';
import RespondentDataTable from "@/components/(dashboard)/survey/RespondentDataTable.vue";
import SurveyResultTable from "@/components/(dashboard)/survey/SurveyResultTable.vue";
import { ApiResponse } from "@/types/api";

const code = useRoute("/(dashboard)/survey/[code]").params.code

const survey = ref<Survey | null>(null);
const respondents = ref<Respondent[]>([]);
const surveyJSON = ref(null);
const surveyModel = ref<Model | null>(null);

function getTime(time: string) {
  return format(new Date(time), "dd MMMM yyyy HH:mm", { locale: localeId })
}

async function fetchData() {
  try {
    const { data: result, error } = await useApiFetch(`/api/v1/survey/${code}/`)
      .json<Survey>();

    if (error.value) {
      console.error('-> Error fetching surveys:', error.value);
      return;
    }

    if (result.value) {
      survey.value = result.value
      surveyJSON.value = JSON.parse(result.value.json)
      surveyModel.value = new Model(surveyJSON.value)

      await fetchRespondents()
    }
  } catch (error) {
    console.error('-> Unexpected error:', error);
  }
}

async function fetchRespondents(): Promise<void> {
  try {
    const { data: result, error } = await useApiFetch("/api/v1/respondent/?survey=" + survey.value?.id)
      .json<ApiResponse<Respondent>>();

    if (error.value) {
      console.error("-> Error fetching:", error.value);
      return;
    }

    if (result.value) {
      respondents.value = result.value.results;
    }
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

onMounted(async () => await fetchData());

/*
 * Respondent
 */
function handleRespondentDelete(id: number) {
  if (survey.value?.progress) {
    survey.value.progress -= 1
  }
}

</script>

<template>
  <DashboardLayout>
    <div class="flex justify-between mb-1">
      <div class="flex items-center">
        <span class="text-2xl">Detail Survey</span>
      </div>
    </div>

    <template v-if="survey">
      <div class="overflow-x-auto">
        <table class="table-auto border-collapse w-full">
          <tbody>
            <tr>
              <td class="border px-4 py-2 w-1/4">Title</td>
              <td class="border px-4 py-2">{{ survey.title }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Description</td>
              <td class="border px-4 py-2">{{ survey.description }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Progress</td>
              <td class="border px-4 py-2">{{ survey.progress }}/{{ survey.limit }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Start Time</td>
              <td class="border px-4 py-2">{{ getTime(survey.start_time) }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">End Time</td>
              <td class="border px-4 py-2">{{ getTime(survey.end_time) }}</td>
            </tr>
            <tr>
              <td class="border px-4 py-2">Anonymous Survey</td>
              <td class="border px-4 py-2">{{ survey.is_anonymous ? '✔️' : '❌' }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <Tabs default-value="preview">
        <TabsList>
          <TabsTrigger value="preview">
            Preview
          </TabsTrigger>
          <TabsTrigger value="data">
            List Respondent
          </TabsTrigger>
          <TabsTrigger value="result">
            Result
          </TabsTrigger>
        </TabsList>
        <TabsContent value="preview">
          <div v-if="surveyModel">
            <SurveyComponent :model="surveyModel" @complete="() => { }" />
          </div>
          <p v-else>Loading survey...</p>
        </TabsContent>
        <TabsContent value="data">
          <RespondentDataTable @delete="handleRespondentDelete" :survey="survey" />
        </TabsContent>
        <TabsContent value="result">
          <SurveyResultTable :survey="survey" :survey-model="surveyModel" :respondents="respondents" />
        </TabsContent>
      </Tabs>
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
            <BreadcrumbLink to="/survey/list">
              List Survey
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