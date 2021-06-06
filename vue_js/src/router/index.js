import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      component: () => import("@/views/Home"),
      meta: {requiresAuth: true},
      // children: [
      //   {
      //     path: "",
      //     name: "home",
      //     component: () => import("@/views/HomeGlobal")
      //   }
      //   ]
        // {
        //   path: "my-feed",
        //   name: "home-my-feed",
        //   component: () => import("@/views/HomeMyFeed")
        // },
        // {
        //   path: "tag/:tag",
        //   name: "home-tag",
        //   component: () => import("@/views/HomeTag")
        // }
      // ]
    },
    {
      name: "login",
      path: "/login",
      component: () => import("@/views/Login")
    },
  {
      name: "logout",
      path: "/logout",
      component: () => import("@/views/Login")
    },
    {
      name: "register",
      path: "/register",
      component: () => import("@/views/Register")
    },
      {
      name: "readme",
      path: "/readme",
      component: () => import("@/views/ReadMe")
    },
    // {
    //   name: "settings",
    //   path: "/settings",
    //   component: () => import("@/views/Settings")
    // },
    // Handle child routes with a default, by giving the name to the
    // child.
    // SO: https://github.com/vuejs/vue-router/issues/777
    // {
    //   path: "/@:username",
    //   component: () => import("@/views/Profile"),
    //   children: [
    //     {
    //       path: "",
    //       name: "profile",
    //       component: () => import("@/views/ProfileEntries")
    //     },
    //     {
    //       name: "profile-favorites",
    //       path: "favorites",
    //       component: () => import("@/views/ProfileFavorited")
    //     }
    //   ]
    // },
    // {
    //   name: "entry",
    //   path: "/entries/:id",
    //   component: () => import("@/views/Entry"),
    //   props: true
    // },
    // {
    //   name: "entry-edit",
    //   path: "/editor/:id?",
    //   props: true,
    //   component: () => import("@/views/EntryEdit")
    // }
  ]
});