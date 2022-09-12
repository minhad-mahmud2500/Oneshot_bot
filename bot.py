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
            