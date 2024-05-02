import {defineStore} from 'pinia';
import type {SpaceListItem} from '@/interfaces/SpaceListItem.interface';
import ApiRequests from '@/api/ApiRequests';

const THROTTLE_TIME_MS = 500;

export const useSpaceStore = defineStore('space', {
  state: () => (
    {
      isLoading: false as Boolean,
      spaces: {} as Record<string, SpaceListItem>,
      currentListIndex: 0,
      searchResults: [] as SpaceListItem[],
      query: '',
      throttled: false,
    }
  ),
  getters: {
    joinedSpaces: (state) => Object.values(state.spaces).filter((space) => space.joined),
    getSpace: (state) => (id: string) => state.spaces[id],
  },
  actions: {
    async fetchSpaces() {
      const req = new ApiRequests();
      const spaces = await req.getSpacesJoined();
      spaces.forEach((space: SpaceListItem) => {
        this.spaces[space.id] = space;
      });
    },

    setIsLoading(value: boolean) {
      this.isLoading = value
    },

    async fetchSpaceIfNecessary(id: string) {
      if (!this.spaces[id]) {
        const req = new ApiRequests();
        this.spaces[id] = await req.getSpace(id);
      }
      return this.spaces[id];
    },

    updateSpacesList() {
      for (const space of this.searchResults) {
        if (!this.spaces[space.id]) {
          this.spaces[space.id] = space;
        }
      }
      console.log("size is now " + Object.keys(this.spaces).length);
    },

    async _search() {
      const req = new ApiRequests();
      this.searchResults = await req.searchSpaces(this.query);
      this.updateSpacesList();
    },

    async search() {
      if (!this.throttled) {
        this.throttled = true;
        await this._search();
        setTimeout(() => {
          this.throttled = false;
        }, THROTTLE_TIME_MS);
      }
    },

    async fetchNext() {
      try {
        //TODO
      } catch (error) {
      }
    },

    async joinSpace(spaceId: string) {
      const req = new ApiRequests();
      await req.joinSpace(spaceId);
      this.spaces[spaceId].joined = true;
    },

    async quitSpace(spaceId: string) {
      const req = new ApiRequests();
      await req.quitSpace(spaceId);
      this.spaces[spaceId].joined = false;
    }
  },
})
