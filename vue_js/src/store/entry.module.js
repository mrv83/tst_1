import Vue from "vue";
import {
  EnrtiesService
} from "@/common/api.service";
import {
  FETCH_ENTRY,
  ENTRY_PUBLISH,
  ENTRY_EDIT,
  ENTRY_EDIT_ADD_TAG,
  ENTRY_EDIT_REMOVE_TAG,
  ENTRY_DELETE,
  ENTRY_RESET_STATE
} from "./actions.type";
import {
  RESET_STATE,
  SET_ENTRY,
  UPDATE_ENTRY_IN_LIST
} from "./mutations.type";

const initialState = {
  article: {
    author: {},
    title: "",
    description: "",
    body: "",
    tagList: []
  },
  comments: []
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_ENTRY](context, articleSlug, prevArticle) {
    // avoid extronuous network call if article exists
    if (prevArticle !== undefined) {
      return context.commit(SET_ENTRY, prevArticle);
    }
    const { data } = await EnrtiesService.get(articleSlug);
    context.commit(SET_ENTRY, data.article);
    return data;
  },
  [ENTRY_PUBLISH]({ state }) {
    return EnrtiesService.create(state.article);
  },
  [ENTRY_DELETE](context, slug) {
    return EnrtiesService.destroy(slug);
  },
  [ENTRY_EDIT]({ state }) {
    return EnrtiesService.update(state.article.slug, state.article);
  },
  [ENTRY_EDIT_ADD_TAG](context, tag) {
    context.commit(TAG_ADD, tag);
  },
  [ENTRY_EDIT_REMOVE_TAG](context, tag) {
    context.commit(TAG_REMOVE, tag);
  },
  [ENTRY_RESET_STATE]({ commit }) {
    commit(RESET_STATE);
  }
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_ENTRY](state, article) {
    state.article = article;
  },
  [RESET_STATE]() {
    for (let f in state) {
      Vue.set(state, f, initialState[f]);
    }
  }
};

const getters = {
  article(state) {
    return state.article;
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
