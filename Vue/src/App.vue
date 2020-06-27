<template>
  <div id="app">
    <main>
      <router-view />
    </main>
    <NotificationList />
  </div>
</template>
<script>
import NotificationList from "./notifications/notificationList";
export default {
  components: {
    NotificationList
  }
};
</script>
