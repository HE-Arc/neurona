import { defineStore } from 'pinia';
import type { SpaceListItem } from '@/interfaces/SpaceListItem.interface';
import axios from 'axios';

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
        const urlString = process.env.VITE_API_ENDPOINT + "spaces/";
        const response = await axios.get(urlString);
        this.spaceList = response.data;
      } catch (error) {
        console.error('An error occurred while fetching data:', error);
      } finally {
        this.setIsLoading(false);
      }
    },

    setIsLoading(value: boolean) {
      this.isLoading = value
    }
  },
})
