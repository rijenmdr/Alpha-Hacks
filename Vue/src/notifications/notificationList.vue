<template>
  <div class="notifications-list">
    <NotificationMessage
      v-for="notification in getNotifications"
      :key="notification.key"
      :notification="notification"
    />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import NotificationMessage from "./notificationMessage";
export default {
  data() {
    return {};
  },
  components: {
    NotificationMessage
  },
  computed: mapGetters(['getNotifications']),

  created() {
  }
};
</script>
<style scoped>
.notifications-list {
  position: fixed;
  bottom: 0;
  right: 0;
  margin-right: 15px;
  width: 320px;
}
</style>