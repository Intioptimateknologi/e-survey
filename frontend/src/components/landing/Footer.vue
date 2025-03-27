<script setup lang="ts">
import { ChevronsDown } from "lucide-vue-next";
import Separator from "@/components/ui/separator/Separator.vue";
</script>

<template>
  <footer
    id="footer"
    class="container py-24 pb-16 sm:py-32 sm:pb-24"
  >
    <div class="p-10 bg-muted/50 dark:bg-card border rounded-2xl">
      <div
        class="grid grid-cols-2 md:grid-cols-4 xl:grid-cols-6 gap-x-12 gap-y-8"
      >
        <div class="col-span-full xl:col-span-2">
          <a
            href="#"
            class="flex font-bold items-center"
          >
            <ChevronsDown
              class="bg-gradient-to-tr from-primary via-primary/70 to-primary rounded-lg w-9 h-9 mr-2 border text-white"
            />

            <h3 class="text-2xl">E-Survey</h3>
          </a>
        </div>

        <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Contact</h3>
          <div>
            <a
              href="https://wa.me/6285156151595"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Whatsapp
            </a>
          </div>

          <div>
            <a
              href="https://www.instagram.com/iotbusiness/"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Instagram
            </a>
          </div>

          <div>
            <a
              href="mailto:inti.optima.t@gmail.com"
              class="opacity-60 hover:opacity-100"
            >
              Email
            </a>
          </div>
        </div>

        <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Platforms</h3>
          <div>
            <a
              href="https://github.com/leoMirandaa/shadcn-vue"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Web
            </a>
          </div>
        </div>

        <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Help</h3>
          <div>
            <a
              href="https://wa.me/6285156151595"
              class="opacity-60 hover:opacity-100"
            >
              Contact Us
            </a>
          </div>

          <div>
            <a
              href="https://wa.me/6285156151595"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Report a Bug
            </a>
          </div>

          <div>
            <a
              href="https://wa.me/6285156151595"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Feedback
            </a>
          </div>
        </div>

        <div class="flex flex-col gap-2">
          <h3 class="font-bold text-lg">Socials</h3>
          <div>
            <a
              href="https://www.instagram.com/iotbusiness/"
              target="_blank"
              class="opacity-60 hover:opacity-100"
            >
              Instagram
            </a>
          </div>
        </div>
      </div>

      <Separator class="my-6" />
      <section className="">
        <h3 class="">
          &copy; 2025 E-SURVEY built by
          <a
            target="_blank"
            href="https://www.intioptima.com"
            className="text-primary transition-all border-primary hover:border-b-2"
          >
            Inti Optima Teknologi
          </a>
        </h3>
      </section>
    </div>
  </footer>
</template>

