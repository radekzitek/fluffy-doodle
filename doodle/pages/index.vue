<template>
  <div>
    <h1>Welcome to the homepage</h1>
    <AppAlert> This is an auto-imported component </AppAlert>
  </div>
  <div>
    <p>Count: {{ counter }}</p>
    <button @click="handleClick">Increment</button>
  </div>
  <div>
    <NuxtLink to="/about">About</NuxtLink>
  </div>
</template>

<script setup lang="ts">
const counter = ref(0);
const handleClick = () => {
  counter.value++;
};
</script>

<style scoped>
h1 {
  color: red;
}
</style>
