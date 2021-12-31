import messageService from '../../services/messageService'

const state = {
  messages: [{'a':1}]
}

const getters = {
  messages: state => {
    return state.messages
  }
}

const actions = {
  getMessages ({ commit }, get_url) {
    messageService.fetchMessages(get_url)
    .then(messages => {
      commit('setMessages', messages)
    })
  },
  setMessages ({ commit }, fetch_result) {
    commit('setMessages', fetch_result)
  },
  
  addMessage({ commit }, message) {
    messageService.postMessage(message)
    .then(() => {
      commit('addMessage', message)
    })
  },
  deleteMessage( { commit }, msgId) {
    messageService.deleteMessage(msgId)
    commit('deleteMessage', msgId)
  }
}

const mutations = {
  setMessages (state, messages) {
    state.messages = messages
  },
  addMessage(state, message) {
    state.messages.push(message)
  },
  deleteMessage(state, msgId) {
    state.messages = state.messages.filter(obj => obj.pk !== msgId)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}