const BASE_URL = import.meta.env.VITE_API_URL;

const routes = {
  authentication: {
    register_options: `${BASE_URL}/passkey-options/register/`,
    register: `${BASE_URL}/register/`,
    login_options: `${BASE_URL}/passkey-options/login/`,
    login: `${BASE_URL}/login/`,
    username_availability: `${BASE_URL}/validity/username/`,
    email_availability: `${BASE_URL}/validity/email/`,
  }
}

export default routes;
