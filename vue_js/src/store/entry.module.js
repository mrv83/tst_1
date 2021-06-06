import Vue from "vue";
import {
  EnrtiesService
} from "@/common/api.service";
import {
  FETCH_ENTRY,
  ENTRY_PUBLISH,
  ENTRY_EDIT,
  ENTRY_DELETE,
  ENTRY_RESET_STATE
} from "./actions.type";
import {
  RESET_STATE,
  SET_ENTRY,
  // UPDATE_ENTRY_IN_LIST
} from "./mutations.type";

const initialState = {
  entry: {
    user: {},
    date: "",
    duration: "",
    distance: ""
  }
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_ENTRY](context, entrySlug, prevEntry) {
    // avoid extronuous network call if entry exists
    if (prevEntry !== undefined) {
      return context.commit(SET_ENTRY, prevEntry);
    }
    const { data } = await EnrtiesService.get(entrySlug);
    context.commit(SET_ENTRY, data.entry);
    return data;
  },
  [ENTRY_PUBLISH]({ state }) {
    return EnrtiesService.create(state.entry);
  },
  [ENTRY_DELETE](context, slug) {
    return EnrtiesService.destroy(slug);
  },
  [ENTRY_EDIT]({ state }) {
    return EnrtiesService.update(state.entry.slug, state.entry);
  },
  [ENTRY_RESET_STATE]({ commit }) {
    commit(RESET_STATE);
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_ENTRY](state, entry) {
    state.entry = entry;
  },
  [RESET_STATE]() {
    for (let f in state) {
      Vue.set(state, f, initialState[f]);
    }
  }
};

const getters = {
  entry(state) {
    return state.entry;
  },
  comments(state) {
    return state.comments;
  }
};

export default {
  state,
  actions,
  mutations,
  getters
};
