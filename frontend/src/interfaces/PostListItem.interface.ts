export interface PostListItem {
  id: string
  user: {
    id: string
    username: string
    display_name: string
    about: string
    image_url: string
  }
  votes_and_comments: {
    votes: number
    comments: number
    has_upvoted: boolean
    has_downvoted: boolean
  }
  created_at: string
  content: string
  space: string
  is_saved: boolean
}
