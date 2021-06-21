<template>
  <div>
    <div v-if="isLoading" class="entry-preview">Loading entries...</div>
    <div v-else>
      <div v-if="entries.length === 0" class="entry-preview">
        No entries are here... yet.
      </div>
      <div v-else>
        <div class="row">
          <div class="col-md-2"><span>Date</span></div>
          <div class="col-md-2"><span>Duration</span></div>
          <div class="col-md-2"><span>Distance</span></div>
          <div class="col-md-2"><span>Average speed</span></div>
          <div class="col-md-2"><span>Action</span></div>
        </div>
        <div class="row" v-for="entry in entries" v-bind:key="entry">
          <div class="col-md-2"><input v-model="entry.date"/></div>
          <div class="col-md-2"><input v-model="entry.duration"/></div>
          <div class="col-md-2"><input v-model="entry.distance"/></div>
          <div class="col-md-2"><span>{{ speed(entry) }}</span></div>
          <div class="col-md-2">
            <input v-if="entry.not_saved && entry.date && entry.duration && entry.distance" type="button" @click="saveEntry(entry)" value="Save"/>
            <input type="button" @click="deleteEntry(entry)" value="Delete"/>
          </div>
        </div>
        <Pagination :pages="pages" :currentPage.sync="currentPage" />
      </div>
      <div class="submit-row modal-button">
          <input type="button" @click="addEntry($event)" value="Add entry"/>
      </div>
    </div>
  </div>
</template>

<script>

import Pagination from "./Pagination";
import EnrtiesService from '@/common/api.service';

export default {
  name: "EntryList",
  components: {
    Pagination
  },
  props: {
    itemsPerPage: {
      type: Number,
      required: false,
      default: 50
    }
  },
  data() {
    return {
      // entries: [],
      limit: 50,
      offset: 0,
      currentPage: 1,
      start_date: null,
      end_date: null
    };
  },
  computed: {
    speed: function (entry) {
      return (entry.distance / entry.duration).toFixed(2)
    },
    listConfig() {
      const filters = {
        offset: (this.currentPage - 1) * this.itemsPerPage,
        limit: this.itemsPerPage
      };
      return filters
    },
    pages() {
      if (this.isLoading || this.entriesCount <= this.itemsPerPage) {
        return [];
      }
      return [
        ...Array(Math.ceil(this.entriesCount / this.itemsPerPage)).keys()
      ].map(e => e + 1);
    }
  },
  watch: {
    currentPage(newValue) {
      this.listConfig.filters.offset = (newValue - 1) * this.itemsPerPage;
      this.fetchEntries();
    },
    type() {
      this.resetPagination();
      this.fetchEntries();
    }
  },
  mounted() {
    this.fetchEntries();
  },
  methods: {
    fetchEntries() {
      this.isLoading = true;
      EnrtiesService.query(this.listConfig)
      .then(({ data }) => {
        this.entries = data;
      })
      .catch(error => {
        throw new Error(error);
      });
      this.isLoading = false
    },
    resetPagination() {
      this.listConfig.offset = 0;
      this.currentPage = 1;
    },
    addEntry() {
      this.entries.push({'date': new Date(), 'distance': 0, 'duration': 0, 'not_saved': true})
    },
    saveEntry(entry) {
      EnrtiesService.update(entry.id, entry).then(({ data }) => {
        entry = data;
      })
      .catch(error => {
        throw new Error(error);
      });
    },
    deleteEntry(entry) {
      EnrtiesService.destroy(entry.id)
      .then(() => {
        this.entries = this.entries.filter((v) => v!== entry);
      })
      .catch(error => {
        throw new Error(error);
      });
    }
  }
};
</script>