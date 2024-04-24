import axios from "axios";
import routes from "@/api/routes";
import MessageManager from "@/tools/MessageManager";
import store from "@/Authentication/store";
import router from "@/router";

class ApiRequests {

  constructor() {
    this.messages = MessageManager.getInstance();
  }

  #getToken() {
    return store.state.token;
  }

  #getConfig(auth = true) {
    if (!auth) {
      return {};
    }
    return {
      headers: {
        'Authorization': this.#getToken(),
      }
    }
  }

  async #request(url, method, data = {}, auth = true) {
    try {
      let response;
      const config = this.#getConfig(auth);
      switch (method) {
        case 'get':
          response = await axios.get(url, config);
          break;
        case 'post':
          response = await axios.post(url, data, config);
          break;
        case 'put':
          response = await axios.put(url, data, config);
          break;
        case 'delete':
          response = await axios.delete(url, config);
          break;
      }
      return response.data;
    } catch (e) {
      try {
        if (e.response.status === 403 || e.response.status === 401) {
          this.messages.add('warning', 'Please log in to access this page.');
          store.commit('logout');
          await router.push({name: "login"});
        }
        else if (e.response.status >= 400 && e.response.status < 500) {
          this.messages.add('warning', e.response.data.message);
        } else {
          this.messages.add('error', 'An unexpected error occurred while trying to contact the API server');
        }
      } catch (e) {
        this.messages.add('error', 'An unexpected error occurred while trying to contact the API server. It may be offline. ' +
          'Please try again later or contact the administrator if the problem persists.');
      }
    }
    throw new Error('An error occurred while trying to contact the API server');
  }

  async #get(url = {}, auth = true) {
    return await this.#request(url, 'get', {}, auth);
  }

  async #post(url, data = {}, auth = true) {
    return await this.#request(url, 'post', data, auth);
  }

  async #put(url, data = {}, auth = true) {
    return await this.#request(url, 'put', data, auth);
  }

  async #delete(url, auth = true) {
    return await this.#request(url, 'delete', {}, auth);
  }

  async getProfile() {
    return await this.#get(routes.profile.show);
  }

  async getProfileFromUsername(username){
    return await this.#get(routes.profile.showFromUsername(username));
  }

  async updateProfile(attribute, value) {
    return await this.#put(routes.profile.edit(attribute), {[attribute]: value});
  }

  async logout(){
    return await this.#post(routes.authentication.logout);
  }

  async deleteAccount(){
    return await this.#delete(routes.profile.delete);
  }

  async getPosts() {
    return await this.#get(routes.posts.show);
  }

  async getPost(postId) {
    return await this.#get(routes.posts.get(postId));
  }

  async deletePost(postId) {
    return await this.#delete(routes.posts.delete(postId));
  }

  async getUserPosts(username) {
    return await this.#get(routes.posts.user(username));
  }

  async createPost(content) {
    return await this.#post(routes.posts.create, {content: content});
  }

  async upvote(postId) {
    return await this.#post(routes.posts.upvote(postId));
  }

  async downvote(postId) {
    return await this.#post(routes.posts.downvote(postId));
  }

  async unvote(postId) {
    return await this.#post(routes.posts.unvote(postId));
  }

  async getComments(postId) {
    return await this.#get(routes.posts.comments(postId));
  }

  async createComment(postId, content) {
    return await this.#post(routes.posts.comments(postId), {content: content});
  }

  async deleteComment(commentId) {
    return await this.#delete(routes.comments.delete(commentId));
  }

  async upvoteComment(commentId) {
    return await this.#post(routes.comments.upvote(commentId));
  }

  async downvoteComment(commentId) {
    return await this.#post(routes.comments.downvote(commentId));
  }

  async unvoteComment(commentId) {
    return await this.#post(routes.comments.unvote(commentId));
  }

  async savePost(postId) {
    return await this.#post(routes.posts.save(postId));
  }

  async unsavePost(postId) {
    return await this.#delete(routes.posts.save(postId));
  }

  async getSavedPosts() {
    return await this.#get(routes.posts.get_saved);
  }

}

export default ApiRequests;
