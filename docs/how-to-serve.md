# Previewing the site locally

Jekyll turns the Markdown, `_data/*.yml` and the Minimal Mistakes theme into plain HTML in `_site/`. GitHub does the same on every push to `main` (see `.github/workflows/update-cv.yml`). Locally you run the same build and a small web server so you can check changes before pushing.

The `Gemfile` installs the `github-pages` gem, which pins the same Jekyll version GitHub uses. The first build downloads the theme, so you need an internet connection.

Pick one of the two routes below. WSL is usually less trouble.

## Option A: WSL (Ubuntu inside Windows)

**One time**

In PowerShell, check for an Ubuntu install:

```powershell
wsl -l -v
```

If none is listed, install one, restart if asked, and set a username and password:

```powershell
wsl --install -d Ubuntu
```

Open Ubuntu (type `wsl` in PowerShell) and install Ruby:

```bash
sudo apt update && sudo apt install -y ruby-full build-essential zlib1g-dev git
sudo gem install bundler
```

Go to the repo. Your C: drive is under `/mnt/c`:

```bash
cd /mnt/c/Users/<you>/<path>/jenuchacko.github.io
bundle config set --local path vendor/bundle
bundle install
```

**Each time**

```bash
bundle exec jekyll serve --livereload --force_polling
```

Open http://localhost:4000 in your Windows browser. `--force_polling` makes Jekyll notice edits made from Windows editors to files under `/mnt/c`.

Or start it straight from PowerShell:

```powershell
wsl -e bash -lc "cd /mnt/c/Users/<you>/<path>/jenuchacko.github.io && bundle exec jekyll serve --livereload --force_polling"
```

## Option B: native Windows (PowerShell)

**One time**

Install Ruby 3.3 with the DevKit. The GitHub Pages gems are known to work on 3.3.

```powershell
winget install -e --id RubyInstallerTeam.RubyWithDevKit.3.3
```

Open a new PowerShell window, then install the compiler toolchain. When asked, type `3` and press Enter.

```powershell
ridk install
ruby -v            # should report 3.3.x
gem install bundler
```

Install the site's gems from the repo folder (the one containing `_config.yml`):

```powershell
cd C:\Users\<you>\<path>\jenuchacko.github.io
bundle config set --local path vendor/bundle
bundle install
```

**Each time**

```powershell
chcp 65001         # UTF-8 console; the theme's Sass fails on non-ASCII characters without it
bundle exec jekyll serve --livereload
```

Open http://localhost:4000.

## Working with the preview

- Edits to `.md` files, `_data/*.yml` and `assets/css/main.scss` rebuild automatically and the browser reloads.
- Changes to `_config.yml` need a restart: Ctrl+C, then run the serve command again.
- `interactive/*.html` pages are copied unchanged. You can also open them directly by double-clicking, with no build.
- `_site/`, `vendor/` and the caches are in `.gitignore`; don't commit them.

## Troubleshooting

- **`bundle install` fails while compiling a gem.** On WSL this is usually a missing system library; the error names it, and `sudo apt install lib<name>-dev` fixes it. On Windows, rerun `ridk install` and choose 3.
- **`--livereload` errors on Windows.** Drop the flag and refresh the browser by hand.
- **`Invalid US-ASCII character` from Sass.** Run `chcp 65001` first (Windows), or `export LANG=C.UTF-8` (WSL).
- **Port 4000 is busy.** Add `--port 4001`.
