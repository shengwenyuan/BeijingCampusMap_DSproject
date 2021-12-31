<template>
  <el-select id="to" v-model="value" placeholder="请选择">
    <el-option ref="to"
      v-for="item in cities"
      :key="item.value"
      :label="item.label"
      :value="item.value">
      <span style="float: left">{{ item.label }}</span>
      <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
    </el-option>
  </el-select>
</template>

<script>
  export default {
    data() {
      return {
        cities: [{
          value: 'PKU',
          label: '北京大学'
        }, {
          value: 'BJUT',
          label: '北京工业大学'
        }, {
          value: 'UIBE',
          label: '对外经贸'
        }, {
          value: 'BNU',
          label: '北京师范大学'
        }, {
          value: 'BIT',
          label: '北京理工大学'
        }, {
          value: 'CUC',
          label: '中国传媒大学'
        }, {
          value: 'RUC',
          label: '北京人民大学'
        }, {
          value: 'BJU',
          label: '北京交通大学'
        }],
        value: ''
      }
    }
  }
</script>