import requests
import json

class InstagramPoster:
    def __init__(self, access_token: str, account_id: str):
        """
        Initialize the InstagramPoster with credentials.
        
        Args:
            access_token (str): Valid Instagram Graph API Access Token.
            account_id (str): Instagram Business Account ID.
        """
        self.access_token = access_token
        self.account_id = account_id
        self.base_url = "https://graph.facebook.com/v18.0"

    def post_image(self, image_url: str, caption: str = "") -> str:
        """
        Post an image to the Instagram account.
        
        Args:
            image_url (str): The public URL of the image to post.
            caption (str): The caption for the post.
            
        Returns:
            str: The ID of the published post/media.

        Raises:
            Exception: If the API call fails at any step.
        """
        # Step 1: Create Media Object Container
        container_id = self._create_media_container(image_url, caption)
        
        # Step 2: Publish Media Container
        post_id = self._publish_media_container(container_id)
        
        return post_id

    def _create_media_container(self, image_url: str, caption: str) -> str:
        """
        Helper method to create the media container.
        """
        url = f"{self.base_url}/{self.account_id}/media"
        payload = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }
        
        response = requests.post(url, data=payload)
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise Exception(f"Failed to decode API response. Status Code: {response.status_code}")

        if response.status_code != 200 or "id" not in data:
            error_msg = data.get("error", {}).get("message", "Unknown error")
            raise Exception(f"Error creating media container: {error_msg}")
            
        return data["id"]

    def _publish_media_container(self, creation_id: str) -> str:
        """
        Helper method to publish the media container.
        """
        url = f"{self.base_url}/{self.account_id}/media_publish"
        payload = {
            "creation_id": creation_id,
            "access_token": self.access_token
        }
        
        response = requests.post(url, data=payload)
        
        try:
            data = response.json()
        except json.JSONDecodeError:
            raise Exception(f"Failed to decode API response. Status Code: {response.status_code}")

        if response.status_code != 200 or "id" not in data:
            error_msg = data.get("error", {}).get("message", "Unknown error")
            raise Exception(f"Error publishing media: {error_msg}")
            
        return data["id"]
