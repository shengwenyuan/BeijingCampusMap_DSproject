import api from '@/services/api'

export default {
  fetchMessages(get_url) {
    // http://127.0.0.1:8000/routeinfo + /pku-bjut-0.json
    return api.get(get_url)
              .then(response => response.data)
  },
  postMessage(payload) {
    return api.post(`messages/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`messages/${msgId}`)
              .then(response => response.data)
  }
}