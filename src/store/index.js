import { createStore } from "vuex";

export default createStore({
  state: {
    appTheme: "white-theme",
    clockStyle: "Clock1",
  },
  getters: {
    appTheme(state) {
      return state.appTheme;
    },
    clockStyle(state) {
      return state.clockStyle;
    },
  },
  mutations: {
    saveAppTheme(state, appTheme) {
      state.appTheme = appTheme;
    },
    saveClockStyle(state, clockStyle) {
      state.clockStyle = clockStyle;
    },
  },
  actions: {
    updateAppTheme(context, appTheme) {
      context.commit("saveAppTheme", appTheme);
    },
    updateClockStyle(context, clockStyle) {
      context.commit("saveClockStyle", clockStyle);
    },
  },
  modules: {},
});
