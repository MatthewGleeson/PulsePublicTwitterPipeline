# PulseTwitterPipeline

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social)

This is a repo of useful pipeline scripts I used to setup the preliminary real-time twitter pipeline for Pulse/Dirichlet.

Includes scripts written for Twitter v1 and v2 APIs which can work with AWS Kinesis Firehose to pump real-time twitter data into S3 buckets, whose 'put' action triggers a Lambda function to do basic sentiment analysis on the data as it goes in. That gets sent to an ElasticSearch instance that you can use to build visualizations like maps, bar graphs, and pie charts. Some examples here:


TODO: Complete README using https://github.com/scottydocs/README-template.md/blob/master/README.md as guide
