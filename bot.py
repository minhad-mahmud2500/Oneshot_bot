import praw
import re
regex = re.compile(r"(one ?shot)|(ch(apter)? ?0*1)\b", re.IGNORECASE)
r = praw.Reddit("bot1")
selftext = ""
for post in r.subreddit("manga").new(limit=None):
    if not post.title.startswith("["): continue
    if regex.search(post.title):
        with open("manga.txt","a") as f:
            selftext += f"[{post.title}]({post.url})\n\n"

if selftext != "":
    r.subreddit("oneshot_daily").submit("Oneshots/First Chapters",selftext=selftext)    
'''
import praw
reddit = praw.Reddit('bot1')
subreddit =reddit.subreddit("manga")
for submission in subreddit.new(limit=500):
              
        if "Oneshot" in submission.title:
            print(submission.title)
            print(submission.url)
        elif "One Piece" in submission.title:
            print(submission.title)
            print(submission.url)
