
import threading
import sys
import json
import subprocess
from instaloader import Instaloader, Profile
import pickle

loader = Instaloader()

# Get num users which posted under specific hashtag
def get_hashtags_posts(query, num):
    posts = loader.get_hashtag_posts(query)
    users = []
    count = 0

    # Add usernames to array
    for post in posts:
        profile = post.owner_profile
        if profile.username not in users:
            users.append(profile.username)
            count += 1
            if count == num:
                break
    return users

if __name__ == "__main__":
    # Check if all required parameters were given
    try: 
        hashtag = sys.argv[1]
    except IndexError:
        print('Missing Argument. Correct Usage: python hastags.py "<message>" <your-hashtag> <number-of-posts[optional, default=10]>')
        sys.exit(1)

    try: 
        num = int(sys.argv[2])
    except IndexError:
        num = 10

    # Get all users for specific hashtag
    users = get_hashtags_posts(hashtag, num)

    # Save users to file
    with open("users.json", "w") as outfile: 
        json.dump(users, outfile)

    # Call node subprocess to message users
    subprocess.call("node messageUsersByHashtag.ts")