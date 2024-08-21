<template>
  <div style="padding: 30px">
    <h1 style="text-align: center">国内疫情数据</h1>
    <p style="text-align: center; color: #999">更新时间: {{ ct }}</p>
    <el-row type="flex" justify="center">
      <el-table
        :data="chinaTable.result"
        style="width: 80%; margin-bottom: 20px"
        :tree-props="{ children: 'child' }"
        row-key="name1"
        :border="true"
      >
        <el-table-column
          prop="name1"
          label="地区"
          align="left"
        ></el-table-column>
        <el-table-column prop="quezhen_add" align="center" :sortable="true">
          <template #header>
            <span style="color: #455fce">昨日新增</span>
          </template>
        </el-table-column>
        <el-table-column prop="quezhen" align="center" :sortable="true">
          <template #header>
            <span style="color: red">累计确诊</span>
          </template>
        </el-table-column>
        <el-table-column prop="zhiyu" align="center" :sortable="true">
          <template #header>
            <span style="color: #15a582">治愈</span>
          </template>
        </el-table-column>
        <el-table-column prop="siwang" align="center" :sortable="true">
          <template #header>
            <span style="color: gray">死亡</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <h1 style="text-align: center">国外疫情数据</h1>
    <p style="text-align: center; color: #999">更新时间: {{ ft }}</p>
    <el-row type="flex" justify="center">
      <el-table
        :data="foreignTable.result"
        style="width: 80%; margin-bottom: 20px"
        :border="true"
      >
        <el-table-column
          prop="name2"
          label="国家"
          align="left"
        ></el-table-column>
        <el-table-column prop="quezhen_add" align="center" :sortable="true">
          <template #header>
            <span style="color: #455fce">昨日新增</span>
          </template>
        </el-table-column>
        <el-table-column prop="quezhen" align="center" :sortable="true">
          <template #header>
            <span style="color: red">累计确诊</span>
          </template>
        </el-table-column>
        <el-table-column prop="zhiyu" align="center" :sortable="true">
          <template #header>
            <span style="color: #15a582">治愈</span>
          </template>
        </el-table-column>
        <el-table-column prop="siwang" align="center" :sortable="true">
          <template #header>
            <span style="color: gray">死亡</span>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import request from "/@/utils/request";
import { formatDateTime } from "/@/utils/tools";
import { reactive, ref, computed } from "vue";
const chinaTable = ref<any>({
  timestamp: null,
  result: [],
});
const foreignTable = ref<any>({
  timestamp: null,
  result: [],
});
const ct = computed(() => {
  return formatDateTime(chinaTable.value.timestamp);
});
const ft = computed(() => {
  return formatDateTime(foreignTable.value.timestamp);
});

request.get("/detail/china").then((res) => {
  chinaTable.value = res.data;
});
request.get("/detail/foreign").then((res) => {
  foreignTable.value = res.data;
});
</script>