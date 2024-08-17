import requests
page_access_token = 'EAARBnlYN4xMBOZBS2gSnY0fMIBqaWFAQP2L4BpPBQxARZBEIlHudVhcGHh3vVCFAbzsdpgFSAEJljDeoE42cqQ5ZBzgjohZA5WWMBizCq2JHJjIXux0hkfd8TSCMOvz9lC0DZBtRZAMbgZBwoizdwPlo1JyFAHZAhMeArnRog8QBPClcX7eWfZARfU5BWDUsJUKwMfi7aiPZCaql4qdCk2oBpXfz5f'
page_id = '435371066315430'
image_path = 'C:/Users/raush/Desktop/Automate_algo/social_media/download.jpeg'
message = "This is a test post with an image on my Facebook Page using the Meta API"
upload_url = f"https://graph.facebook.com/v20.0/{page_id}/photos"
with open(image_path, 'rb') as image_file:
    upload_payload = {
        'caption': message,
        'access_token': page_access_token
    }
    files = {
        'source': image_file
    }
    upload_response = requests.post(upload_url, data=upload_payload, files=files)

if upload_response.status_code == 200:
    print("Image successfully uploaded and post created on your Facebook Page!")
else:
    print("Failed to upload the image or create the post:", upload_response.json())
