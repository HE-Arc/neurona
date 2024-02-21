import {reactive} from "vue";

export function get_current_auth_state(){
  return localStorage.getItem("authenticated") === "true";
}

export function set_current_auth_state(state){
  localStorage.setItem("authenticated", state);
}

export const state = reactive({
  authenticated: get_current_auth_state(),
});
