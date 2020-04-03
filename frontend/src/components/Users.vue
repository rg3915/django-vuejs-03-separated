<template>
  <div>
    <b-container>
      <b-table striped hover :items="users"></b-table>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'

const endpoint = 'http://localhost:8000/'

export default {
  data() {
    return {
      users: [
        // { 'username': 'huguinho' },
        // { 'username': 'zezinho' },
        // { 'username': 'luizinho' },
      ]
    }
  },
  created() {
    axios.get(endpoint + 'api/users/')
      .then(response => {
        this.users = response.data.data;
      })
  }
}
</script>