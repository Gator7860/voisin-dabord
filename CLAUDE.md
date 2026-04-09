# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

**Voisin D'abord** is a static HTML website for a French home services business (baby-sitting, pet-sitting, gardening, pressure washing, car cleaning, gutter cleaning) in the Yvelines region (78). Hosted on GitHub Pages at `voisindabord.fr`.

No build system, no package manager, no framework — pure HTML/CSS/JS.

## Development

Open any `.html` file directly in a browser, or use a local server:

```bash
python -m http.server 8080
# or
npx serve .
```

To deploy: push to `main` — GitHub Pages serves automatically via the `CNAME` (voisindabord.fr).

## Architecture

Five pages, each self-contained:
- `index.html` — homepage (hero, services grid, tax credit banner, how-it-works, Leaflet map, CTA)
- `services.html` — detailed service pages with anchor links (`#baby`, `#pet`, `#jardin`, `#karcher`, `#voiture`, `#gouttieres`)
- `a-propos.html` — about page
- `contact.html` — contact form
- `mentions-legales.html` — legal notices

**Important:** Each HTML file contains its own `<style>` block as the active design system. `style.css` is an older/alternate stylesheet that is **not linked** from any current page — do not use it as the style reference.

## Design system (inline `<style>` in each HTML file)

Fonts: `Fraunces` (serif headings, italic accents) + `DM Sans` (body text) from Google Fonts.

CSS variables:
```css
--vert: #2d5a27        /* primary green */
--vert-clair: #4a8c3f  /* lighter green (hover states) */
--vert-pale: #e8f0e6   /* green tint background */
--creme: #f8f5ee       /* warm off-white sections */
--brun: #3b2f20        /* dark brown (headings) */
--brun-mid: #7a6550    /* medium brown (body text) */
--brun-pale: #ece5d8   /* light brown borders */
--blanc: #fdfcf9       /* near-white background */
```

The Leaflet.js interactive map (`index.html`) uses CDN-loaded Leaflet 1.9.4 with CartoDB light tiles, a polygon for CC Gally Mauldre coverage zone, and custom div icons for city markers.

## Content language

All user-facing content is in **French**. Keep any new copy in French.
