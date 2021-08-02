# https://aws.amazon.com/blogs/compute/upcoming-changes-to-the-python-sdk-in-aws-lambda/
import urllib3
import json
import boto3

http = urllib3.PoolManager()
url = 'https://jsonplaceholder.typicode.com/posts'

# Connect to AWS Simple Notification Service
sns_client = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:112757862110:test-topic'

def lambda_handler(event, context):
    response = http.request("GET", url)

    posts = json.loads(response.data) #load data into a dict of objects, posts

    # Let's get the unique userId, there should only be 1-10
    unique_titles = [] #set()
    for post in posts:
        if post['title'] not in unique_titles:
            unique_titles.append(post['title']) # unique_ids.add(post['userId'])

    # Publish a message.
    sns_client.publish(
        Message=f'Posts\' Titles: {unique_titles}',
        TopicArn=topic_arn
    )

    return {'titles': unique_titles }