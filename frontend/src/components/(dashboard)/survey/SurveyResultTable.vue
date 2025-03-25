<script setup lang="tsx">
import { onMounted, ref } from "vue";

import 'tabulator-tables/dist/css/tabulator.css';
import 'survey-analytics/survey.analytics.tabulator.css';
import { Tabulator } from 'survey-analytics/survey.analytics.tabulator';
import { Model } from "survey-core";
import jsPDF from "jspdf";
import { applyPlugin } from "jspdf-autotable";
applyPlugin(jsPDF);
import * as XLSX from "xlsx";

const props = defineProps({
  respondents: {
    type: Array<Respondent>,
    required: true
  },
  survey: {
    type: Object,
    required: true
  },
  surveyModel: {
    type: Model,
    required: true
  }
})

async function getData(): Promise<void> {
  try {
    const answers = props.respondents.map(item => JSON.parse(item.answer));
    const hasil = answers.map(item => JSON.parse(item))
    const extractedAnswers = hasil.map(item => item.answer);

    console.log('-> Load table:', extractedAnswers);

    const surveyDataTable = new Tabulator(
      props.surveyModel,
      extractedAnswers,
      { jspdf: jsPDF, xlsx: XLSX }
    );

    surveyDataTable.render('answerList');
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

onMounted(async () => await getData());

</script>

<template>
  <div id="answerList"></div>
</template>