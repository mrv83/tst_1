import { EnrtiesService } from "@/common/api.service";
import { FETCH_ENTRY } from "./actions.type";
import { SET_ENTRY, SET_COMMENTS } from "./mutations.type";

export const state = {
  entry: {},
  comments: []
};

export const actions = {
  [FETCH_ENTRY](context, entrySlug) {
    return EnrtiesService.get(entrySlug)
      .then(({ data }) => {
        context.commit(SET_ENTRY, data.entry);
      })
      .catch(error => {
        throw new Error(error);
      });
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_ENTRY](state, entry) {
    state.entry = entry;
  },
  [SET_COMMENTS](state, comments) {
    state.comments = comments;
  }
};

export default {
  state,
  actions,
  mutations
};
