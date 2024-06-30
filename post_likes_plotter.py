import matplotlib.pyplot as plt
from typing import List
import random

from post_result import PostResult

# Constants for the bar chart
BAR_WIDTH = 0.5  # Width of the bars in the chart
ALL_LIKES_COLOR = 'blue'  # Color of the bars representing all likes
LIKERS_LIKES_COLOR = 'green'  # Color of the bars representing likes from followers

class PostLikesPlotter:
    
    def plot_analysis(self, results: List[PostResult]) -> None:
        """
        Plot the analysis of post likes, showing total likes and likes from followers for each post.

        :param results: A list of PostResult objects containing analysis results for each post.
        """
        # Extract post IDs, total likes counts, and likers likes counts from the results
        post_ids = [result.post_id for result in results]
        all_likes_counts = [result.all_likes_count for result in results]
        likers_likes_counts = [result.likers_likes_count for result in results]

        # Example of generating random numbers for testing purposes
        random_numbers = random.sample(range(10, 31), 5)
        likers_likes_counts = [result for result in random_numbers]

        # Create a figure and axis for the bar chart
        fig, ax = plt.subplots()

        # Plot the bars for total likes
        bars = ax.bar(post_ids, all_likes_counts, BAR_WIDTH, color=ALL_LIKES_COLOR, label='All Likes')

        # Plot the bars for likes from followers, overlaying them on the total likes bars
        for i, (bar, all_likes, liker_likes) in enumerate(zip(bars, all_likes_counts, likers_likes_counts)):
            ax.bar(bar.get_x(), liker_likes, BAR_WIDTH, color=LIKERS_LIKES_COLOR, label='Likers Likes' if i == 0 else "")

        # Set the labels and title of the chart
        ax.set_xlabel('Post ID')
        ax.set_ylabel('Likes Count')
        ax.set_title('Likes Analysis per Post')
        
        # Move the legend outside the bar chart area
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        # Adjust the appearance of the x-axis labels
        ax.set_xticklabels(post_ids, fontsize=8, rotation=45, ha='right')

        # Display the bar chart
        plt.show()
