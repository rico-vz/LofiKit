<script is:inline>
  import chillSongs from "./chillSongs.js";
  import jazzySongs from "./jazzySongs.js";
  import sleepySongs from "./sleepySongs.js";
  import effects from "./effects.js";

  let selectedGenre = "chill";
  let volume = 1;
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
    console.log(effect);
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
</script>

<div class="flex flex-col items-center mt-10">
  <div class="text-lg font-bold mb-3">Select a genre:</div>
  <select
    class="bg-white border border-gray-400 rounded p-2"
    on:change={handleGenreSelection}
  >
    {#each genres as genre}
      <option value={genre} selected={selectedGenre === genre}>{genre}</option>
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
    class="w-64"
  />
</div>

<button
  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 mt-10 rounded"
  on:click={handleNextSong}
>
  Next song
</button>

{#each effects as effect}
  <audio
    src={`${effect}`}
    loop
    bind:volume={effectVolumes[effect].volume}
    bind:paused={effectVolumes[effect].paused}
    class="hidden"
  />

  <div class="flex flex-col items-center mt-10">
    <div class="text-lg font-bold mb-3">{effect} volume:</div>
    <input
      type="range"
      min="0"
      max="1"
      step="0.01"
      value={effectVolumes[effect].volume}
      on:input={handleEffectVolumeChange(effect)}
      class="w-64"
    />
  </div>
{/each}
