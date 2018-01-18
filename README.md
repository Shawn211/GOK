# GOK
    Python爬虫使用Scrapy框架抓取了王者荣耀官网内所有英雄皮肤高清图并分类保存
## 概述
王者荣耀(Glory of king)，即GOK，是当前手机游戏中最热门的一款MOBA手游。

此爬虫爬取官网所有英雄皮肤图片。使用Chrome对官网抓包，发现`herolist.json`文件与皮肤图片链接有关联。利用gokpic爬虫爬取并分析得到必要信息，再用pipelines对皮肤图片进行爬取，并且按照不同英雄分开包装。
****
|Author|查看README|查看Tree|查看成果|
|:------:|:-------:|:-------:|:-------:|
|Shawn|[README](/README.md)|[Tree](/Tree.md)|[成果展示](#成果展示)|
****
## 详述
### 成果展示
### `英雄总览：`
![](/image/heroes.jpg)
### `孙悟空皮肤总览：`
![](/image/孙悟空.jpg)
***
### 个人观点
pipelines中可以用`file_path`函数改写图片名以及文件夹名。此处用`image_guid`存储图片名，再用`filename`存储文件夹名和文件名，即路径，最后返回`filename`便能创建特定文件名。  
pipelines中`get_media_requests`函数中，当yield Request获取图片时，带上`meta`参数，将当前的`英雄名`、`皮肤名`以及`当前皮肤于皮肤list的索引index`一并传送到`file_path`函数的`request`参数中。
