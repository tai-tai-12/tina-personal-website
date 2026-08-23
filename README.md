# Tina Tai — Personal Website V2

A bilingual Hugo portfolio built for recruiting and long-term personal branding.

## Positioning

**Product & Analytics**  
**AI × Healthcare**  
Turning complex problems into products, insights, and real-world impact.

## V2 design direction

- Recruiter-first hierarchy: Product & Analytics is the primary identity; AI × Healthcare is the specialization.
- Light mode default + dark mode toggle.
- Black / white / deep-blue palette with restrained electric-blue interaction details.
- Sans-serif only: Inter + Noto Sans TC.
- Medium professional portrait: visible enough to be memorable, but secondary to positioning and work.
- Three featured case-study cards with abstract public-safe visuals that can later be replaced with real project imagery.
- English primary + Traditional Chinese.
- Writing remains built in but intentionally hidden from the main navigation until there are strong posts to publish.

## Deployment-ready

This package includes a GitHub Pages workflow at `.github/workflows/hugo.yaml`. After the repository is pushed to GitHub, set **Settings → Pages → Source → GitHub Actions**. Every push to `main` will then rebuild and deploy the site automatically.

See `docs/DEPLOYMENT_GUIDE.md` for the exact steps.

## Local preview on Mac

```bash
brew install hugo
hugo server -D
```

Open `http://localhost:1313`.

The site also contains a static browser preview under `preview/` for quick viewing without Hugo.

## CareerCanvas

The project retains CareerCanvas as the upstream Hugo theme identity, while the custom layouts and CSS in this repository override the visual presentation. The bundled theme folder is an offline placeholder so the repository can build without a network-time theme fetch. `setup-theme.sh` can replace it with the official upstream CareerCanvas repository when desired.

## Before launch

Review `docs/PRELAUNCH_CHECKLIST.md` and `docs/ASSETS_NEEDED.md`.
