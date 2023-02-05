<!-- Generate a sample svelte component that says hello world -->
<script>
  export let title = "LofiKit";
  let num = Math.floor(Math.random() * 8) + 1;
  let path = `/assets/background/${num}.jpg`;
  let imageToPreload = `/assets/background/${num}.jpg`;

  function changeBackground() {
    // Rotate the button until the image is loaded
    document.getElementById("changeBackground").classList.add("rotate-180");

    setTimeout(() => {
      document
        .getElementById("changeBackground")
        .classList.remove("rotate-180");
    }, 450);

    while (path === `/assets/background/${num}.jpg`) {
      num = Math.floor(Math.random() * 8) + 1;
    }
    imageToPreload = `/assets/background/${num}.jpg`;
    setTimeout(() => {
      path = `/assets/background/${num}.jpg`;
    }, 450);
  }
</script>

<link rel="preload" href={imageToPreload} as="image" />

<div
  id="background"
  class="h-screen w-screen bg-cover bg-center relative z-0 overflow-clip brightness-[.25]"
  style="background-image: url({path});"
/>

<button
  id="changeBackground"
  class="absolute top-0 left-0 m-5 scale-125 hover:scale-110  font-semibold text-white text-lg md:text-xl opacity-75 transition-all duration-200"
  on:click={changeBackground}
>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="1em"
    height="1em"
    viewBox="0 0 24 24"
    ><path
      fill="currentColor"
      d="m12.05 19l2.85-2.825l-2.85-2.825L11 14.4l1.075 1.075q-.7.025-1.362-.225q-.663-.25-1.188-.775q-.5-.5-.763-1.15q-.262-.65-.262-1.3q0-.425.113-.85q.112-.425.312-.825l-1.1-1.1q-.425.625-.625 1.325T7 12q0 .95.375 1.875t1.1 1.65q.725.725 1.625 1.088q.9.362 1.85.387l-.95.95Zm4.125-4.25q.425-.625.625-1.325T17 12q0-.95-.362-1.888q-.363-.937-1.088-1.662q-.725-.725-1.637-1.075q-.913-.35-1.863-.35L13 6.05L11.95 5L9.1 7.825l2.85 2.825L13 9.6l-1.1-1.1q.675 0 1.375.262q.7.263 1.2.763t.763 1.15q.262.65.262 1.3q0 .425-.113.85q-.112.425-.312.825ZM12 22q-2.075 0-3.9-.788q-1.825-.787-3.175-2.137q-1.35-1.35-2.137-3.175Q2 14.075 2 12t.788-3.9q.787-1.825 2.137-3.175q1.35-1.35 3.175-2.138Q9.925 2 12 2t3.9.787q1.825.788 3.175 2.138q1.35 1.35 2.137 3.175Q22 9.925 22 12t-.788 3.9q-.787 1.825-2.137 3.175q-1.35 1.35-3.175 2.137Q14.075 22 12 22Zm0-2q3.35 0 5.675-2.325Q20 15.35 20 12q0-3.35-2.325-5.675Q15.35 4 12 4Q8.65 4 6.325 6.325Q4 8.65 4 12q0 3.35 2.325 5.675Q8.65 20 12 20Zm0-8Z"
    /></svg
  >
</button>

<div class="text-gray-100 absolute flex justify-center flex-col h-screen">
  <div class="m-auto">
    <h1 class="font-bold text-4xl md:text-6xl">
      Welcome to <span
        class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"
        >{title}</span
      >
      <h3 class="font-bold text-xl md:text-3xl text-center">
        Relax, work, or study to <span
          class="text-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"
          >lofi</span
        >.
      </h3>
    </h1>
    <div class="flex justify-center">
      <a
        href="/play"
        rel="prefetch"
        class="transition mt-5 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 hover:scale-110  font-semibold text-white py-2 px-4 border rounded text-md md:text-lg"
      >
        Start Listening
      </a>
    </div>
  </div>
</div>
