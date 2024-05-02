// ApiRequests.d.ts
export default class ApiRequests {
  getPosts(): Promise<any>;
  getPost(postId: string): Promise<any>;
  deletePost(postId: string): Promise<void>;
  getUserPosts(username: string): Promise<any>;
  createPost(content: string, spaceId: string | null): Promise<any>;
  upvote(postId: string): Promise<void>;
  downvote(postId: string): Promise<void>;
  unvote(postId: string): Promise<void>;
  getComments(postId: string): Promise<any>;
  createComment(postId: string, content: string): Promise<any>;
  deleteComment(commentId: string): Promise<void>;
  upvoteComment(commentId: string): Promise<void>;
  downvoteComment(commentId: string): Promise<void>;
  unvoteComment(commentId: string): Promise<void>;
  savePost(postId: string): Promise<void>;
  unsavePost(postId: string): Promise<void>;
  getSavedPosts(): Promise<any>;
  getSpaces(): Promise<any>;
  getSpace(spaceId: string): Promise<any>;
  getSpacesJoined(): Promise<any>;
  searchSpaces(query: string): Promise<any>;
  createSpace(name: string, about: string): Promise<any>;
  joinSpace(spaceId: string): Promise<void>;
  quitSpace(spaceId: string): Promise<void>;
  deleteSpace(spaceId: string): Promise<void>;
  getProfile(): Promise<any>;
  updateProfile(attribute: string, value: string): Promise<void>;
  deleteAccount(): Promise<void>;

  getPostsFromSpace(spaceId: string, cursor: string | null ): Promise<any>;
  getPostsFromHome(cursor: string | null): Promise<any>;
  getPostsFromUser(username: string, cursor: string | null): Promise<any>;
  getPostsFromSaved(cursor: string | null): Promise<any>;

  // Ajoutez d'autres méthodes au besoin
}
