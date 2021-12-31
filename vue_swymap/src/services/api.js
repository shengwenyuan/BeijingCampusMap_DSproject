import axios from 'axios'
import Cookies from 'js-cookie'

export default axios.create({
  baseURL: '/test',
  // baseURL: 'https://echarts.apache.org/examples/data/asset/data/',
  timeout: 9000,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': Cookies.get('csrftoken'),
  }
})