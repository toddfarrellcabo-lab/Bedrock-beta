# Bedrock Vault — Upload-ready site

This is the complete Bedrock website, with the existing Slate, Dock, Quarry, cart and Vault demo files.

## Add your assets
1. Unzip the website. Put your logos, PDFs, InDesign files, Illustrator files, Photoshop files, images, or templates into the relevant folder under `vault/files/`.
2. Run `update-vault-catalog.bat` on Windows (requires Python 3), or run `python update-vault-catalog.py` in a terminal.
3. Open `index.html` with a local web server or publish to GitHub Pages. The Vault catalog lists the files and provides links to preview/download them.
4. Upload the **contents** of this directory to the root of the GitHub repository, preserving all subfolders, including the updated `vault/catalog.js`.

**Important:** GitHub Pages cannot discover files in folders automatically. The catalog-generation step is required whenever you add/remove files. Files added without updating the catalog will exist online but won't appear in the Vault list.

**Notes:** SVG, JPG, PNG, WebP and PDF are browser-previewable. Adobe native files download for editing. This demo is public on GitHub Pages, so do not upload confidential brand assets or restricted documents to a public repository. Empty directories do not persist on GitHub; the included README.txt files keep them present. If the repo is public, everyone can access the files regardless of the site's role selector.
