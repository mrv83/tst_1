<template>
  <div>
    <div v-if="isLoading" class="entry-preview">Loading entries...</div>
    <div v-else>
      <div v-if="entries.length === 0" class="entry-preview">
        No entries are here... yet.
      </div>
<!--      <EntryPreview-->
<!--        v-for="(entry, index) in entries"-->
<!--        :entry="entry"-->
<!--        :key="entry.title + index"-->
<!--      />-->
<!--      <VPagination :pages="pages" :currentPage.sync="currentPage" />-->
    </div>
  </div>
</template>

<script>
// import { mapGetters } from "vuex";
// import EntryPreview from "./VEntryPreview";
// import VPagination from "./VPagination";
// import { FETCH_ENTRYS } from "../store/actions.type";
export default {
  name: "EntryList",
  components: {
    // EntryPreview,
    // VPagination
  },
  props: {
    type: {
      type: String,
      required: false,
      default: "all"
    },
    author: {
      type: String,
      required: false
    },
    tag: {
      type: String,
      required: false
    },
    favorited: {
      type: String,
      required: false
    },
    itemsPerPage: {
      type: Number,
      required: false,
      default: 10
    }
  },
  data() {
    return {
      currentPage: 1
    };
  },
  computed: {
    // listConfig() {
    //   const { type } = this;
    //   const filters = {
    //     offset: (this.currentPage - 1) * this.itemsPerPage,
    //     limit: this.itemsPerPage
    //   };
    //   if (this.author) {
    //     filters.author = this.author;
    //   }
    //   if (this.tag) {
    //     filters.tag = this.tag;
    //   }
    //   if (this.favorited) {
    //     filters.favorited = this.favorited;
    //   }
    //   return {
    //     type,
    //     filters
    //   };
    // },
    // pages() {
    //   if (this.isLoading || this.entriesCount <= this.itemsPerPage) {
    //     return [];
    //   }
    //   return [
    //     ...Array(Math.ceil(this.entriesCount / this.itemsPerPage)).keys()
    //   ].map(e => e + 1);
    // },
    // ...mapGetters(["entriesCount", "isLoading", "entries"])
  },
  watch: {
    // currentPage(newValue) {
    //   this.listConfig.filters.offset = (newValue - 1) * this.itemsPerPage;
    //   this.fetchEntries();
    // },
    // type() {
    //   this.resetPagination();
    //   this.fetchEntries();
    // },
    // author() {
    //   this.resetPagination();
    //   this.fetchEntries();
    // },
    // tag() {
    //   this.resetPagination();
    //   this.fetchEntries();
    // },
    // favorited() {
    //   this.resetPagination();
    //   this.fetchEntries();
    // }
  },
  mounted() {
    // this.fetchEntries();
  },
  methods: {
    // fetchEntries() {
    //   this.$store.dispatch(FETCH_ENTRYS, this.listConfig);
    // },
    // resetPagination() {
    //   this.listConfig.offset = 0;
    //   this.currentPage = 1;
    // }
  }
};
</script>