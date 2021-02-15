# PulseTwitterPipeline

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub issues](https://img.shields.io/github/issues/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub license](https://img.shields.io/github/license/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub stars](https://img.shields.io/github/stars/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub forks](https://img.shields.io/github/forks/MatthewGleeson/PulsePublicTwitterPipeline)

Python functions used to setup the preliminary real-time twitter pipeline for Pulse/Dirichlet.

Includes code written for Twitter v1 and v2 APIs which can work with AWS Kinesis Firehose to pump real-time twitter data into S3 buckets, whose 'put' action triggers a Lambda function to do basic sentiment analysis on the data as it goes in. That gets sent to an ElasticSearch instance that you can use to build visualizations like maps, bar graphs, and pie charts. Some examples here:

Bar Graph
https://tinyurl.com/got06a48

Map(sparse data)
https://tinyurl.com/h6xejoly


## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a Twitter Developer Account(with API key, API key secret if using API v1 OR Bearer Token if using API v2)
* You have an AWS account with an SDK IAM role
