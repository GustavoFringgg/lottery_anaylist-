<template>
  <button class="date-btn">
    <slot />
  </button>
</template>

<style scoped>
.date-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 5px 10px;
  gap: 10px;
  font-size: 12px;
  background: #f9805a;
  border: 3px solid #ffffff;
  border-radius: 45px;
  font-weight: bold;
  color: white;
  cursor: pointer;
}

@media (min-width: 640px) {
  .date-btn {
    padding: 8px 20px;
    font-size: 18px;
    border: 4px solid #ffffff;
  }
}
</style>
