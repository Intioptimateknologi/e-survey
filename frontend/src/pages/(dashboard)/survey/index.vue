<script setup lang="tsx">
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
import { ColumnDef } from "@tanstack/vue-table";

definePage({
  meta: {
    title: 'Survey List',
    description: 'Survey List page',
    requiresAuth: true,
  }
})

const router = useRouter()

const data = ref<Survey[]>([])

async function getData(): Promise<void> {
  try {
    const { data: result, error } = await useApiFetch("/api/v1/survey")
      .json<ApiResponse<Survey>>();

    if (error.value) {
      console.error("-> Error fetching surveys:", error.value);
      return;
    }

    if (result.value) {
      data.value = result.value.results;
    }
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

async function handleEdit(code: number) {
  router.push(`/survey/edit/${code}`);
}

async function handleDelete(code: number) {
  try {
    const { error } = await useApiFetch(`/api/v1/survey/${code}/`)
      .delete()
      .json<any>();

      if (error.value) {
        console.error("-> Error deleting survey:", error.value);
        return;
      }

      toast({
        variant: "success",
        title: 'Success',
        description: 'Survey deleted successfully',
      })
      await getData();
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

function handleShow(code: number) {
  router.push(`/survey/${code}`)
}

function handleAdd() {
  router.push('/survey/add')
}

function handleLink() {

}

onMounted(async () => {
  await getData()
})

import { h, ref } from 'vue'
import DataTable from "@/components/(dashboard)/survey/DataTable.vue";
import { ApiResponse } from "@/types/api";
import { onMounted } from "vue";

import { format } from 'date-fns';
import { id } from 'date-fns/locale';
import Button from "@/components/ui/button/Button.vue";
import { Eye, Pencil, Plus, Trash2 } from "lucide-vue-next";
import { useRouter } from "vue-router";
import useApiFetch from "@/composables/useFetch";
import { toast } from "@/components/ui/toast";
import CopyLinkDialog from "@/components/(dashboard)/survey/CopyLinkDialog.vue";

const columns: ColumnDef<Survey>[] = [
  {
    accessorKey: 'rowNumber',
    header: 'No',
    cell: ({ row }) => row.index + 1,
  },
  {
    accessorKey: 'title',
    header: 'Title',
    cell: ({ row }) => row.getValue('title'),
  },
  {
    accessorKey: 'progress',
    header: 'Progress',
    cell: ({ row }) => {
      const progress = row.original.progress
      const limit = row.original.limit

      return (
        <div class={`text-start`}>{progress}/{limit}</div>
      )
    }
  },
  {
    accessorKey: 'created_at',
    header: 'Created At',
    cell: ({ row }) =>
      format(new Date(row.getValue('created_at')), "dd MMMM yyyy HH:mm", { locale: id }), // Format waktu human-readable
  },
  {
    accessorKey: 'actions',
    header: 'Aksi',
    enableHiding: false,
    size: 100,
    cell: ({ row }) => {
      const code = row.original.code

      return (
        <div class="flex gap-2">
          <Button
            class={"uppercase"}
            variant="outline"
            size="sm"
            onClick={() => handleEdit(code)}
          >
            <Pencil class="w-4 h-4 mr-1" />
            Edit
          </Button>
          <AlertDialog>
            <AlertDialogTrigger>
              <Button
                variant="destructive"
                size="sm"
              >
                <Trash2 class="w-4 h-4 mr-1" />
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
                <AlertDialogAction onClick={() => handleDelete(code)}>Continue</AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
          <Button
            variant="default"
            class={"uppercase"}
            size="sm"
            onClick={() => handleShow(code)}
          >
            <Eye class="w-4 h-4 mr-1" />
            Show
          </Button>
          <CopyLinkDialog code={code} />
        </div>
      );
    },
  },
]


</script>

<template>


  <DashboardLayout>
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
            <BreadcrumbPage>List Survey</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>
    </template>

    <div class="flex justify-between mb-4">
      <div>
        <span class="text-2xl">List Survey</span>
      </div>
      <router-link to="/survey/add">
        <Button variant="default" size="sm">
          <Plus class="w-4 h-4 mr-1" />
          Create
        </Button>
      </router-link>
    </div>
    <DataTable :columns="columns" :data="data" />
  </DashboardLayout>
</template>