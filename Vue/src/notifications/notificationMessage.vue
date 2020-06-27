<template>
  <div :class="typeClass" class="alert alert-dismissible fade show custom" role="alert">
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span arial-hidden="true">&times;</span>
    </button>
    {{notification.message}}
  </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
  props: ["notification"],
  data() {
    return {
      timeOut: null
    };
  },
  computed: {
    typeClass() {
      return `alert-${this.notification.type}`;
    }
  },
  created() {
    this.timeOut = setTimeout(() => {
      this.removeNotifi(this.notification);
    }, 3000);
  },
  methods:{
    removeNotifi(notification){
        this.$store.dispatch('removeNotifications',notification)
    }
  },
  beforDestroy() {
    clearTimeout(this.timeOut);
  }
};
</script>
<style scoped>
  .custom{
    z-index: 100;
  }
</style>