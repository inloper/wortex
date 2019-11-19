import Vue from 'vue'
import Vuex from 'vuex'

import { isValidJwt, EventBus } from '@/utils'
import { authenticate, scrape, search } from '@/api'

Vue.use(Vuex)

const state = {
  // single source of data
  user: {},
  jwt: {'token': localStorage.getItem('token')}
}

const actions = {
  // LOGIN / AUTHENTICATION
  // asynchronous operations
  login (context, userData) {
    context.commit('setUserData', { userData })
    return authenticate(userData)
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
      .catch(error => {
        console.log('Error Authenticating: ', error)
        EventBus.$emit('failedAuthentication', error)
      })
  },
  logout() {
    return delete localStorage.token
  },
  // register (context, userData) {
  //   context.commit('setUserData', { userData })
  //   return register(userData)
  //     .then(context.dispatch('login', userData))
  //     .catch(error => {
  //       console.log('Error Registering: ', error)
  //       EventBus.$emit('failedRegistering: ', error)
  //     })
  // },

  // SCRAPER RELATED
  scraper() {
    return scrape()
  },
  searchedString(context, body) {
    context.commit('setBodyData', { body })
    return search(body)
      .then(response => console.log(body))
      .catch(error => {
        console.log('Error Authenticating: ', error)
      })
  },
}

const mutations = {
  // isolated data mutations
  setUserData (state, payload) {
    // console.log('setUserData payload = ', payload)
    state.userData = payload.userData
  },
  setJwtToken (state, payload) {
    // console.log('setJwtToken payload = ', payload)
    localStorage.token = payload.jwt.token
    state.jwt = payload.jwt
  },
  setBodyData(state, payload) {
    state.body = payload.body
  }
}

const getters = {
  // reusable data accessors
  isAuthenticated (state) {
    return isValidJwt(state.jwt.token)
  }
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store