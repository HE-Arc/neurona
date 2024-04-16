const BASE_URL = import.meta.env.VITE_API_URL;

const routes = {
  authentication: {
    register_options: `${BASE_URL}/passkey-options/register/`,
    register: `${BASE_URL}/register/`,
    login_options: `${BASE_URL}/passkey-options/login/`,
    login: `${BASE_URL}/login/`,
    logout: `${BASE_URL}/logout/`,
    username_availability: `${BASE_URL}/validity/username/`,
    email_availability: `${BASE_URL}/validity/email/`,
  },
  posts: {
    create: `${BASE_URL}/posts/`,
    show: `${BASE_URL}/posts/`,
    upvote: (id) => `${BASE_URL}/posts/${id}/upvote/`,
    downvote: (id) => `${BASE_URL}/posts/${id}/downvote/`,
    unvote: (id) => `${BASE_URL}/posts/${id}/unvote/`,
    user: (username) => `${BASE_URL}/posts/user/${username}/`,
  },
  profile: {
    show: `${BASE_URL}/profile/`,
    edit: (attribute) => `${BASE_URL}/profile/${attribute}/`,
    delete: `${BASE_URL}/profile/`,
  }
}

export default routes;
