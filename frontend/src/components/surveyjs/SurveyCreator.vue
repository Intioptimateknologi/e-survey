<script setup lang="ts">
import type { ICreatorOptions } from "survey-creator-core";
import { SurveyCreatorModel } from "survey-creator-core";
import { SurveyCreatorComponent } from "survey-creator-vue";

const creatorOptions: ICreatorOptions = {
  autoSaveEnabled: true,
  collapseOnDrag: true
};
const creator = new SurveyCreatorModel(creatorOptions);
</script>

<template>
  <SurveyCreatorComponent :model="creator" />
</template>
