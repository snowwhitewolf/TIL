<template>
  <div>
    <div v-if="isShow">
      <iframe :src="videoUrl" frameborder="0"></iframe>
      <p>{{ selectItem.snippet.title | unescapTitle }}</p>
      <p>{{ selectItem.snippet.description | unescapTitle}}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    selectItem: Object,
  },
  filters: {
    unescapTitle: function (title) {
      return _.unescape(title)
    }
  },
  computed: {
    videoUrl: function () {
      if (_.isEmpty(this.selectItem)) {
        return ''
      } else {
        return `https://www.youtube.com/embed/${this.selectItem.id.videoId}`
      }
    },
    // 전달된 데이터가 없으면 디테일 페이지는 보여줄 필요 없음.
    isShow: function () {
      return !_.isEmpty(this.selectItem)
    }
  }
}
</script>

<style>

</style>