import { defineStore } from "pinia";
import { ref, computed } from "vue";
import type { User } from "@/types/user";
import type { AuthResponse } from "@/types/api";
import { API_BASE_URL } from "@/utils/api";

const KEY_ACCESS_TOKEN = "access_token";
const KEY_REFRESH_TOKEN = "refresh_token";

export const useAuthStore = defineStore("auth", () => {
  const accessToken = ref<string | null>(
    localStorage.getItem(KEY_ACCESS_TOKEN)
  );
  const refreshToken = ref<string | null>(
    localStorage.getItem(KEY_REFRESH_TOKEN)
  );
  const user = ref<User | null>(
    JSON.parse(localStorage.getItem("user") || "null")
  );

  const isAuthenticated = computed(() => !!accessToken.value);

  function setAuthData(data: AuthResponse) {
    accessToken.value = data.access;
    refreshToken.value = data.refresh;
    user.value = data.user;

    const isFirstNameNull = data.user.first_name === "";

    console.log(isFirstNameNull);

    const firstName = isFirstNameNull
      ? data.user.username.charAt(0).toUpperCase() + data.user.username.slice(1)
      : data.user.first_name;

    user.value = {
      ...data.user,
      first_name: firstName,
      profile: {
        ...data.user.profile,
        avatar: `${import.meta.env.VITE_API_ASSETS_BASE_URL}${
          data.user.profile.avatar
        }`,
      },
    };

    localStorage.setItem(KEY_ACCESS_TOKEN, data.access);
    localStorage.setItem(KEY_REFRESH_TOKEN, data.refresh);
    localStorage.setItem("user", JSON.stringify(data.user));
  }

  function setUser(user: User) {
    localStorage.setItem("user", JSON.stringify(user));
  }

  function setAccessToken(token: string) {
    accessToken.value = token;
    localStorage.removeItem(KEY_ACCESS_TOKEN);
    localStorage.setItem(KEY_ACCESS_TOKEN, token);
  }

  function setRefreshToken(token: string) {
    refreshToken.value = token;
    localStorage.setItem(KEY_REFRESH_TOKEN, token);
  }

  function logout() {
    accessToken.value = null;
    refreshToken.value = null;
    user.value = null;

    localStorage.removeItem(KEY_ACCESS_TOKEN);
    localStorage.removeItem(KEY_REFRESH_TOKEN);
    localStorage.removeItem("user");
  }

  /**
   * Fungsi untuk merefresh token akses menggunakan refresh token.
   * @returns {Promise<string | null>} Token baru jika berhasil, null jika gagal.
   */
  async function refreshAccessToken(): Promise<string | null> {
    if (!refreshToken.value) {
      logout();
      return null;
    }

    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/token/refresh/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh_token: refreshToken.value }),
      });

      if (!response.ok) {
        logout(); // Jika refresh gagal, otomatis logout
        return null;
      }

      const data = await response.json();
      accessToken.value = data.access;
      localStorage.setItem(KEY_ACCESS_TOKEN, data.access);

      return data.access;
    } catch (error) {
      console.error("-> Failed to refresh token:", error);
      logout();
      return null;
    }
  }

  return {
    accessToken,
    refreshToken,
    user,
    isAuthenticated,
    setAuthData,
    setUser,
    setAccessToken,
    setRefreshToken,
    logout,
    refreshAccessToken,
  };
});
