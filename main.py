import sys
from typing import List
from likes_analyzer import LikesAnalyzer
from post_data import PostData
from post_likes_plotter import PostLikesPlotter
from rapidapi_client import RapidApiClient

api_client = RapidApiClient()
end_cursor = None

# Replace with your actual Instagram account ID
ACCOUNT_ID = '__PASTE_ACCOUNT_ID__'

# Retrieve followers for the account (maximum 50 followers for testing purposes)
followers = api_client.get_user_followers(ACCOUNT_ID, 50)
# Extract usernames of the followers
followers_usernames = [user['username'] for user in followers["data"]["user"]]

# Initialize an empty list to store post data
posts_data: List[PostData] = []
PAGE_LIMIT = 1  # Limit the number of pages to retrieve for testing purposes

for i in range(PAGE_LIMIT):
    # Retrieve user posts (maximum 5 posts per page for testing purposes)
    posts = api_client.get_user_posts(ACCOUNT_ID, 5, end_cursor)
    
    # Check if there is no next page, break the loop if not
    if not posts["data"]["next_page"]:
        break
    
    data = posts["data"]
    end_cursor = data["end_cursor"]  # Update the end_cursor for the next page
    edges = data["edges"]  # Extract the posts data

    for edge in edges:
        node = edge["node"]
        post_id = node["id"]  # Extract the post ID
        
        # Retrieve likes for the post (maximum 50 likes for testing purposes)
        post_likes = api_client.get_post_likes(node["shortcode"], 50)
        # Extract usernames of the users who liked the post
        post_likers = [like['username'] for like in post_likes["data"]["likes"]]
        
        # Create a PostData object and add it to the posts_data list
        posts_data.append(PostData(post_id, post_likers, followers_usernames))


analyzer = LikesAnalyzer(posts_data)
results = analyzer.get_analysis()

plotter = PostLikesPlotter()
plotter.plot_analysis(results)
