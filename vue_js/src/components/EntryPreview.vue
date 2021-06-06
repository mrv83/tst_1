<template>
  <div class="article-preview">
    <RwvArticleMeta isPreview :article="article" />
    <router-link :to="articleLink" class="preview-link">
      <h1 v-text="article.title" />
      <p v-text="article.description" />
      <span>Read more...</span>
      <TagList :tags="article.tagList" />
    </router-link>
  </div>
</template>

<script>
// import RwvArticleMeta from "./ArticleMeta";
export default {
  name: "EntryPreview",
  components: {
    // RwvArticleMeta,
    // TagList
  },
  props: {
    entry: { type: Object, required: true }
  },
  computed: {
    entryLink() {
      return {
        name: "entry",
        params: {
          id: this.entry.id
        }
      };
    }
  }
};
</script>