import axios from "axios";
import routes from "@/api/routes";
import MessageManager from "@/tools/MessageManager";
import store from "@/Authentication/store";

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
        if (e.response.status >= 400 && e.response.status < 500) {
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

  async updateProfile(attribute, value) {
    return await this.#put(routes.profile.edit(attribute), {[attribute]: value});
  }
}

export default ApiRequests;
