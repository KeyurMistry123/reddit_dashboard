import boto3
import os
import json

def upload_to_s3():
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
    with open(config_path) as f:
        config = json.load(f)
    s3 = boto3.client('s3')
    file_path = os.path.join(os.path.dirname(__file__), '../data/reddit_posts.csv')
    s3.upload_file(file_path, config['s3_bucket'], 'reddit_posts.csv')

if __name__ == "__main__":
    upload_to_s3() 