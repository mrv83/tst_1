<template>
  <div class="home-page">
      <h1>V2 - Report page</h1>
      <p>You need to create a Django project, that should meet the following requirements</p>
      <ul>
          <li>Anonymous User can only access README page and login or registration forms</li>
          <li>User can create, delete or see list of his own entries only</li>
          <li>To create an entry user provide this data:
              <ul>
                  <li>date</li>
                  <li>distance</li>
                  <li>duration</li>
              </ul>
          </li>
          <li>When user see list of entries, application also shows average speed</li>
          <li>User should be able to filter list of entries by date range</li>
          <li>There should be a page with per-week statistics for last year - week number, total amount of entries, total distance, total duration and weekly average speed.</li>
          <li>Minimal front-end design required. You may use some free templates, also you should use some layout framework for frontend like bootstrap. You may use default color scheme. But application response should not be plain-text, add (sticky) header and footer, tables and lists when appropriate.</li>
      </ul>

      <p>
          These are the minimal task set for application. If you have more time and want to show more skills you can implement bonus tasks. They are optional and you can pick any of them in different order.
      </p>
      <h2>
          Bonus tasks
      </h2>
      <ul>
          <li>
              Prepare settings.py configuration to be used in different environments (e.g. local, dev server, prod server). Sensible data like passwords, secrets, api keys should not be committed to git
          </li>
          <li>Add managers accounts. The permissions should work like this:
              <ul>
                  <li>User - Can only manage own entries</li>
                  <li>Manager - Can create users, activate and deactivate them, or reset user’s password. But manager can not access user data.</li>
                  <li>Admin - Can manage users as managers, and also can see all users’ data and create entries on behalf of other user</li>
              </ul>
          </li>
          <li>Unit Test coverage</li>
          <li>Provide deployment instructions & configuration</li>
          <li>Integrate social login (Facebook, Google, any other OAuth provider of your choice)</li>
          <li>Do the task as separate backend and frontend applications. Backend should provide REST or RPC API
              <ul>
                  <li>Never reload the front-end page, even for authentication</li>
              </ul>
          </li>
          <li>Management command (or another background task, e.g. celery) to email a user his yearly statistic</li>
          <li>Prepare static files collection for production - this may include
              <ul>
                  <li>minifying</li>
                  <li>merging JS or CSS files to single file</li>
                  <li>add hash to file names for browser cache</li>
              </ul>
          </li>
      </ul>
  </div>
</template>

<script>
export default {
  name: "readme",
  components: {
  },
  mounted() {
  },
  computed: {
  }
};
</script>