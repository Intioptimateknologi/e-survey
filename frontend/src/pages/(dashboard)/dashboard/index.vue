<script setup lang="tsx">
import Breadcrumb from "@/components/ui/breadcrumb/Breadcrumb.vue";
import BreadcrumbItem from "@/components/ui/breadcrumb/BreadcrumbItem.vue";
import BreadcrumbLink from "@/components/ui/breadcrumb/BreadcrumbLink.vue";
import BreadcrumbList from "@/components/ui/breadcrumb/BreadcrumbList.vue";
import BreadcrumbSeparator from "@/components/ui/breadcrumb/BreadcrumbSeparator.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import DashboardLineChart from "@/components/(dashboard)/dashboard/DashboardLineChart.vue"
import { useAuthStore } from "@/stores/auth";
import { computed, onMounted, ref } from "vue";
import Card from "@/components/ui/card/Card.vue";
import CardHeader from "@/components/ui/card/CardHeader.vue";
import CardTitle from "@/components/ui/card/CardTitle.vue";
import CardContent from "@/components/ui/card/CardContent.vue";
import { BookOpen, UserCheck2Icon, UserCog, Users } from "lucide-vue-next";
import useApiFetch from "@/composables/useFetch";
import { toast } from "@/components/ui/toast";
import { JSX } from "vue/jsx-runtime";
import Tabs from "@/components/ui/tabs/Tabs.vue";
import TabsList from "@/components/ui/tabs/TabsList.vue";
import TabsTrigger from "@/components/ui/tabs/TabsTrigger.vue";
import TabsContent from "@/components/ui/tabs/TabsContent.vue";
import DashboardLineChartOld from "@/components/(dashboard)/dashboard/DashboardLineChartOld.vue";

definePage({
  meta: {
    title: 'Dashboard',
    description: 'Dashboard page',
    requiresAuth: true,
  }
})

const loading = ref(true)
const apiData = ref<DashboardResponse | null>(null)
const userType = computed(() => useAuthStore().user?.profile.role)

type DashboardCard = {
  title: string;
  count: number;
  icon: JSX.Element;
  onlyAdmin?: boolean;
}

const cards = ref<DashboardCard[]>([
  {
    title: 'Total Surveys',
    count: 0,
    icon: <BookOpen />,
  },
  {
    title: 'Total Respondents',
    count: 0,
    icon: <Users />,
  },
  {
    title: 'Total Admin Users',
    count: 0,
    icon: <UserCog />,
    onlyAdmin: true,
  },
  {
    title: 'Total Member Users',
    count: 0,
    icon: <UserCheck2Icon />,
    onlyAdmin: true,
  },
])

async function fetchData() {
  try {
    const { data, statusCode } = await useApiFetch('/api/v1/dashboard/').json<DashboardResponse>();
    if (statusCode.value !== 200) {
      console.error(data);

      toast({
        variant: 'destructive',
        title: 'Error',
        description: 'Failed to fetch dashboard data.',
      })
    }

    if (data.value) {
      apiData.value = data.value
      cards.value[0].count = data.value.data.surveys;
      cards.value[1].count = data.value.data.respondents;
      cards.value[2].count = data.value.data.users.admin;
      cards.value[3].count = data.value.data.users.member;
    }
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false
  }
}

onMounted(async () => await fetchData());

</script>

<template>
  <DashboardLayout>
    <div :class="`grid gap-4 grid-cols-1 sm:grid-cols-${userType === 'member' ? 2 : 4} md:grid-cols-${userType === 'member' ? 2 : 4}`">
      <template v-for="(card, index) in cards" :key="index">
        <Card v-if="!(card.onlyAdmin && userType === 'member')">
          <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle class="text-sm font-medium">
              {{ card.title }}
            </CardTitle>
            <component :is="card.icon" class="h-6 w-6 text-primary" />
          </CardHeader>
          <CardContent>
            <div class="text-2xl font-bold">
              {{ card.count }}
            </div>
          </CardContent>
        </Card>
      </template>
    </div>

    <Tabs default-value="survey">
      <TabsList>
        <TabsTrigger value="survey">
          Survey
        </TabsTrigger>
        <TabsTrigger value="respondent">
          Respondent
        </TabsTrigger>
        <TabsTrigger v-if="userType === 'admin'" value="member">
          Member
        </TabsTrigger>
      </TabsList>
      <TabsContent value="survey">
        <Card class="mt-3" v-if="!loading">
          <CardContent class="pt-4">
            <DashboardLineChart :data="apiData!!.chart.survey_creation" index="date" :categories="['count']" />
          </CardContent>
        </Card>
        <p v-else>Loading content...</p>
      </TabsContent>
      <TabsContent value="respondent">
        <Card class="mt-3" v-if="!loading">
          <CardContent class="pt-4">
            <DashboardLineChart :data="apiData!!.chart.respondent_filling" index="date" :categories="['count']" />
          </CardContent>
        </Card>
        <p v-else>Loading content...</p>
      </TabsContent>
      <TabsContent value="member">
        <Card class="mt-3" v-if="!loading">
          <CardContent class="pt-4">
            <DashboardLineChart :data="apiData!!.chart.member_registration" index="date" :categories="['count']" />
          </CardContent>
        </Card>
        <p v-else>Loading content...</p>
      </TabsContent>
    </Tabs>

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
            <BreadcrumbPage>Dashboard</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>
  </DashboardLayout>
</template>