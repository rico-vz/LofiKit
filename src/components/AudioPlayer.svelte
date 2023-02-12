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

<select on:change={handleGenreSelection}>
  {#each genres as genre}
    <option value={genre} selected={selectedGenre === genre}>{genre}</option>
  {/each}
</select>

<audio src={currentSong} autoplay loop bind:volume />

<p>Music volume:</p>
<input
  type="range"
  min="0"
  max="1"
  step="0.01"
  value={volume}
  on:input={handleVolumeChange}
/>

<button on:click={handleNextSong}>Next song</button>

{#each effects as effect}
  <audio
    src={`${effect}`}
    loop
    bind:volume={effectVolumes[effect].volume}
    bind:paused={effectVolumes[effect].paused}
  />

  <p>{effect} volume:</p>
  <input
    type="range"
    min="0"
    max="1"
    step="0.01"
    value={effectVolumes[effect].volume}
    on:input={handleEffectVolumeChange(effect)}
  />
{/each}
