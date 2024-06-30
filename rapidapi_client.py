import http
import os
import pickle
from typing import Any, Optional
import requests

from config import RAPIDAPI_HOST, RAPIDAPI_KEY

class RapidApiClient:

    def __init__(self, cache_dir: str = 'cache'):
        self.headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST
        }
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            
    def get_user_posts(self, userid, count, end_cursor = None):
        url = self.__get_api_url(f"/userposts/{userid}/{count}/{self.__get_end_cursor(end_cursor)}")
        return self.__get_or_set_cache("userposts", userid, count, end_cursor, url)
     
    def get_post_likes(self, shortcode, count, end_cursor = None):
        url = self.__get_api_url(f"/postlikes/{shortcode}/{count}/{self.__get_end_cursor(end_cursor)}")
        return self.__get_or_set_cache("postlikes", shortcode, count, end_cursor, url)

    def get_user_followers(self, userid, count, end_cursor = None):
        url = self.__get_api_url(f"/userfollowers/{userid}/{count}/{self.__get_end_cursor(end_cursor)}")
        return self.__get_or_set_cache("userfollowers", userid, count, end_cursor, url)
   
    def __get_api_url(self, path_and_query):
        return f"https://{RAPIDAPI_HOST}{path_and_query}"
    
    def __get_end_cursor(self, ec):
        if ec == None:
            return "%7Bend_cursor%7D"
        return ec

    def __get_cache_file_path(self, endpoint: str, identifier: str, count: int, end_cursor: Optional[str]) -> str:
        """
        Generate a file path for caching based on the endpoint, identifier, count, and end_cursor.
        """
        filename = f"{endpoint}_{identifier}_{count}_{self.__get_end_cursor(end_cursor)}.pkl"
        return os.path.join(self.cache_dir, filename)

    def __get_or_set_cache(self, endpoint: str, identifier: str, count: int, end_cursor: Optional[str], url: str) -> Any:
        """
        Retrieve data from the cache if it exists; otherwise, fetch data from the URL, cache it, and return the data.

        :param endpoint: The API endpoint being queried.
        :param identifier: The identifier for the request (e.g., user ID or post shortcode).
        :param count: The number of items requested.
        :param end_cursor: The pagination cursor for the request.
        :param url: The URL to fetch data from if not cached.
        :return: The data retrieved from the cache or fetched from the URL.
        """
        cache_file_path = self.__get_cache_file_path(endpoint, identifier, count, end_cursor)
        
        # Check if the cache file exists
        if os.path.exists(cache_file_path):
            # Load and return data from cache
            with open(cache_file_path, 'rb') as cache_file:
                return pickle.load(cache_file)

        # Make the API request if cache does not exist
        response = requests.get(url, headers=self.headers)
        data = response.json()

        # Save the fetched data to the cache
        with open(cache_file_path, 'wb') as cache_file:
            pickle.dump(data, cache_file)

        return data