import Vue from 'vue'
import VueRouter from 'vue-router'

import Torr from '../views/Torr'
import Podcasts from '../views/Podcasts'
import Rss from '../views/Rss'
import Home from '../views/Home'
import NotFound404 from '../views/NotFound404'

import Login from '../components/Login'
import store from '../../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home', name: 'Home', component: Home,
  },
  {
    path: '/api/torr',
  },
  {
    path: '/torr', name: 'Torr', component: Torr,
    beforeEnter(to, from, next){
      if(!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/podcasts', name: 'Podcasts', component: Podcasts
  },
  {
    path: '/rss', name: 'Rss', component: Rss
  },
  {
    path: '/login', name: 'Login', component: Login
  },
  {
    path: '*', component: NotFound404
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router