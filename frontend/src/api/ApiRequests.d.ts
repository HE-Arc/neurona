// ApiRequests.d.ts
export default class ApiRequests {
  getPosts(): Promise<any>;
  getPost(postId: string): Promise<any>;
  deletePost(postId: string): Promise<void>;
  getUserPosts(username: string): Promise<any>;
  createPost(content: string): Promise<any>;
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
  uploadImageToImgur(imageFile: File): Promise<string>;

  // Ajoutez d'autres méthodes au besoin
}
