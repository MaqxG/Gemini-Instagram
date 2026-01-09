

class InstagramPoster:
    def __init__(self, access_token: str, account_id: str):
        """
        Initialize the InstagramPoster with credentials.
        
        Args:
            access_token (str): Valid Instagram Graph API Access Token.
            account_id (str): Instagram Business Account ID.
        """
        print("TestInstagramPoster.__init__ called:")
        print("\taccess_token: " + access_token)
        print("\taccount_id: " + account_id)

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

        print("TestInstagramPoster.post_image called:")
        print("\timage_url: " + image_url)
        print("\tcaption: " + caption)
        print("\treturn: POSTID_2003")
        
        return "POSTID_2003"
