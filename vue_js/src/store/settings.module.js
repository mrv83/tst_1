import { EnrtiesService } from "@/common/api.service";
import { FETCH_ENTRY } from "./actions.type";
import { SET_ENTRY, SET_COMMENTS } from "./mutations.type";

export const state = {
  article: {},
  comments: []
};

export const actions = {
  [FETCH_ENTRY](context, articleSlug) {
    return EnrtiesService.get(articleSlug)
      .then(({ data }) => {
        context.commit(SET_ENTRY, data.article);
      })
      .catch(error => {
        throw new Error(error);
      });
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_ENTRY](state, article) {
    state.article = article;
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
