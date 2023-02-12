<script is:inline>
  import chillSongs from "./chillSongs.js";
  import jazzySongs from "./jazzySongs.js";
  import sleepySongs from "./sleepySongs.js";
  import effects from "./effects.js";

  let selectedGenre = "chill";
  let volume = 0.5;
  let effectVolumes = {};

  const genres = ["chill", "jazzy", "sleepy"];

  const songs = {
    chill: chillSongs,
    jazzy: jazzySongs,
    sleepy: sleepySongs,
  };

  function randomSong(genre) {
    return songs[genre][Math.floor(Math.random() * songs[genre].length)];
  }

  function handleGenreSelection(event) {
    selectedGenre = event.target.value;
    currentSong = randomSong(selectedGenre);
  }

  let currentSong = randomSong(selectedGenre);

  function handleVolumeChange(event) {
    volume = event.target.value;
  }

  function handleNextSong() {
    currentSong = randomSong(selectedGenre);
  }

  function handleEffectVolumeChange(effect) {
    return (event) => {
      effectVolumes[effect].volume = event.target.value;
      if (event.target.value > 0) {
        effectVolumes[effect].paused = false;
      } else {
        effectVolumes[effect].paused = true;
      }
    };
  }

  effects.forEach((effect) => {
    effectVolumes[effect] = {
      volume: 0,
      paused: true,
    };
  });

  let num = Math.floor(Math.random() * 18) + 1;
  let path = `/assets/background/${num}.jpg`;
  let imageToPreload = `/assets/background/${num}.jpg`;

  function changeBackground() {
    const changeBackgroundEl = document.getElementById("changeBackground");
    const backgroundEl = document.getElementById("background");

    changeBackgroundEl.classList.add("rotate-180");
    backgroundEl.classList.add("opacity-0");

    setTimeout(() => {
      changeBackgroundEl.classList.remove("rotate-180");
    }, 350);

    setTimeout(() => {
      while (num === parseInt(path.split("/")[3])) {
        num = Math.floor(Math.random() * 8) + 1;
      }

      path = `/assets/background/${num}.jpg`;
      imageToPreload = `/assets/background/${num}.jpg`;
      backgroundEl.classList.remove("opacity-0");
    }, 300);
  }
</script>

<link rel="preload" href={imageToPreload} as="image" />

<div
  id="background"
  class="h-screen w-screen bg-cover bg-center relative z-0 overflow-clip brightness-[.40] transition-all duration-500"
  style="background-image: url({path});"
/>

<div class="absolute w-full h-full text-white z-2">
  <button
    id="changeBackground"
    class="top-0 left-0 m-5 scale-125 hover:scale-110  font-semibold text-white text-lg md:text-xl opacity-75 transition-all duration-300"
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
  <div class="flex flex-col items-center mt-10">
    <div class="text-lg font-bold mb-3">Select a genre:</div>
    <select
      class="bg-white/20 backdrop-blur border focus:text-black text-white border-gray-400/40 rounded-lg p-2"
      on:change={handleGenreSelection}
    >
      {#each genres as genre}
        <option value={genre} selected={selectedGenre === genre}
          >{genre.charAt(0).toUpperCase() + genre.slice(1)}</option
        >
      {/each}
    </select>
  </div>

  <audio src={currentSong} autoplay loop bind:volume class="hidden" />

  <div class="flex flex-col items-center mt-10">
    <div class="text-lg font-bold mb-3">Music volume:</div>
    <input
      type="range"
      min="0"
      max="1"
      step="0.01"
      value={volume}
      on:input={handleVolumeChange}
      class="appearance-none h-2 w-64 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full"
    />
    <button
      class="transition mt-8 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 hover:scale-110  font-semibold text-white py-2 px-4 border rounded-lg text-md md:text-lg"
      on:click={handleNextSong}
    >
      Next song
    </button>
  </div>

  <div class="flex flex-col items-center mt-5">
    <div
      id="effectBox"
      class="mt-6 overflow-hidden hover:overflow-auto h-40 w-52 bg-white/[.10] rounded-lg before:blur-md hover:cursor-pointer shadow-lg backdrop-blur px-4 py-4 absolute"
    >
      <h3 class="mb-2">Effects</h3>
      {#each effects as effect}
        <audio
          src={`${effect}`}
          loop
          bind:volume={effectVolumes[effect].volume}
          bind:paused={effectVolumes[effect].paused}
        />

        <div class="mb-4">
          <p class="text-sm">
            {effect
              .split("/")
              .pop()
              .replace(/\.[^/.]+$/, "")
              .replace(/-|_/g, " ")
              .replace(/\b\w/g, (l) => l.toUpperCase())} volume:
          </p>
          <input
            type="range"
            class="appearance-none h-2 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 border-none outline-none w-full rounded-lg"
            min="0"
            max="1"
            step="0.01"
            value={effectVolumes[effect].volume}
            on:input={handleEffectVolumeChange(effect)}
          />
        </div>
      {/each}
    </div>
  </div>
</div>
