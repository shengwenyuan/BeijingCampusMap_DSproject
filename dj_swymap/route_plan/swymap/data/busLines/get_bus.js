AMap.plugin(["AMap.LineSearch"], function() {
    //实例化公交线路查询类
    var linesearch = new AMap.LineSearch({
        pageIndex: 1, //页码，默认值为1
        pageSize: 1, //单页显示结果条数，默认值为20，最大值为50
        city: "北京", //限定查询城市，可以是城市名（中文/中文全拼）、城市编码，默认值为『全国』
        extensions: "all" //是否返回公交线路详细信息，默认值为『base』
    });

    //执行公交路线关键字查询
    linesearch.search('536', function(status, result) {
        //打印状态信息status和结果信息result
        console.log(status, result);
    });
});

