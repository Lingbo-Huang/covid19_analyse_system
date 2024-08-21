import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import { IMenubarList } from '/@/type/store/layout'
import { components } from '/@/router/asyncRouter'

const Components: IObject<() => Promise<typeof import('*.vue')>> = Object.assign({}, components, {
    Layout: (() => import('/@/layout/index.vue')) as unknown as () => Promise<typeof import('*.vue')>,
    Redirect: (() => import('/@/layout/redirect.vue')) as unknown as () => Promise<typeof import('*.vue')>,
    LayoutBlank: (() => import('/@/layout/blank.vue')) as unknown as () => Promise<typeof import('*.vue')>
})

// 静态路由页面
export const allowRouter: Array<IMenubarList> = [
    {
        name: 'Overall',
        path: '/',
        component: Components['Layout'],
        redirect: '/Overall',
        meta: { title: '国内疫情', icon: 'el-icon-eleme' },
        children: [
            {
                name: 'List',
                path: '/Overall',
                component: Components['Overall'],
                meta: { title: '国内疫情', icon: '' }
            }
        ]
    },
    {
        name: 'Curve',
        path: '/Curve',
        component: Components['Layout'],
        redirect: '/Curve/List',
        meta: { title: '疫情走势', icon: 'el-icon-eleme' },
        children: [
            {
                name: 'CurveList',
                path: '/Curve/List',
                component: Components['Curve'],
                meta: { title: '疫情走势', icon: '' }
            }
        ]
    },
    {
        name: 'Data',
        path: '/Data',
        component: Components['Layout'],
        redirect: '/Data/List',
        meta: { title: '疫情数据', icon: 'el-icon-eleme' },
        children: [
            {
                name: 'DataList',
                path: '/Data/List',
                component: Components['Data'],
                meta: { title: '疫情数据', icon: '' }
            }
        ]
    },
    {
        name: 'News',
        path: '/News',
        component: Components['Layout'],
        redirect: '/News/List',
        meta: { title: '疫情新闻', icon: 'el-icon-eleme' },
        children: [
            {
                name: 'NewsList',
                path: '/News/List',
                component: Components['News'],
                meta: { title: '疫情新闻', icon: '' }
            }
        ]
    },
    {
        name: 'Analyse',
        path: '/Analyse',
        component: Components['Layout'],
        redirect: '/Analyse/List',
        meta: { title: '舆情分析', icon: 'el-icon-eleme' },
        children: [
            {
                name: 'AnalyseList',
                path: '/Analyse/List',
                component: Components['Analyse'],
                meta: { title: '舆情分析', icon: '' }
            }
        ]
    },
    {
        name: 'ErrorPage',
        path: '/ErrorPage',
        meta: { title: '错误页面', icon: 'el-icon-eleme', hidden: true },
        component: Components.Layout,
        redirect: '/ErrorPage/404',
        children: [
            {
                name: '401',
                path: '/ErrorPage/401',
                component: Components['401'],
                meta: { title: '401', icon: 'el-icon-s-tools' }
            },
            {
                name: '404',
                path: '/ErrorPage/404',
                component: Components['404'],
                meta: { title: '404', icon: 'el-icon-s-tools' }
            }
        ]
    },
    {
        name: 'RedirectPage',
        path: '/redirect',
        component: Components['Layout'],
        meta: { title: '重定向页面', icon: 'el-icon-eleme', hidden: true },
        children: [
            {
                name: 'Redirect',
                path: '/redirect/:pathMatch(.*)*',
                meta: {
                    title: '重定向页面',
                    icon: ''
                },
                component: Components.Redirect
            }
        ]
    },
    {
        name: 'Login',
        path: '/Login',
        component: Components.Login,
        meta: { title: '登录', icon: 'el-icon-eleme', hidden: true }
    },
    {
        name: 'Register',
        path: '/Register',
        component: Components.Register,
        meta: { title: '注册', icon: 'el-icon-eleme', hidden: true }
    },
]

const router = createRouter({
    history: createWebHashHistory(), // createWebHistory
    routes: allowRouter as RouteRecordRaw[]
})

export default router