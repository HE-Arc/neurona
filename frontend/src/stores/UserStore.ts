import {defineStore} from "pinia";
import {UserItem} from "@/interfaces/UserItem.interface";

export const useUserStore = defineStore('user', {
  state: () => (
    {
      user: null as UserItem | null,
      token: null as string | null,
    }
  ),
  getters: {
    isLoggedIn: (state) => state.token !== null,
  },
  actions: {
    login(user: UserItem, token: string) {
      this.user = user;
      this.token = token;
    },
    logout() {
      this.user = null;
      this.token = null;
    },
  },
  persist: {
    storage: sessionStorage,
    paths: ['token'],
  }
});
