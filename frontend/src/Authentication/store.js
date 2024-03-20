import {reactive, ref} from "vue";

const state_ref = ref(false);

export function get_current_auth_state() {
  if (state_ref.value === false) {
    state_ref.value = sessionStorage.getItem("token") !== undefined;
  }
  return state_ref;
}

export function set_current_auth_state(state) {
  sessionStorage.setItem("authenticated", state);
  state_ref.value = state;
}

export const state = reactive({
  authenticated: get_current_auth_state(),
});
