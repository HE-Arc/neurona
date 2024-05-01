import {defineStore} from 'pinia';
import type {PostListItem} from '@/interfaces/PostListItem.interface';
import ApiRequests from '@/api/ApiRequests';

export const usePostStore = defineStore('post', {
  state: () => (
    {
      postList: [] as PostListItem[],
      isLoading: false as Boolean,
    }
  ),
  getters: {
    getPosts: (state) => state.postList,
    getPostsBySpaceId: (state) => (spaceId: string) => {
      return state.postList.filter(post => post.space === spaceId);
    },
  },
  actions: {
    async fetchPosts() {
      this.setIsLoading(true);
      try {
        const apiRequests = new ApiRequests();
        const posts = await apiRequests.getPosts();
        this.postList = posts;
      } catch (error) {
        console.error('Failed to fetch posts:', error);
      }
    },

    async fetchPostsBySpaceId(spaceId: string) {
      this.setIsLoading(true);
      try {
        const apiRequests = new ApiRequests();
        const posts = await apiRequests.getPostsFromSpace(spaceId);
        this.postList = posts;
        console.log("Fetched posts:", posts);
      } catch (error) {
        console.error('Failed to fetch posts:', error);
      }
    },

    setIsLoading(value: boolean) {
      this.isLoading = value;
    }
  },
})
