
import threading
import sys
import json
import subprocess
from instaloader import Instaloader, Profile
import pickle

loader = Instaloader()
def get_hashtags_posts(query, num):
    posts = loader.get_hashtag_posts(query)
    users = []
    count = 0
    for post in posts:
        profile = post.owner_profile
        if profile.username not in users:
            users.append(profile.username)
            count += 1
            if count == num:
                break
    return users

if __name__ == "__main__":
    try: 
        hashtag = sys.argv[1]
    except IndexError:
        print('Missing Argument. Correct Usage: python hastags.py "<message>" <your-hashtag> <number-of-posts[optional, default=10]>')
        sys.exit(1)

    try: 
        num = int(sys.argv[2])
    except IndexError:
        num = 10
    # users = get_hashtags_posts(hashtag, num)
    users = ["botta_modus"]

    with open("users.json", "w") as outfile: 
        json.dump(users, outfile)

    subprocess.call("node messageUsers.ts")