import axios from 'axios'

export default async ({ Vue }) => {
  Vue.prototype.$axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/api'
  })
}
