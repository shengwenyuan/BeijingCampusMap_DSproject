<template>
  <div class="hello">
    <el-container>
      <el-header id="header" height="80px">北京高校公交导航系统</el-header>
      <el-container>
        <el-aside id="aside" width="50%">
          起点 <br />
          <el-select-from ref="fr"></el-select-from> <br />
          终点 <br />
          <el-select-to ref="to"></el-select-to> <br />
          <br />
          <el-row>
            <el-button type="primary" round @click="query('-0')">路程近</el-button>
            <el-button type="primary" round @click="query('-1')">时间短</el-button>
            <el-button type="primary" round @click="query('-2')">花钱少</el-button>
          </el-row>
          <el-divider></el-divider>
          <routeline ref="rl"></routeline>
          
        </el-aside>
        <el-main id="main" style="width: 100%; height: 7rem">
          <echart-map ref="map"></echart-map>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import SelectFrom from "@/components/SelectFrom";
import SelectTo from "@/components/SelectTo";
import EchartMap from "@/components/EchartMap";
import Routeline from "@/components/Routeline";
import messageService from "../services/messageService";

export default {
  name: "homepage",
  props: {},
  components: {
    "el-select-from": SelectFrom,
    "el-select-to": SelectTo,
    "echart-map": EchartMap,
    "routeline": Routeline
  },
  methods: {
    async query(w){
      if(this.$refs.fr.value == this.$refs.to.value){
        alert("immediate tp! serious?")
        return
      }
      let get_url = '/' + this.$refs.fr.value + '-' + this.$refs.to.value + w + '.json'
      let fetch_result = await messageService.fetchMessages(get_url);
      console.log(get_url);
      if (!fetch_result){
        alert("fetch fail")
        return;
      }
      this.$store.dispatch("messages/setMessages", fetch_result);
      this.$refs.map.freshStation();
      this.$refs.rl.freshInfo();
    },
  },
};
</script>

<style>
#header {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  color: cornflowerblue;
  font-size: 37px;
  text-align: center;
}
#aside {
  color: #2c3e50;
  font-size: 27px;
}
</style>
