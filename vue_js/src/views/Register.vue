<template>
  <div class="auth-page">
    <div class="container page">
      <div class="row">
        <div class="col-md-6 offset-md-3 col-xs-12">
          <h1 class="text-xs-center">Sign up</h1>
          <p class="text-xs-center">
            <router-link :to="{ name: 'login' }">
              Have an account?
            </router-link>
          </p>
          <form @submit.prevent="onSubmit">
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="text"
                v-model="email"
                placeholder="Email"
              />
            </fieldset>
            <ul v-if="errors && errors.email" class="error-messages">
              <li>{{ errors.email | error }}</li>
            </ul>
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="password"
                v-model="password1"
                placeholder="Password"
              />
            </fieldset>
            <ul v-if="errors && errors.password1" class="error-messages">
              <li>{{ errors.password1 | error }}</li>
            </ul>
            <fieldset class="form-group">
              <input
                class="form-control form-control-lg"
                type="password"
                v-model="password2"
                placeholder="Confirm password"
              />
            </fieldset>
            <button class="btn btn-lg btn-primary pull-xs-right">
              Sign up
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { REGISTER } from "@/store/actions.type";
export default {
  name: "Register",
  data() {
    return {
      errors: {},
      email: "",
      password1: "",
      password2: ""
    };
  },
  computed: {
  },
  methods: {
    onSubmit() {
      this.$store
        .dispatch(REGISTER, {
          email: this.email,
          password1: this.password1,
          password2: this.password2
        })
        .then(() => this.$router.push({ name: "home" }))
        .catch(({ response }) => {
          this.errors = response.data;
        });
    }
  }
};
</script>