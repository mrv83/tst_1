import { EnrtiesService } from "@/common/api.service";
import { FETCH_ENTRYS } from "./actions.type";
import {
  FETCH_START,
  FETCH_END,
  UPDATE_ENTRY_IN_LIST
} from "./mutations.type";

const state = {
  entries: [],
  isLoading: true,
  entriesCount: 0
};

const getters = {
  entriesCount(state) {
    return state.entriesCount;
  },
  entries(state) {
    return state.entries;
  },
  isLoading(state) {
    return state.isLoading;
  },
  tags(state) {
    return state.tags;
  }
};

const actions = {
  [FETCH_ENTRYS]({ commit }, params) {
    commit(FETCH_START);
    return EnrtiesService.query(params.type, params.filters)
      .then(({ data }) => {
        commit(FETCH_END, data);
      })
      .catch(error => {
        throw new Error(error);
      });
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [FETCH_START](state) {
    state.isLoading = true;
  },
  [FETCH_END](state, { entries, entriesCount }) {
    state.entries = entries;
    state.entriesCount = entriesCount;
    state.isLoading = false;
  },
  [UPDATE_ENTRY_IN_LIST](state, data) {
    state.entries = state.entries.map(entry => {
      if (entry.slug !== data.slug) {
        return entry;
      }
      // We could just return data, but it seems dangerous to
      // mix the results of different api calls, so we
      // protect ourselves by copying the information.
      entry.favorited = data.favorited;
      entry.favoritesCount = data.favoritesCount;
      return entry;
    });
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
