import { defineStore } from 'pinia';
import type { SpaceListItem } from '@/interfaces/SpaceListItem.interface';
import type { SpacePostItem } from '@/interfaces/SpacePostItem.interface';
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
    fetchSpaces() {
      this.setIsLoading(true);
      const urlString = import.meta.env.VITE_API_URL + "/spaces";
      console.log(urlString);

      axios.get(urlString)
        .then((response) => {
          this.spaceList = response.data;
        })
        .catch((error) => {
          console.error('An error occurred while fetching data:', error);
        })
        .finally(() => {
          this.setIsLoading(false);
        });
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
