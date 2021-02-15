# Folder containing basic textblob sentiment analysis functions, passes data via Boto3 SDK to ElasticSearch. Can be added to AWS Lambda layers where a 'put' trigger has been set on an S3 bucket
# Also keeps track of emojis in tweets
# TODO: replace w/ huggingface transformer-based model and upload to S3



# To avoid package versioning issues/OS incompatabilities, I recommend spinning up a basic EC2 instance and zipping lambda functions+dependencies there.
# I used the basic "Amazon Linux 2 AMI (HVM), SSD Volume Type" AWS EC2 AMI

# credits to Assaf Mentzer(https://github.com/AssafMentzer) & Zhong Hongsheng(https://github.com/joking-clock) whose (open-source) code this is partially derived from