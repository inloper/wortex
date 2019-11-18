import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function authenticate (userData) {
  return axios.post(`${API_URL}/login`, userData)
}

// export function register (userData) {
//   return axios.post(`${API_URL}/register`, userData)
// }

export function scrape () {
  return axios.get(`${API_URL}/scraper`)
}

// export function search_new (searched_string) {
//   return axios.post(`${API_URL}/scraper/search=`, searched_string)
// }