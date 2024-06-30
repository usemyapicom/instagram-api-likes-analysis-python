from typing import List


class PostData:
    def __init__(self, post_id, post_likers: List[str], followers: List[str]):
        self.post_id = post_id
        self.post_likers = post_likers
        self.followers = followers