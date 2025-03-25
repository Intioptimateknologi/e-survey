<script setup lang="tsx">
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

import { ColumnDef } from "@tanstack/vue-table";

const emit = defineEmits(["delete"])

const props = defineProps({
  survey: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const data = ref<Respondent[]>([])

async function getData(): Promise<void> {
  try {
    const { data: result, error } = await useApiFetch("/api/v1/respondent/?survey=" + props.survey.id)
      .json<ApiResponse<Respondent>>();

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

// async function handleEdit(code: number) {
//   router.push(`/survey/edit/${code}`);
// }

async function handleDelete(id: number) {
  try {
    const { error } = await useApiFetch(`/api/v1/respondent/${id}/`)
      .delete()
      .json<any>();

      if (error.value) {
        console.error("-> Error deleting:", error.value);
        return;
      }

      emit('delete', id);

      toast({
        variant: "success",
        title: 'Success',
        description: 'Respondent deleted successfully',
      })
      await getData();
  } catch (error) {
    console.error("-> Unexpected error:", error);
  }
}

function handleShow(id: number) {
  router.push(`/respondent/${id}`)
}

onMounted(async () => await getData())

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

const columns: ColumnDef<Respondent>[] = [
  {
    accessorKey: 'rowNumber',
    header: 'No',
    cell: ({ row }) => row.index + 1,
  },
  {
    accessorKey: 'name',
    header: 'Name',
    cell: ({ row }) => {
      const name = row.original.bio?.name

      if (name == null || name == '') {
        return 'Anonymous'
      } else {
        return name
      }
    },
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
      const id = row.original.id

      return (
        <div class="flex gap-2">
          {/* <Button
            class={"uppercase"}
            variant="outline"
            size="sm"
            onClick={() => handleEdit(id)}
          >
            <Pencil class="w-4 h-4 mr-1" />
            Edit
          </Button> */}
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
                  Are you sure you want to delete this item? This action cannot be undone.
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
                <AlertDialogAction onClick={() => handleDelete(id)}>Continue</AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
          <Button
            variant="default"
            class={"uppercase"}
            size="sm"
            onClick={() => handleShow(id)}
          >
            <Eye class="w-4 h-4 mr-1" />
            Show
          </Button>
        </div>
      );
    },
  },
]


</script>

<template>
  <DataTable :columns="columns" :data="data" />
</template>