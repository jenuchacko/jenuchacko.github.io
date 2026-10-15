# Handoff: jenuchacko.github.io redesign

Context for continuing this work in Claude Code. Read this first, then `README.md` and `docs/how-to-serve.md`.

## Goal

Replace the old single-page CV site with a Jekyll site on the Minimal Mistakes theme:

- a simple home page (bio, three cards, news),
- **Research**: one page per research theme,
- **Interactive**: self-contained teaching widgets, starting with the FLIM decay ↔ phasor explorer,
- **CV**: the existing CV content, printable.

Layout inspiration: Vicidomini Lab site (research cards), Christoph Gohlke's site (categorized software list), PhasorPy (thumbnail gallery), and LOCI's interactive-microscopy-courseware (single-file widgets with "why this matters" text, a live widget and a readout).

## Repository

- GitHub: `jenuchacko/jenuchacko.github.io` (owner is the `jenuchacko` organization; Jenu's account is `jenuc` / `JenuC`).
- Live site: https://jenuchacko.github.io
- Deploys with GitHub Actions on push to `main` (`.github/workflows/update-cv.yml` → `actions/jekyll-build-pages` → `actions/deploy-pages`). Pages source is already set to GitHub Actions.
- As of 2026-10-15 the remote `main` is still the old site at commit `ff43cc3` (files: `index.html`, `build.py`, `template.html`, `cv.md`, `profile.jpg`, `.nojekyll`, workflow).

## Status

Done (in this folder, not yet committed to GitHub):

- Full scaffold: `_config.yml` (theme pinned `mmistakes/minimal-mistakes@4.28.1`, sidebar profile, `research` collection), `_data/navigation.yml`, `_data/news.yml`, `index.md`, `cv.md`, `research.md`, four `_research/*.md` pages, `interactive/index.md`, `assets/css/main.scss` (old site's teal/paper palette, print styles for the CV), SVG card images in `assets/images/teasers/`, 400 px profile crop in `assets/images/profile.jpg`.
- `interactive/phasor-explorer.html`: self-contained, no front matter, so Jekyll copies it unchanged. Three sections: two-component decay ↔ phasor with draggable points; repetition rate, harmonics and wraparound; Monte Carlo photon cloud with background. Light and dark mode, phone layout, keyboard and touch tested.
- Verified in the cloud session: built with Jekyll 3.10 + Minimal Mistakes 4.28.1 (same as GitHub Pages), no broken internal links, CV prints to 4 Letter pages, widget math checked against numerical integration and simulation.
- `docs/how-to-serve.md`: local preview on WSL and native PowerShell.
- `_research/automated-microscopy.md` rewritten with SmartPath, QPSC and DReAMS (from the public READMEs of `uw-loci/smart-wsi-scanner`, `uw-loci/QPSC`, `uw-loci/dreams`).
- `.gitignore`, and `tzinfo-data` added to `Gemfile` for Windows.

## Next steps

1. **Put the files in the repo.** In a clone of `jenuchacko/jenuchacko.github.io`, delete everything except `.git`, copy in this folder's contents (including `.github/` and `docs/`), so `_config.yml` sits at the repo root. Work on a branch, e.g. `redesign`. The workflow only deploys from `main`.
2. **Preview locally** following `docs/how-to-serve.md` (WSL or PowerShell; the machine is Windows). Check home, Research, each research page, Interactive, the widget, CV, and CV print preview.
3. **Review content Jenu hasn't approved yet:**
   - the four `_research/*.md` pages (draft text marked `<!-- TODO -->`), especially the new SmartPath / QPSC / DReAMS sections;
   - `_data/news.yml` (bioRxiv 2026 preprint, QUAREP-LiMi ERB role);
   - `index.md` card blurbs.
4. **Merge to `main`** and watch the "Build and deploy site" run in the Actions tab.
5. **Optional follow-ups discussed:**
   - Software section (Gohlke style): FLIM analysis (flimj-ops, PhasorKit), microscope control (QPSC, DReAMS, SmartPath), file I/O (sdt writer), simulation.
   - More widgets: photon-budget / lifetime-precision calculator, ISM pixel-reassignment demo, instrument tours with clickable photos; consider contributing FLIM pages to `uw-loci/interactive-microscopy-courseware`.
   - Before/after drag slider for images (intensity vs FLIM, confocal vs ISM).
   - GitHub profile README for `JenuC` linking back to the site; pin more repos.
   - Add real figures to research pages.

## Conventions

- New research theme: copy a `_research/*.md`, set `title`, `excerpt`, `order`, `header.teaser`.
- New widget: drop a self-contained `.html` (no front matter) in `interactive/`, add a teaser SVG, add a `feature_row` entry in `interactive/index.md`. Keep the thin top bar linking back to `../` and `./`, the CSS colour tokens, and dark-mode support.
- If a widget ever gets front matter (to use the site layout), wrap its script in `{% raw %}…{% endraw %}` and scope its CSS.
- News: newest first in `_data/news.yml`; home shows four.
- `docs/` is excluded from the published site.

## Gotchas

- The old root files (`index.html`, `build.py`, `template.html`) are listed in `exclude`, so leftovers can't override the new home page; still delete them and `.nojekyll`.
- Native Windows: run `chcp 65001` before `jekyll serve`, or Sass fails on UTF-8.
- WSL serving from `/mnt/c`: use `--force_polling` so edits from Windows are picked up.
- The theme loads Font Awesome from jsDelivr; offline previews show the sidebar links without icons.
