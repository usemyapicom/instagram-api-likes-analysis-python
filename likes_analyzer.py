from typing import List

from post_data import PostData
from post_result import PostResult


from typing import List

class LikesAnalyzer:
    def __init__(self, posts_data: List[PostData]):
        """
        Initialize the LikesAnalyzer with a list of PostData objects.
        
        :param posts_data: List of PostData objects containing data for each post.
        """
        self.posts_data = posts_data
    
    def get_analysis(self) -> List[PostResult]:
        """
        Analyze the likes data to determine the total likes and the likes from followers for each post.
        
        :return: A list of PostResult objects containing the analysis results for each post.
        """
        results: List[PostResult] = []  # Initialize an empty list to store the analysis results

        # Iterate through each PostData object in the posts_data list
        for p in self.posts_data:
            all_likes_count = len(p.post_likers)  # Count the total number of likes for the post
            likers_likes_count = 0  # Initialize the count for likes from followers
            
            # Iterate through each liker of the post
            for liker in p.post_likers:
                # Check if the liker is also a follower
                if liker in p.followers:
                    likers_likes_count += 1  # Increment the count if the liker is a follower
            
            # Create a PostResult object with the post ID, total likes, and likes from followers
            results.append(PostResult(p.post_id, all_likes_count, likers_likes_count))

        return results  # Return the list of PostResult objects
