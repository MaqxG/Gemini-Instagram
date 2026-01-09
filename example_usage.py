from test_instagram_poster import InstagramPoster

def main():
    # REPLACE THESE WITH YOUR ACTUAL VALUES
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"
    ACCOUNT_ID = "YOUR_INSTAGRAM_ACCOUNT_ID_HERE"
    
    # Must be a publicly accessible URL (e.g., hosted on a server, S3, or a testing service like ngrok)
    IMAGE_URL = "https://images.unsplash.com/photo-1517849845537-4d257902454a" 
    CAPTION = "Hello World! This is a test post from my Python script. 🐍📸 #python #coding #instagramapi"

    try:
        print("Initializing Instagram Poster...")
        poster = InstagramPoster(ACCESS_TOKEN, ACCOUNT_ID)
        
        print(f"Attempting to post image: {IMAGE_URL}")
        post_id = poster.post_image(IMAGE_URL, CAPTION)
        
        print(f"Success! Post published with ID: {post_id}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
