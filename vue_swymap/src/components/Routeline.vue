<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item
        v-for="(activity, index) in activities"
        :key="index"
        :icon="activity.icon"
        :type="activity.type"
        :color="activity.color"
        :size="activity.size"
        :timestamp="activity.timestamp"
      >
        {{ activity.content }}
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activities: [],
    };
  },
  methods: {
      freshInfo() {
        var routeinfo = this.$store.state.messages.messages;
        let sortedInfo = [];
        for(var y = 0; y < routeinfo.length; y++){
            sortedInfo.push([]);
        }
        for(var i = 0; i < routeinfo.length; i++){
            sortedInfo[routeinfo[i]["stepnum"]]=[
                routeinfo[i]["stationName"], routeinfo[i]["lineName"], routeinfo[i]["lineType"],
                routeinfo[i]["w_dist"], routeinfo[i]["w_time"], routeinfo[i]["w_cost"]
            ]
        }
        let index_now = sortedInfo[0]
        let index_next
        var s1, s2, s3, s4, s5, s6
        this.activities = []
        for(var j = 1; j < routeinfo.length; j++){
            index_next = sortedInfo[j]
            s1 = "于“"+index_now[0]+"”换乘地铁"+index_next[1];
            s2 = "于“"+index_now[0]+"”开始乘坐地铁"+index_now[1];
            s3 = "于“"+index_now[0]+"”换乘公交"+index_next[1]+"路";
            s4 = "于“"+index_now[0]+"”开始乘坐公交"+index_now[1]+"路";
            s5 = "抵达终点站"+index_next[0]+
                "距离："+parseInt(index_next[3])+"km"+
                "时间："+index_next[4]+"min"+
                "花销："+index_next[5]+"￥";  
            s6 = "距离："+parseInt(index_now[3])+"km"+
                "时间："+index_now[4]+"min"+
                "花销："+index_now[5]+"￥";
            if (index_now == sortedInfo[0]){
                    if (index_now[2] == 'subway')
                        this.activities.push({content: s2, color: "#0000ff", size: "large"});
                    else
                        this.activities.push({content: s4, color: "#0000ff", size: "large"});
                }
            else if (index_next == sortedInfo[routeinfo.length-1]){
                this.activities.push({content: s5, color: "#ff0000", size: "large"});
            }
            else if ((index_now[1]!=index_next[1]) || 
            (index_now[2]!=index_next[2])){
            if (index_next[2] == 'subway')
                this.activities.push({content: s1 + s6, color: "#66000a"});
            else
                this.activities.push({content: s3 + s6, color: "#66000a"});                    

            }
            
            index_now = index_next
        }
      },
  },
};
</script>

