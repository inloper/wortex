import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '../store'
import './filters'

// import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';
import BootstrapVue from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
