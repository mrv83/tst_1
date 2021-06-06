<template>
  <div class="home-page">
    <div class="banner">
      <div class="container">
        <h1 class="logo-font">Entries</h1>
      </div>
    </div>
    <div class="container page">
      <div class="row">
        <div class="col-md-9">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
// import RwvTag from "@/components/VTag";
export default {
  name: "home",
  components: {
    // RwvTag
  },
  mounted() {
  },
  computed: {
    ...mapGetters(["isAuthenticated", "tags"]),
    tag() {
      return this.$route.params.tag;
    }
  }
};
</script>