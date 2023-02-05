import { defineConfig } from 'astro/config';

// https://astro.build/config
import svelte from "@astrojs/svelte";

// https://astro.build/config

// https://astro.build/config
import vercel from "@astrojs/vercel/serverless";

// https://astro.build/config
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
import prefetch from "@astrojs/prefetch";

// https://astro.build/config
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  integrations: [svelte(), tailwind(), prefetch(), sitemap()],
  output: "server",
  adapter: vercel()
});