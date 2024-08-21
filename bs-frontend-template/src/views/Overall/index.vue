<template>
  <div style="padding: 30px">
    <div style="text-align: left">
      <div style="height: 40px; line-height: 40px">
        <label style="font-weight: 800; font-size: 18px">国内疫情</label
        ><label style="float: right; color: rgb(65, 151, 253)"
          >数据更新时间： {{ updateTime }}</label
        >
      </div>
    </div>
    <el-card shadow="always" style="background: rgb(244, 244, 245)">
      <el-row>
        <el-col :span="6" style="padding-left: 10px; padding-right: 10px">
          <div style="text-align: center">
            <div
              class="sum_numb"
              style="
                color: rgb(245, 82, 83);
                font-size: 20px;
                margin-bottom: 8px;
              "
            >
              {{ overall.confirmedCount }}
            </div>
            <div
              class="sum_numb"
              style="color: rgb(51, 51, 51); font-size: 14px"
            >
              确诊病例
            </div>
            <div
              class="sum_numb"
              style="
                font-size: 13px;
                color: rgb(153, 153, 153);
                margin-top: 8px;
              "
            >
              <label style="font-weight: 200">较昨日 </label
              ><label style="color: rgb(245, 82, 83)"
                ><span v-if="overall.confirmedIncr > 0">+</span
                >{{ overall.confirmedIncr }}</label
              >
            </div>
          </div>
        </el-col>
        <el-col :span="6" style="padding-left: 10px; padding-right: 10px">
          <div style="text-align: center">
            <div
              class="sum_numb"
              style="
                color: rgb(255, 150, 30);
                font-size: 20px;
                margin-bottom: 8px;
              "
            >
              {{ overall.suspectedCount }}
            </div>
            <div
              class="sum_numb"
              style="color: rgb(51, 51, 51); font-size: 14px"
            >
              疑似病例
            </div>
            <div
              class="sum_numb"
              style="
                font-size: 13px;
                color: rgb(153, 153, 153);
                margin-top: 8px;
              "
            >
              <label style="font-weight: 200">较昨日 </label
              ><label style="color: rgb(255, 150, 30)"
                ><span v-if="overall.suspectedIncr > 0">+</span
                >{{ overall.suspectedIncr }}</label
              >
            </div>
          </div>
        </el-col>
        <el-col :span="6" style="padding-left: 10px; padding-right: 10px">
          <div style="text-align: center">
            <div
              class="sum_numb"
              style="
                color: rgb(102, 102, 108);
                font-size: 20px;
                margin-bottom: 8px;
              "
            >
              {{ overall.deadCount }}
            </div>
            <div
              class="sum_numb"
              style="color: rgb(51, 51, 51); font-size: 14px"
            >
              死亡病例
            </div>
            <div
              class="sum_numb"
              style="
                font-size: 13px;
                color: rgb(153, 153, 153);
                margin-top: 8px;
              "
            >
              <label style="font-weight: 200">较昨日 </label
              ><label style="color: rgb(102, 102, 108)"
                ><span v-if="overall.deadIncr > 0">+</span
                >{{ overall.deadIncr }}</label
              >
            </div>
          </div>
        </el-col>
        <el-col :span="6" style="padding-left: 10px; padding-right: 10px">
          <div style="text-align: center">
            <div
              class="sum_numb"
              style="
                color: rgb(23, 139, 80);
                font-size: 20px;
                margin-bottom: 8px;
              "
            >
              {{ overall.curedCount }}
            </div>
            <div
              class="sum_numb"
              style="color: rgb(51, 51, 51); font-size: 14px"
            >
              治愈病例
            </div>
            <div
              class="sum_numb"
              style="
                font-size: 13px;
                color: rgb(153, 153, 153);
                margin-top: 8px;
              "
            >
              <label style="font-weight: 200">较昨日 </label
              ><label style="color: rgb(23, 139, 80)"
                ><span v-if="overall.curedIncr > 0">+</span
                >{{ overall.curedIncr }}</label
              >
            </div>
          </div>
        </el-col>
      </el-row>
    </el-card>
    <el-row :gutter="20" style="margin-top: 20px">
      <el-col :span="12">
        <vue-echarts
          api="/china/map/"
          style="height: 500px"
        ></vue-echarts>
      </el-col>
      <el-col :span="12">
        <vue-echarts
          api="/china/bar/"
          style="height: 500px"
        ></vue-echarts>
      </el-col>
    </el-row>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, computed } from "vue";
import { apiOverall } from "/@/api/covid19";
import { formatDateTime } from "/@/utils/tools";

const overall = ref<any>({});
const getOverall = async () => {
  const { data } = await apiOverall();
  console.log(data);
  overall.value = data;
};
const updateTime = computed(() => {
  if (overall.value.updateTime !== undefined) {
    return formatDateTime(overall.value.updateTime);
  }
});

getOverall();
</script>