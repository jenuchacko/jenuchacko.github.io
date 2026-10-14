# Jenu Varghese Chacko CV website

A static website for https://jenuchacko.github.io with an editable CV and a printable view. No Python packages or web framework are needed.

## Review before publishing

This draft uses the supplied CV records through October 2025. Confirm the current appointment, public email, editorial roles and any newer work. Phone numbers, street address and personal email have been omitted. The supplied patent entry combines wording without patent identifiers; verify and split it into individual records if appropriate. The 2014 STED-AFM conference citation includes a 2012 journal reference in the source; confirm that date. Publication metadata and author contributions have been retained from the source rather than independently verified. Add confirmed Scholar and ORCID URLs when available.

## Publish using the GitHub website

1. Sign in with your existing `jenuc` account and open https://github.com/jenuchacko and check whether a repository named `jenuchacko.github.io` already exists. If it exists, inspect and back it up before replacing files.
2. If absent, create a public repository named exactly `jenuchacko.github.io`, owned by the `jenuchacko` organization. Initialize it with a README so the main branch exists.
3. Extract the ZIP. In the repository choose **Add file â†’ Upload files**. Upload the contents of this folder, not the enclosing folder. `index.html` must be at the repository root. Commit to `main`.
4. The `.github` folder and `.nojekyll` file may be hidden or skipped by drag-and-drop. For automatic rebuilding, use **Add file â†’ Create new file**, name it `.github/workflows/update-cv.yml`, and paste the matching local workflow contents. Create an empty `.nojekyll` file at the root if it did not upload. The initial static site still works without the rebuild workflow.
5. Open **Settings â†’ Pages â†’ Build and deployment**. Choose **GitHub Actions** as the source. Open the Actions tab and run **Publish CV** if a deployment has not started.
6. Wait for deployment; GitHub says changes can take up to 10 minutes. Open https://jenuchacko.github.io. Check the mobile view, contact email, publication text and print output.

## Update the running CV

Open `cv.md` in GitHub, click the pencil, edit and commit to `main`. The Rebuild CV action regenerates `index.html` and commits it. GitHub Pages then publishes it. If the action fails because repository policies prevent writing, run `python build.py` locally and upload the resulting `index.html` alongside the updated `cv.md`. No packages are required.

Keep appointments and publications in reverse chronological order. Add new work as it happens and update the content date in `template.html` after reviewing the CV. Edit `template.html` for colors, layout or contact navigation; edit `cv.md` for content. The print button opens your browser's print dialog, where you can save a PDF.

The site is public when deployed. Git history preserves earlier versions of committed content. Keep private working notes outside the repository.

Official instructions: https://docs.github.com/en/pages/quickstart
