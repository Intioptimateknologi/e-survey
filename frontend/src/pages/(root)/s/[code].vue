<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import { Model } from "survey-core";
import { SurveyComponent } from "survey-vue3-ui";
import useApiFetch from "@/composables/useFetch";
import DefaultLayout from "@/layouts/DefaultLayout.vue";
import { toast } from "@/components/ui/toast";
import { ApiResponse } from "@/types/api";

const route = useRoute("/(root)/s/[code]");
const router = useRouter();
const code = route.params.code

definePage({
  meta: {
    title: 'Pengisian Survey',
    description: 'Survey detail page',
    requiresAuth: true,
  }
})

import { LayeredDarkPanelless } from "survey-core/themes";

const data = ref<Survey | null>(null);
const surveyJSON = ref(null);
const surveyModel = ref<Model | null>(null);
const location = ref<{ latitude: number; longitude: number } | null>(null);

function checkIfItsClosed(status: boolean) {
  if (status === true) {
    toast({
      title: 'Error',
      description: 'Survey is closed',
      variant: 'destructive'
    })
    router.push('/s')
  } else {
    console.log('-> Survey is open');
  }
}

async function fetchData() {
  try {
    const { data: result, error, statusCode } = await useApiFetch(`/api/v1/survey/${code}/`)
      .json<Survey>();

    if (statusCode.value === 404) {
      toast({
        title: 'Error',
        description: 'Survey not found',
        variant: 'destructive'
      })
      router.push('/s')
      return;
    }

    if (error.value) {
      console.error('-> Error fetching surveys:', error.value);
      toast({
        title: 'Error',
        description: error.value.message,
        variant: 'destructive'
      })
      router.push('/s')
      return;
    }

    if (result.value) {
      data.value = result.value

      checkIfItsClosed(data.value.status.enough)

      let dataJSON = JSON.parse(result.value.json)

      if (data.value.is_anonymous !== true) {
        const biodata = await import('../../../components/surveyjs/json/biodata.json');

        if (Array.isArray(dataJSON.pages)) {
          dataJSON.pages.unshift(biodata.default.pages[0]);
        } else {
          dataJSON.pages = [biodata.default.pages[0]];
        }
      }

      surveyJSON.value = dataJSON
      surveyModel.value = new Model(surveyJSON.value)
      // surveyModel.value.applyTheme(LayeredDarkPanelless)
      surveyModel.value.onComplete.add(async function(sender, options) {
        await sendDataRespondent(sender.data);
      });

      // Request location access
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            location.value = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude
            };
          },
          (error) => {
            console.error('-> Error getting location:', error);
          }
        );
      }
    }
  } catch (error) {
    console.error('-> Unexpected error:', error);
  }
}

async function sendDataRespondent(results: any) {
  try {
    const bio = {
      email: results.email,
      name: results.name,
    }
    delete results.email
    delete results.name

    console.log('-> Results:', results);
    console.log('-> Bio:', bio);

    const payload = JSON.stringify({
      bio: bio,
      answer: results,
      location: location.value
    })

    const { data: result, error } = await useApiFetch('/api/v1/respondent/')
      .json<ApiResponse<Respondent>>()
      .post({
        survey: data.value?.id,
        bio: bio,
        answer: JSON.stringify(payload),
        latitude: location.value?.latitude,
        longitude: location.value?.longitude
      });

    if (error.value) {
      console.error('-> Error sending respondent data:', error.value);
      toast({
        title: 'Error',
        description: error.value.message,
        variant: 'destructive'
      })
      return;
    }

    if (result.value) {
      toast({
        title: 'Success',
        description: 'Survey sent successfully',
        variant: 'success'
      })
      //router.push('/s')
    }
  } catch (error) {
    console.error('-> Unexpected error:', error);
  }
}

onMounted(async() => await fetchData());

</script>

<template>
  <DefaultLayout :is-survey="true">
    <template v-if="data">
      <div v-if="surveyModel">
        <SurveyComponent :model="surveyModel" />
      </div>
      <p v-else>Loading survey...</p>
    </template>
  </DefaultLayout>
</template>

