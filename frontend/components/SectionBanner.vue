<template>
  <div class="relative w-full mt-10 my-3" style="height: 63px">
    <!-- Group 88 緞帶兩端裝飾（底層） -->
    <img src="/images/logos/Group88.png" class="absolute inset-0 w-full h-full z-10" style="object-fit: fill" alt="" />
    <!-- 漸層色塊 + 文字 一起往上移 10px -->
    <div
      class="absolute inset-y-0 z-20 flex items-center justify-center"
      style="
        left: 10%;
        right: 10%;
        transform: translateY(-15px);
        border-radius: 10px;
        background: linear-gradient(90deg, #64cbaa 0%, #8bffda 50%, #64cbaa 100%);
      "
    >
      <span class="font-bold text-2xl sm:text-3xl md:text-4xl" style="color: #2a716d">
        <slot />
      </span>
    </div>
  </div>
</template>
