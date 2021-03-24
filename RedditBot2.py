import praw

reddit = praw.Reddit(
    client_id="Insert here",
    client_secret="insert here",
    user_agent="<console:Secret>",
)

redditname = ["frugal", "musictheory"]
for tide in redditname:
    subreddit = reddit.subreddit(tide)
    for post in subreddit.rising(limit=3):
        s = "*" * 20
        print(s)
        print(post.title)
        print(post.url)

