import praw

credentials_config = open("./login.txt","r")

creds = credentials_config.read().splitlines()

reddit = praw.Reddit(client_id=creds[0],
                     client_secret=creds[1],
                     username=creds[2],
                     password=creds[3],
                     user_agent='test /u/charredbot')

print(reddit.user.me())