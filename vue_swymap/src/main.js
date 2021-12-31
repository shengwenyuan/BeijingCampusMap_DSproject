import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'amfe-flexible/index.js';
import App from './App.vue'
import store from '@/stores'

// import BaiduMap from 'vue-baidu-map'
// Vue.use(BaiduMap,{ak:'P0ebUOAIcG1kG4PSB4FS7fSUBAEx2cfZ'})
import VueAMap from 'vue-amap'
Vue.use(VueAMap);
VueAMap.initAMapApiLoader({
  key: '10c5eb9cf93f104de57d76876768cfe4',

})

Vue.config.productionTip = false

Vue.use(ElementUI)

new Vue({
  el: '#app',
  store,
  render: h => h(App),
}).$mount('#app')


function setRem() {
  let htmlWidth = document.documentElement.clientWidth || document.body.clientWidth;
  let htmlDom = document.getElementsByTagName('html')[0];
  htmlDom.style.fontSize = (htmlWidth / 10) > 75 ? "75px" : htmlWidth / 10 + 'px';
}
setRem();
window.onresize = function () {
  setRem();
}