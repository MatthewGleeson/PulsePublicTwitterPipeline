# PulseTwitterPipeline

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub issues](https://img.shields.io/github/issues/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub license](https://img.shields.io/github/license/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub stars](https://img.shields.io/github/stars/MatthewGleeson/PulsePublicTwitterPipeline)
![GitHub forks](https://img.shields.io/github/forks/MatthewGleeson/PulsePublicTwitterPipeline)

Python functions used to setup the preliminary real-time twitter pipeline for Pulse/Dirichlet.

Includes code written for Twitter v1 and v2 APIs which can work with AWS Kinesis Firehose to pump real-time twitter data into S3 buckets, whose 'put' action triggers a Lambda function to do basic sentiment analysis on the data as it goes in. That gets sent to an ElasticSearch instance that you can use to build visualizations like maps, bar graphs, and pie charts. Some examples here:

[Bar Graph](https://search-es-twitter-demo-dovg4mzxx2qjbpg4jxfkqc7dka.us-east-1.es.amazonaws.com/_plugin/kibana/app/visualize#/edit/9262bc40-6f16-11eb-897b-53b2a064776a?_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:be0f1370-6ee4-11eb-98ee-1b5f3b805e43,key:_index,negate:!f,params:(query:twitter),type:phrase),query:(match_phrase:(_index:twitter)))),linked:!f,query:(language:kuery,query:vaccine),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(field:sentiments,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:20),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f),labels:(show:!f),legendPosition:right,seriesParams:!((data:(id:'1',label:Count),drawLinesBetweenPoints:!t,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:histogram,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Count),type:value))),title:'Vaccine%20Sentiment',type:histogram))&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&indexPattern=be0f1370-6ee4-11eb-98ee-1b5f3b805e43&type=histogram)

[Map](https://search-es-twitter-demo-dovg4mzxx2qjbpg4jxfkqc7dka.us-east-1.es.amazonaws.com/_plugin/kibana/app/visualize#/create?type=tile_map&indexPattern=be0f1370-6ee4-11eb-98ee-1b5f3b805e43&_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(mapCenter:!(33.02708758002874,-90.087890625),mapZoom:4),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(autoPrecision:!t,field:coordinates.coordinates,isFilteredByCollar:!t,precision:2,useGeocentroid:!t),schema:segment,type:geohash_grid)),params:(addTooltip:!t,colorSchema:'Yellow%20to%20Red',heatClusterSize:1.5,isDesaturated:!t,legendPosition:bottomright,mapCenter:!(0,0),mapType:'Scaled%20Circle%20Markers',mapZoom:2,wms:(enabled:!f,options:(format:image%2Fpng,transparent:!t),selectedTmsLayer:(attribution:'%3Ca%20rel%3D%22noreferrer%20noopener%22%20href%3D%22https:%2F%2Fwww.openstreetmap.org%2Fcopyright%22%3EMap%20data%20%C2%A9%20OpenStreetMap%20contributors%3C%2Fa%3E',id:road_map,maxZoom:10,minZoom:0,origin:elastic_maps_service))),title:'',type:tile_map))) (current dataset has very sparse geospatial data but basic POC)


## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have a Twitter Developer Account(with API key, API key secret if using API v1 OR Bearer Token if using API v2)
* You have an AWS account with an SDK IAM role
