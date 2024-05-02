import {defineStore} from 'pinia';
import type {PostListItem} from '@/interfaces/PostListItem.interface';
import ApiRequests from '@/api/ApiRequests';

const PAGE_SIZE = 10;

export const usePostStore = defineStore('post', {
  state: () => (
    {
      postList: [] as PostListItem[],
      isLoading: false as Boolean,

      homePosts: [] as PostListItem[],
      spacePosts: {} as Record<string, PostListItem[]>,
      userPosts: {} as Record<string, PostListItem[]>,
      savedPosts: [] as PostListItem[],

      homePostsNextCursor: null as string | null,
      spacePostsNextCursor: {} as Record<string, string | null>,
      userPostsNextCursor: {} as Record<string, string | null>,
      savedPostsNextCursor: null as string | null,

      reachedEndHome: false as Boolean,
      reachedEndSpace: {} as Record<string, Boolean>,
      reachedEndUser: {} as Record<string, Boolean>,
      reachedEndSaved: false as Boolean,
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

    setIsLoading(value: boolean) {
      this.isLoading = value;
    },

    async fetchNextPostsHome() {
      if (this.reachedEndHome) {
        return;
      }

      const req = new ApiRequests();
      const response = await req.getPostsFromHome(this.homePostsNextCursor);
      const nextLink: string | null = response.next;

      if (!nextLink) {
        this.reachedEndHome = true;
      } else {
        this.homePostsNextCursor = nextLink.split('cursor=')[1];
      }

      this.homePosts.push(...response.results);
    },

    async fetchNextPostsUser(username: string) {
      if (this.reachedEndUser[username]) {
        return;
      }

      const req = new ApiRequests();
      const response = await req.getPostsFromUser(username, this.userPostsNextCursor[username]);
      const nextLink: string | null = response.next;

      if (!nextLink) {
        this.reachedEndUser[username] = true;
      } else {
        this.userPostsNextCursor[username] = nextLink.split('cursor=')[1];
      }

      if(!this.userPosts[username]) {
        this.userPosts[username] = [];
      }

      this.userPosts[username].push(...response.results);
    },

    async fetchNextPostsSpace(spaceId: string) {
      if (this.reachedEndSpace[spaceId]) {
        return;
      }

      const req = new ApiRequests();
      const response = await req.getPostsFromSpace(spaceId, this.spacePostsNextCursor[spaceId]);
      const nextLink: string | null = response.next;

      if (!nextLink) {
        this.reachedEndSpace[spaceId] = true;
      } else {
        this.spacePostsNextCursor[spaceId] = nextLink.split('cursor=')[1];
      }

      if(!this.spacePosts[spaceId]) {
        this.spacePosts[spaceId] = [];
      }

      this.spacePosts[spaceId].push(...response.results);
    },

    async fetchNextPostsSaved() {
      if (this.reachedEndSaved) {
        return;
      }

      const req = new ApiRequests();
      const response = await req.getPostsFromSaved(this.savedPostsNextCursor);
      const nextLink: string | null = response.next;

      if (!nextLink) {
        this.reachedEndSaved = true;
      } else {
        this.savedPostsNextCursor = nextLink.split('cursor=')[1];
      }

      this.savedPosts.push(...response.results);
    },

    async createPost(content: string, spaceId: string | null) {
      const req = new ApiRequests();
      const post = await req.createPost(content, spaceId);

      this.homePosts.unshift(post);
      console.log("add post to homePosts: ", post);

      if(spaceId && this.spacePosts[spaceId]) {
        this.spacePosts[spaceId].unshift(post);
      }

      if(this.userPosts[post.user.username]) {
        this.userPosts[post.user.username].unshift(post);
      }
    },

    async deletePost(post: PostListItem) {
      const req = new ApiRequests();
      await req.deletePost(post.id);

      this.homePosts = this.homePosts.filter(p => p.id !== post.id);

      this.savedPosts = this.savedPosts.filter(p => p.id !== post.id);

      if(post.space && this.spacePosts[post.space]) {
        this.spacePosts[post.space] = this.spacePosts[post.space].filter(p => p.id !== post.id);
      }

      if(this.userPosts[post.user.username]) {
        this.userPosts[post.user.username] = this.userPosts[post.user.username].filter(p => p.id !== post.id);
      }
    },

    async _upvote(postId: string) {
      const req = new ApiRequests();
      await req.upvote(postId);
    },

    async _downvote(postId: string) {
      const req = new ApiRequests();
      await req.downvote(postId);
    },

    async _unvote(postId: string) {
      const req = new ApiRequests();
      await req.unvote(postId);
    },

    async _toggleUpvote(post: PostListItem, request = false){
      post.votes_and_comments.has_upvoted = !post.votes_and_comments.has_upvoted;

      if (post.votes_and_comments.has_upvoted) {
        post.votes_and_comments.votes += 1;
        if(request) {
          await this._upvote(post.id);
        }
      } else {
        post.votes_and_comments.votes -= 1;
        if(request) {
          await this._unvote(post.id);
        }
      }

      if (post.votes_and_comments.has_downvoted) {
        post.votes_and_comments.votes += 1;
      }

      post.votes_and_comments.has_downvoted = false;
    },

    async _toggleDownvote(post: PostListItem, request = false){
      post.votes_and_comments.has_downvoted = !post.votes_and_comments.has_downvoted;

      if (post.votes_and_comments.has_downvoted) {
        post.votes_and_comments.votes -= 1;
        if(request){
          await this._downvote(post.id);
        }
      } else {
        post.votes_and_comments.votes += 1;
        if(request){
          await this._unvote(post.id);
        }
      }

      if (post.votes_and_comments.has_upvoted) {
        post.votes_and_comments.votes -= 1;
      }

      post.votes_and_comments.has_upvoted = false;
    },

    async toggleUpvote(_post: PostListItem) {
      let post: PostListItem | undefined;

      await this._toggleUpvote(_post, true);

      post = this.homePosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleUpvote(post);
      }

      post = this.savedPosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleUpvote(post);
      }

      post = this.spacePosts[_post?.space]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleUpvote(post);
      }

      post = this.userPosts[_post.user.username]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleUpvote(post);
      }
    },

    async toggleDownvote(_post: PostListItem) {
      let post: PostListItem | undefined;

      await this._toggleDownvote(_post, true);

      post = this.homePosts.find(post => post.id === _post.id);
      if(post && post !== _post){
        await this._toggleDownvote(post);
      }

      post = this.savedPosts.find(post => post.id === _post.id);
      if(post && post !== _post){
        await this._toggleDownvote(post);
      }

      post = this.spacePosts[_post?.space]?.find(post => post.id === _post.id);
      if(post && post !== _post){
        await this._toggleDownvote(post);
      }

      post = this.userPosts[_post?.user.username]?.find(post => post.id === _post.id);
      if(post && post !== _post){
        await this._toggleDownvote(post);
      }
    },

    async _toggleSave(post: PostListItem, request = false) {
      post.is_saved = !post.is_saved;
        if (post.is_saved) {
          if(request){
            await (new ApiRequests()).savePost(post.id);
          }
        } else {
          if(request){
            await (new ApiRequests()).unsavePost(post.id);
          }
        }
    },

    async toggleSave(_post: PostListItem) {
      let post: PostListItem;

      await this._toggleSave(_post, true);

      post = this.homePosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleSave(post);
      }

      post = this.savedPosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleSave(post);
      }

      post = this.spacePosts[_post?.space]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleSave(post);
      }

      post = this.userPosts[_post.user.username]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        await this._toggleSave(post);
      }

    },

    _updateCommentCount(_post: PostListItem, count: number) {
      let post: PostListItem;

      if(!_post){
        return;
      }

      post = _post;
      post.votes_and_comments.comments = count;

      post = this.homePosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        post.votes_and_comments.comments = count;
      }

      post = this.savedPosts.find(p => p.id === _post.id);
      if(post && post !== _post){
        post.votes_and_comments.comments = count;
      }

      post = this.spacePosts[_post?.space]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        post.votes_and_comments.comments = count;
      }

      post = this.userPosts[_post.user.username]?.find(p => p.id === _post.id);
      if(post && post !== _post){
        post.votes_and_comments.comments = count;
      }
    },

    increaseCommentCount(post: PostListItem) {
      this._updateCommentCount(post, post.votes_and_comments.comments + 1);
    },

    decreaseCommentCount(post: PostListItem) {
      this._updateCommentCount(post, post.votes_and_comments.comments - 1);
    },

    async fetchPost(postId: string): Promise<PostListItem> {
      const post = this.postList.find(post => post.id === postId);
      if(post) {
        return post;
      } else {
        const req = new ApiRequests();
        return await req.getPost(postId);
      }
    },

    deleteAllPostsOfSpace(spaceId: string) {
      this.homePosts = this.homePosts.filter(post => post.space != spaceId);
      this.savedPosts = this.savedPosts.filter(post => post.space != spaceId);
      this.userPosts = Object.keys(this.userPosts).reduce((acc, key) => {
        acc[key] = this.userPosts[key].filter(post => post.space != spaceId);
        return acc;
      }, {} as Record<string, PostListItem[]>);
      delete this.spacePosts[spaceId];
    }

  },
})
