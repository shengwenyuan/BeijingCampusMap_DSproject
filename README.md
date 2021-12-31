# BeijingCampusMap_DSproject
the project of data structure course in latter semester of 2021

## Introduction
To practice what we learned in data structure course in first semester, we are asked to implement a simplified map software, which works as the guide of route between campus in Beijing. 
It should use proper data structure and has a GUI ineraction.

In general, I depart the project into four parts. 

**1. network crawling**

  To collect the real information of public traffic in Beijing, it is need to crawl from business map web pages. The project collects around 4k nodes from 400 bus lines and every subway lines.
  
**2. design(select) algorithm**

  To find the shortest path of source campus in different rights(includes cost on time, route or money), I use the Dijkstra algorithm with heap optimization, which has a balance on the time of 
    user corresponding and space consumption.

**3. build the front-end by Vue**

  The GUI is implemented on web and is helpted with Vue frame and numbers of build-databases 
  like [Element UI](https://element.eleme.cn/#/zh-CN/component/installation), [ECharts](https://echarts.apache.org/examples/zh/index.html#chart-type-map).

**4. build the back-end by django**

  Since database usages are forbidden in this project, it works only for connecting with the front end. Anyway, it delivers the result of algorithm to the web page.
