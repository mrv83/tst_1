import ApiService from "@/common/api.service";
import JwtService from "@/common/jwt.service";
import {
  LOGIN,
  LOGOUT,
  REGISTER,
  CHECK_AUTH,
  UPDATE_USER
} from "./actions.type";
import { SET_AUTH, PURGE_AUTH, SET_ERROR } from "./mutations.type";

const state = {
  errors: null,
  user: {},
  isAuthenticated: !!JwtService.getToken()
};

const getters = {
  currentUser(state) {
    return localStorage.getItem('user');
  },
  isAuthenticated(state) {
    return state.isAuthenticated;
  }
};

const actions = {
  [LOGIN](context, credentials) {
    return ApiService.post("auth/login/", credentials)
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH);
  },
  [REGISTER](context, credentials) {
    // return new Promise((resolve, reject) => {
    //   ApiService.post("auth/registration/", credentials )
    //     .then(({ data }) => {
    //       context.commit(SET_AUTH, data.user);
    //       resolve(data);
    //     })
    //     .catch(({ response }) => {
    //       // context.commit(SET_ERROR, response.data);
    //       reject(response);
    //     });
    // });
    return ApiService.post("auth/registration/", credentials )
        .then(({ data }) => {
          context.commit(SET_AUTH, data.user);
          // resolve(data);
        })
  },
  [CHECK_AUTH](context) {
    if (JwtService.getToken()) {
      ApiService.setHeader();
      ApiService.post("auth/token/verify/", {'token': JwtService.getToken()})
        .then(({ data }) => {
          context.commit(SET_AUTH, data.user);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.data.errors);
        });
    } else {
      context.commit(PURGE_AUTH);
    }
  },
  [UPDATE_USER](context, payload) {
    const { email, username, password, } = payload;
    const user = {
      email,
      username,
      password
    };
    if (password) {
      user.password = password;
    }

    return ApiService.put("auth", user).then(({ data }) => {
      context.commit(SET_AUTH, data.user);
      return data;
    });
  }
};

// const mutations = {
//   [SET_ERROR](state, error) {
//     state.errors = error;
//   },
//   [SET_AUTH](state, user) {
//     state.isAuthenticated = true;
//     state.user = user;
//     state.errors = {};
//     JwtService.saveToken(state.user.token);
//   },
//   [PURGE_AUTH](state) {
//     state.isAuthenticated = false;
//     state.user = {};
//     state.errors = {};
//     Storage.removeItem('jwt');
//     Storage.removeItem('user');
//   }
// };

export default {
  state,
  actions,
  // mutations,
  getters
};
