import { defineStore } from 'pinia';
import type { SpaceListItem } from '@/interfaces/SpaceListItem.interface';
import type { SpacePostItem } from '@/interfaces/SpacePostItem.interface';
import axios from 'axios';
import ApiRequests from '@/api/ApiRequests';

export const useSpaceStore = defineStore('space', {
  state: () => (
    {
      spaceList: [] as SpaceListItem[],
      isLoading: false as Boolean,
    }
  ),
  getters: {
    getSpaces: (state) => state.spaceList,
  },
  actions: {
    async fetchSpaces() {
      this.setIsLoading(true);
      try {
        const apiRequests = new ApiRequests();
        const spaces = await apiRequests.getSpaces();
        this.spaceList = spaces;
      } catch (error) {
        console.error('Failed to fetch posts:', error);
      }
    },

    postSpace(post: SpacePostItem){
      this.setIsLoading(true);
      const urlString = import.meta.env.VITE_API_URL + "/spaces";

      axios.post(urlString, post)
        .then((response) => {
          this.spaceList = response.data;
        })
        .catch((error) => {
          console.error('An error occurred while posting data:', error);
        })
        .finally(() => {
          this.setIsLoading(false);
        });

    },

    setIsLoading(value: boolean) {
      this.isLoading = value
    }
  },
})
