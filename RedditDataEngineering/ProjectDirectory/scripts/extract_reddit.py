import praw
import pandas as pd
import json
import os

def extract_reddit_data():
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
    with open(config_path) as f:
        config = json.load(f)
    reddit = praw.Reddit(
        client_id=config['reddit_client_id'],
        client_secret=config['reddit_client_secret'],
        user_agent=config['reddit_user_agent']
    )
    posts = []
    for submission in reddit.subreddit('python').hot(limit=100):
        posts.append({
            'id': submission.id,
            'title': submission.title,
            'score': submission.score,
            'created': submission.created_utc
        })
    df = pd.DataFrame(posts)
    output_path = os.path.join(os.path.dirname(__file__), '../data/reddit_posts.csv')
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    extract_reddit_data() 