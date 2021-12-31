
<template>
  <div style="width: 100%; height: 100%">
    <!-- <baidu-map
      id="allmap"
      style="width: 600px; height: 600px; position: relative">
    </baidu-map> -->
    <el-amap
      vid="amapDemo"
      id="allmap"
      style="width: 100%; height: 100%; position: relative"
    >
    </el-amap>
  </div>
</template>

<script>
var echarts = require("echarts");
// require("echarts/extension/bmap/bmap");
require("echarts-extension-amap");

export default {
  name: "EchartDemo",
  data() {
    return {
      chart: null,
      option: {
        amap: {
          center: [116.46, 39.92],
          zoom: 10,
          roam: true,

        },
        series: [
          //[0] lines between stations
          {
            type: "lines",
            coordinateSystem: "amap",
            polyline: true,
            data: [],
            silent: true,
            lineStyle: {
              color: "rgb(20, 135, 145)",
              opacity: 0.8,
              width: 2.5,
            },
            // progressiveThreshold: 500,
            // progressive: 200,
          },
          //[1] from station
          {
            type: "effectScatter",
            coordinateSystem: "amap",
            data: [],
            itemStyle: {
              normal: {
                color: "#ff0000",
              },
            },
            label: {
              normal: {
                formatter: "{b}",
                position: "right",
                show: true,
              },
            },
            rippleEffect: {
              brushType: "stroke",
            },
            symbolSize: 10,
          },
          //[2] to station
          {
            type: "effectScatter",
            coordinateSystem: "amap",
            data: [],
            itemStyle: {
              normal: {
                color: "#0000ff",
              },
            },
            label: {
              normal: {
                formatter: "{b}",
                position: "right",
                show: true,
              },
            },
            rippleEffect: {
              brushType: "stroke",
            },
            symbolSize: 10,
          },
          //[3] normal stations
          {
            type: "scatter",
            coordinateSystem: "amap",
            data: [],
            itemStyle: {
              normal: {
                color: "#66000a",
              },
            },
            label: {
              normal: {
                formatter: "{b}",
                position: "right",
                show: true,
              },
            },
            symbolSize: 7,
          },
        ],
      },
    };
  },
  methods: {
    freshStation() {
      //  ['stepnum', 'stationName', 'gcj02_longi', 'gcj02_lati', 'wgs84_longi', 'wgs84_lati', 'lineName', 'lineType', 'FTW']
      this.option.series[0].data=[];
      this.option.series[1].data=[];
      this.option.series[2].data=[];
      this.option.series[3].data=[];


      var routeinfo = this.$store.state.messages.messages;
      var stations = {'coords':[]};
      for(var y = 0; y < routeinfo.length; y++){
        stations['coords'].push([]);
      }
      // {'coords':[[], [], []]}
      for (var i = 0; i < routeinfo.length; i++) {
        if (routeinfo[i]["stepnum"] == 0) {
          this.option.series[2].data = [
            {
              name: routeinfo[i]["stationName"],
              value: [
                routeinfo[i]["gcj02_longi"],
                routeinfo[i]["gcj02_lati"],
              ],
            },
          ];
        } else if (routeinfo[i]["stepnum"] == routeinfo.length - 1) {
          this.option.series[1].data = [
            {
              name: routeinfo[i]["stationName"],
              value: [
                routeinfo[i]["gcj02_longi"],
                routeinfo[i]["gcj02_lati"],
              ],
            },
          ];
        } else {
          this.option.series[3].data.push({
            name: routeinfo[i]["stationName"],
            value: [
              routeinfo[i]["gcj02_longi"],
              routeinfo[i]["gcj02_lati"],
            ],
          });
        }
        // AddressSort | IndexSort   T=O(n)
        stations['coords'][routeinfo[i]["stepnum"]] = [
          routeinfo[i]["gcj02_longi"], routeinfo[i]["gcj02_lati"]
          ];
      }
      this.option.series[0].data.push(stations);
      this.chart.setOption(this.option);
    },
  },
  mounted() {
    this.chart = echarts.init(document.getElementById("allmap"));
    setTimeout(() => {
      this.chart.setOption(this.option);
    }, 1000);
  },
};
</script>

<style lang="scss" scoped>
</style>