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
