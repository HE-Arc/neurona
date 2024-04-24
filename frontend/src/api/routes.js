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
    get: (id) => `${BASE_URL}/posts/${id}/`,
    show: `${BASE_URL}/posts/`,
    delete: (id) => `${BASE_URL}/posts/${id}/`,
    upvote: (id) => `${BASE_URL}/posts/${id}/upvote/`,
    downvote: (id) => `${BASE_URL}/posts/${id}/downvote/`,
    unvote: (id) => `${BASE_URL}/posts/${id}/unvote/`,
    user: (username) => `${BASE_URL}/posts/user/${username}/`,
    comments: (id) => `${BASE_URL}/posts/${id}/comments/`,
    save: (id) => `${BASE_URL}/posts/${id}/save/`,
    get_saved: `${BASE_URL}/posts/saved/`,
  },
  profile: {
    show: `${BASE_URL}/profile/`,
    edit: (attribute) => `${BASE_URL}/profile/${attribute}/`,
    delete: `${BASE_URL}/profile/`,
    showFromUsername: (username) => `${BASE_URL}/profile/${username}/`,
  },
  comments: {
    delete: (id) => `${BASE_URL}/comments/${id}/`,
    upvote: (id) => `${BASE_URL}/comments/${id}/upvote/`,
    downvote: (id) => `${BASE_URL}/comments/${id}/downvote/`,
    unvote: (id) => `${BASE_URL}/comments/${id}/unvote/`,
  }
}

export default routes;
