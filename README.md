# Lofi Kit
### Relax, work, or study to lofi.
The FOSS solution to just staying calm.

## 🚀 Project Structure

Inside of LofiKit, you'll see the following folders:

```
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── 
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
└── package.json
```

LofiKit looks for `.astro`, `.md` or `.svelte` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro or Svelte components.

Any static assets, like images, songs or effects , can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                | Action                                           |
| :--------------------- | :----------------------------------------------- |
| `npm install`          | Installs dependencies                            |
| `npm run dev`          | Starts local dev server at `localhost:3000`      |
| `npm run build`        | Build your production site to `./dist/`          |
| `npm run preview`      | Preview your build locally, before deploying     |
| `npm run astro ...`    | Run CLI commands like `astro add`, `astro check` |
| `npm run astro --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more

Feel free to check [Astro's documentation](https://docs.astro.build) or jump into their [Discord server](https://astro.build/chat).
