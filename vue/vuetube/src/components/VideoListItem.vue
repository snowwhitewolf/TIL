<template>
  <div @click="selectVideo">
    <hr>
    <img :src="videoItem.snippet.thumbnails.default.url" alt="썸네일">
    <p>{{ videoItem.snippet.title | unescapTitle }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    videoItem: Object,
  },
  filters: {
    unescapTitle: function (title) {
      return _.unescape(title)
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('selected', this.videoItem)
    }
  }
}
</script>

<style>

</style>