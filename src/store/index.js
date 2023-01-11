import { createStore } from "vuex";

export default createStore({
  state: {
    appTheme: "white-theme",
  },
  getters: {
    appTheme(state) {
      return state.appTheme;
    },
  },
  mutations: {
    saveAppTheme(state, appTheme) {
      state.appTheme = appTheme;
    },
  },
  actions: {
    updateAppTheme(context, appTheme) {
      context.commit("saveAppTheme", appTheme);
    },
  },
  modules: {},
});
