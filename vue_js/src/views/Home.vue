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
import Entry from "@/components/EntryList";
export default {
  name: "home",
  components: {
    Entry
  },
  mounted() {
  },
  computed: {
    ...mapGetters(["isAuthenticated", "entries"]),
    entry() {
      return this.$route.params.entry;
    }
  }
};
</script>