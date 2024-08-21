import request from '/@/utils/request'
import { AxiosResponse } from 'axios'

export function apiOverall(): Promise<any> {
    return request({
        url: `/overall/`,
        method: 'get',
    })
}