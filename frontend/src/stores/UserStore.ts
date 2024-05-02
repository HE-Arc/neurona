import {defineStore} from "pinia";
import {UserItem} from "@/interfaces/UserItem.interface";
import ApiRequests from "@/api/ApiRequests";

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
    async fetch() {
      if (!this.user) {
        const req = new ApiRequests();
        req.getProfile().then((user) => {
          this.user = user;
        });
      }
    },
    async updateUsername(username: string) {
      const req = new ApiRequests();
      await req.updateProfile('username', username)
      this.user.username = username;
    },
    async updateDisplayName(displayName: string) {
      const req = new ApiRequests();
      await req.updateProfile('display_name', displayName);
      this.user.display_name = displayName;
    },
    async updateAbout(about: string) {
      const req = new ApiRequests();
      await req.updateProfile('about', about);
      this.user.about = about;
    },
    async deleteAccount() {
      const req = new ApiRequests();
      await req.deleteAccount();
      this.logout();
    },
  },
  persist: {
    storage: sessionStorage,
    paths: ['token'],
  }
});
