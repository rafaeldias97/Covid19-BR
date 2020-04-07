import axios from 'axios'

let $axios = axios.create({
    baseURL: 'http://localhost:5000/api/'
})

export default $axios
