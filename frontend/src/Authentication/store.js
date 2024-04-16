import {createStore, useStore} from "vuex";
import createPersistedState from 'vuex-persistedstate';

const store = createStore({
  state() {
    return {
      authenticated: false,
      token: null,
    }
  },
  mutations: {
    logout(state) {
      state.authenticated = false
    },
    login(state) {
      state.authenticated = true
    },
    setToken(state, token) {
      state.token = token
    }
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
      paths: ['authenticated', 'token']
    })
  ]
})

export default store;
