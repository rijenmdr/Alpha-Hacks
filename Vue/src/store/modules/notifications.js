import axios from "axios";
const state = {
  notifications: [],
};
const mutations = {
  PUSH_NOTIFICATIONS(state, notification) {
    state.notifications.push({
      ...notification,
      id: (Math.random().toString(36) + Date.now().toString(36)).substr(2),
    });
  },
  POP_NOTIFICATIONS(state, notificationToRemove) {
    state.notifications = state.notifications.filter((notification) => {
      return notification.id != notificationToRemove.id;
    });
  },
};
const actions = {
  addNotifications({ commit }, notification) {
    commit("PUSH_NOTIFICATIONS", notification);
  },
  removeNotifications({ commit }, notification) {
    commit("POP_NOTIFICATIONS", notification);
  },
};
const getters = {
  getNotifications: (state) => {
    return state.notifications;
  },
};
export default {
  state,
  getters,
  mutations,
  actions,
};
