import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function authenticate(userData) {
  return axios.post(`${API_URL}/login`, userData)
}
export function register (userData) {
  return axios.post(`${API_URL}/register`, userData)
}
export function scrape() {
  return axios.get(`${API_URL}/scraper`)
}
export function search(body) {
  return axios.post(`${API_URL}/scraper/search=`, body)
}
export function fetchTorrData(jwt) {
  // console.log(jwt)
  return axios.get(`${API_URL}/torr`, { headers: { Authorization: `Bearer: ${jwt}` } })
}
