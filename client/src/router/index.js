import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'NameGenerator' },
  { path: '/login', component: 'login' },
  { path: '/register', component: 'register'},
  { path: '/favorites', component: 'favorites'},
  { path: '/advanced', component: 'advanced'}
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)
const router = new Router({
  routes,
  mode: 'history'
})
export default router