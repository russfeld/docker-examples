<script setup>
import { ref } from 'vue';
const users = ref(null);
fetch('http://localhost:5001/users')
    .then(response => response.json())
    .then(data => users.value = data);
</script>

<template>
  <ul>
    <li v-for="user in users">{{ user.name }} ({{  user.eid }})</li>
  </ul>
</template>
