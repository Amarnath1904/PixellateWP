import os
import auth
import WP_request_handel
import json
import time
import urllib.parse
import ImageCreation

Authorization, Web_URL = auth.authorization()
NUM_OF_PAGE = 8
count = 0
all_posts = []  # Initialize an empty list to collect posts

for i in range(1, NUM_OF_PAGE):
    result = WP_request_handel.posts_without_featured_image(Web_URL, Authorization, i)

    dump_json = json.dumps(result)
    result_json = json.loads(dump_json)

    for post in result_json:
        print("id = ", post['id'], "title = ", post['title']["rendered"], "post = ", post['featured_media'])

        if post['featured_media'] == 0:
            count += 1
            print("How many posts updated ", count)
            all_posts.append(post)

            # Handle special characters in titles for image creation
            title = post['title']['rendered']

            title = title.replace("&#8211;", "-")  # Replace "-" with ","
            title = title.replace("&#038;", "and")  # Replace "&" with "and"
            title = title.replace("&#8230;", "...")  # Remove "?" from the title
            title = title.replace("&#8217;s", "'s")
            title = title.replace("&#8217;t", "'t")


            # Update the title in the post dictionary (if needed for further processing)
            post['title']['rendered'] = title

            # image creation
            IMG_DIR = ImageCreation.image_creation(str(title))

            # Image upload
            image_upload_response = WP_request_handel.upload_image(IMG_DIR, Web_URL, Authorization)
            dump_json = json.dumps(image_upload_response, indent=4)
            image_upload_response_result_json = json.loads(dump_json)

            # Image update per post
            image_id = image_upload_response_result_json["id"]
            post_id = post['id']

            end_result = WP_request_handel.update_post_with_featured_image(post_id, image_id, Web_URL, Authorization)

            dump_json = json.dumps(end_result, indent=4)
            end_result_json = json.loads(dump_json)

            os.remove(IMG_DIR)  # Remove the image after uploading

            print(end_result_json)

    print(count)
    print(i, "page done -------- !!")

# After collecting all posts, write them to the file as a JSON array.
with open("JASON Response/data.json", "w") as outfile:  # Corrected the folder name from "JASON Response" to "JSON Response"
    json.dump(all_posts, outfile, indent=4)
