<template>
  <div style="padding: 30px">
    <el-row type="flex" justify="center">
      <vue-echarts
        api="/china/line/xinzeng"
        style="height: 700px"
      ></vue-echarts>
    </el-row>
    <el-row type="flex" justify="center">
      <vue-echarts
        api="/china/line/leiji"
        style="height: 700px"
      ></vue-echarts>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
</script>