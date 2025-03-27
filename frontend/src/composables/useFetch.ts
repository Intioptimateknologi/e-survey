import { useAuthStore } from "@/stores/auth";
import { API_BASE_URL } from "@/utils/api";
import { createFetch } from "@vueuse/core";

let isRefreshing = false;
const refreshSubscribers: Array<() => void> = [];

const authStore = useAuthStore();

const useApiFetch = createFetch({
  baseUrl: API_BASE_URL,
  combination: "overwrite",
  options: {
    async beforeFetch({ options }) {
      const accessToken = authStore.accessToken;
      if (accessToken !== null) {
        options.headers = {
          ...options.headers,
          Authorization: `Bearer ${accessToken}`,
        };
      }
      return { options };
    },
    onFetchError({ data, response, context, execute, error }) {
      // console.log(data, response, context, execute);
      const needRefreshToken =
        (response?.status === 401 || response?.status === 403) &&
        context.url !== `${API_BASE_URL}/api/v1/token/refresh/`;
      let isAuthenticated = true;
      const accessToken = authStore.accessToken;
      if (accessToken === null) {
        isAuthenticated = false;
      }

      if (needRefreshToken && isAuthenticated) {
        refreshToken().then((newToken) => {
          if (newToken.access) {
            isRefreshing = false;
            useAuthStore().setAccessToken(newToken.access);
            onRrefreshed();
          } else {
            refreshSubscribers.length = 0;
            // handle refresh token error
          }
        });

        return new Promise((resolve) => {
          addRefreshSubscriber(() => {
            execute().then((response) => {
              resolve({ data, response });
            });
          });
        });
      }

      return { error: data, data: error, response };
    },
  },
  fetchOptions: {
    mode: "cors",
  },
});

async function refreshToken() {
  const response = await fetch(`${API_BASE_URL}/api/v1/token/refresh/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ refresh: authStore.refreshToken }),
  });
  const data = await response.json();
  return data;
}

function onRrefreshed() {
  refreshSubscribers.forEach((callback) => callback());
  refreshSubscribers.length = 0;
}

function addRefreshSubscriber(callback: () => void) {
  refreshSubscribers.push(callback);
}

export default useApiFetch;

export const useCustomFetch = createFetch({
  baseUrl: API_BASE_URL,
  combination: "overwrite",
  fetchOptions: {
    mode: "cors",
  },
});
