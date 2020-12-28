
import threading
import sys
import json
import subprocess
from instaloader import Instaloader, Profile
from itertools import islice
import pickle

loader = Instaloader()

# Get num followers of a specific user
def get_user_followers(username, num):
    profile = Profile.from_username(loader.context, username)
    users = []
    count = 0

    followers = islice(profile.get_followees(), num)

    # Add usernames to array
    for profile in followers:
        if profile.username not in users:
            users.append(profile.username)
            count += 1
            if count == num:
                break

    return users

if __name__ == "__main__":
    # Check if all required parameters were given
    try: 
        username = sys.argv[1]
    except IndexError:
        print('Missing Argument. Correct Usage: python user.py <username> <number-of-followers[optional, default=100]>')
        sys.exit(1)

    try: 
        num = int(sys.argv[2])
    except IndexError:
        num = 100

    # Read config
    with open("config.json") as infile:
        data = json.load(infile)
        instaUser = data["InstaUser"]
        instaPwd = data["InstaPassword"]

    # Login User
    loader.login(instaUser, instaPwd)

    # Get all users
    users = get_user_followers(username, num)

    # Save users to file
    with open("users.json", "w") as outfile: 
        json.dump(users, outfile)

    # Call node subprocess to message users
    subprocess.call("node messageUsers.ts")