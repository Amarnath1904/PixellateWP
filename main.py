import os

import auth
import WP_request_handel
import json
import time
import ImageCreation

Authorization, Web_URL = auth.authorization()
NUM_OF_PAGE = 7
count = 0
all_posts = []  # Initialize an empty list to collect posts

for i in range(NUM_OF_PAGE):
    result = WP_request_handel.posts_without_featured_image(Web_URL, Authorization, i+1)

    dump_json = json.dumps(result)
    result_json = json.loads(dump_json)

    for post in result_json:
        print("id = ", post['id'], "title = ", post['title'], "post = ", post['featured_media'])

        if post['featured_media'] == 0:
            count += 1
            all_posts.append(post)

            # image creation
            IMG_DIR = ImageCreation.image_creation(str(post["title"]))

            # Image uplode
            image_upload_response = WP_request_handel.upload_image(IMG_DIR, Web_URL, Authorization)
            dump_json = json.dumps(image_upload_response, indent=4)
            image_upload_response_result_json = json.loads(dump_json)

            # Image update per post

            image_id = image_upload_response_result_json["id"]
            post_id = post['id']

            end_result = WP_request_handel.update_post_with_featured_image(post_id, image_id, Web_URL, Authorization)

            dump_json = json.dumps(end_result, indent=4)
            end_result_json = json.loads(dump_json)

            os.remove(IMG_DIR)

            print(end_result_json)


    print(count)
    print(i, "page done -------- !!")
    time.sleep(10)

# After collecting all posts, write them to the file as a JSON array.
with open("JASON Response/data.json", "w") as outfile:
    json.dump(all_posts, outfile, indent=4)

