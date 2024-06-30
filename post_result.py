class PostResult:
    def __init__(self, post_id, all_likes_count, likers_likes_count):
        self.all_likes_count = all_likes_count
        self.likers_likes_count = likers_likes_count
        self.post_id = post_id