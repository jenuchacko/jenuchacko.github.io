# jenuchacko.github.io

Personal site of Jenu Varghese Chacko, built with Jekyll and the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme (pinned to 4.28.1 in `_config.yml`). GitHub builds and publishes it on every push to `main` through `.github/workflows/update-cv.yml`.

## Layout

```
_config.yml            site settings, sidebar profile and links
_data/navigation.yml   top menu (Research · Interactive · CV)
_data/news.yml         news items on the home page (newest first)
index.md               home page
cv.md                  CV (plain Markdown; has a Print / save PDF button)
research.md            research index (cards built from _research/)
_research/*.md         one page per research theme; `order:` sets card order
interactive/index.md   widget gallery
interactive/*.html     self-contained widgets (no front matter)
assets/css/main.scss   colours and small style additions
assets/images/         profile photo and card images
```

## Common edits

- **CV:** edit `cv.md` on GitHub (pencil icon) and commit. Keep sections in reverse chronological order.
- **News:** add an entry at the top of `_data/news.yml`.
- **Research theme:** copy a file in `_research/`, change `title`, `excerpt`, `order` and `header.teaser`.
- **Widget:** add a self-contained `.html` file to `interactive/` (no front matter, so Jekyll copies it untouched), then add a card to `feature_row` in `interactive/index.md`.

## Preview locally (optional)

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Switching over from the old single-page site

1. Delete `index.html`, `build.py`, `template.html` and `.nojekyll` from the repository (the new home page is `index.md`).
2. Upload or commit everything in this folder, including the hidden `.github` folder.
3. **Settings → Pages → Build and deployment** should stay on **GitHub Actions**. Watch the **Actions** tab for the "Build and deploy site" run.
