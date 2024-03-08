// src/services/ApiService.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/',
  withCredentials: false,
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
});

export default {
  getPosts() {
    return apiClient.get('/posts');
  },
  createPost(postData) {
    return apiClient.post('/posts', postData);
  },
  upvotePost(postId) {
    return apiClient.post(`/posts/${postId}/upvote`); // Assuming your backend is set up to handle this route
  },
  downvotePost(postId) {
    return apiClient.post(`/posts/${postId}/downvote`); // Assuming your backend is set up to handle this route
  },
  addComment(postId, commentData) {
    return apiClient.post(`/posts/${postId}/comments`, commentData);
  },
};
