<template>
  <div class="auth-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-6 offset-md-3 col-xs-12">
          <h1 class="text-xs-center">Sign in</h1>
          <p class="text-xs-center">
            <router-link :to="{ name: 'register' }">
              Need an account?
            </router-link>
          </p>
          <ul v-if="errors" class="error-messages">
            <li v-for="(v, k) in errors" :key="k">{{ k }} {{ v | error }}</li>
          </ul>
          <form @submit.prevent="onSubmit(email, password)">
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="text"
                v-model="email"
                placeholder="Email"
              />
            </fieldset>
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="password"
                v-model="password"
                placeholder="Password"
              />
            </fieldset>
            <button class="btn btn-lg btn-primary pull-xs-right">
              Sign in
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { LOGIN } from "@/store/actions.type";
import ApiService from "@/common/api.service";
export default {
  name: "Login",
  data() {
    return {
      errors: {},
      email: null,
      password: null
    };
  },
  methods: {
    onSubmit(email, password) {
      ApiService.post("auth/login/", { email: email, password: password })
      .then(({data}) => {
          localStorage.setItem('user', data.user);
          localStorage.setItem('jwt',{'access_token': data.access_token, 'refresh_token': data.refresh_token});
          this.$router.push({ name: "home" })
      })
      .catch(({ response }) => {
        this.errors = response.data;
      });
      // this.$store
      //   .dispatch(LOGIN, { email: email, password: password })
      //   .then(() => {
      //     this.$router.push({ name: "home" })
      //   })
      //   .catch(({ response }) => {
      //     this.errors = response.data;
      //   });
    }
  },
  computed: {
  }
};
</script>