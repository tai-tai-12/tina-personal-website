# Deployment Guide — Tina Tai Personal Website V2

## Recommended stack

- Source control: GitHub
- Static site generator: Hugo
- Hosting: GitHub Pages
- Planned domain: tinatai.com
- Cost before buying the domain: $0

## Part 1 — Publish the site first on GitHub Pages

### 1. Create the GitHub repository

Create a new repository on GitHub. Recommended name:

`personal-website`

For GitHub Free, make it **Public** so GitHub Pages is available without a paid plan.

Do not initialize it with a README, license, or .gitignore because those files already exist in this package.

### 2. Put this V2 folder into GitHub

#### Easiest on Mac: GitHub Desktop

1. Unzip `Tina_Tai_Personal_Website_V2_Deployment.zip`.
2. Install/open GitHub Desktop and sign in.
3. Choose **File → Add Local Repository** and select the unzipped `tina-personal-website-v2` folder.
4. If GitHub Desktop says the folder is not a Git repository, choose **create a repository here**.
5. Repository name: `personal-website`.
6. Commit all files with a message such as `Initial V2 website`.
7. Click **Publish repository** and publish it to your GitHub account.

#### Terminal alternative

```bash
cd /path/to/tina-personal-website-v2
git init
git add .
git commit -m "Initial V2 website"
git branch -M main
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/personal-website.git
git push -u origin main
```

### 3. Enable GitHub Pages

In the repository:

1. Open **Settings**.
2. In the left sidebar choose **Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. No branch folder needs to be selected.

The workflow in `.github/workflows/hugo.yaml` will handle the build and deploy.

### 4. Watch the deployment

1. Open the repository's **Actions** tab.
2. Open the latest `Build and deploy` run.
3. Wait until both the build and deploy jobs are green.
4. Open the deployment URL shown by GitHub.

From then on, every push to the `main` branch automatically rebuilds the site.

## Part 2 — Test locally before pushing changes

On macOS:

```bash
brew install hugo
cd /path/to/tina-personal-website-v2
hugo server -D
```

Open:

`http://localhost:1313`

Stop the server with `Control + C`.

You do not need to manually build or upload the `/public` folder. GitHub Actions does that for you.

## Part 3 — Connect tinatai.com after you buy it

You can deploy the GitHub Pages version first and add the domain later.

### 1. Buy `tinatai.com`

Buy it from any reputable domain registrar. Keep DNS management enabled at the registrar or DNS provider.

### 2. Add the custom domain in GitHub

Repository → **Settings → Pages → Custom domain** → enter:

`tinatai.com`

Save it.

### 3. Configure DNS

For the apex domain `tinatai.com`, create these four A records:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

For `www.tinatai.com`, create:

| Type | Name | Value |
|---|---|---|
| CNAME | www | YOUR-GITHUB-USERNAME.github.io |

Do not point the CNAME to the repository path. Use only `YOUR-GITHUB-USERNAME.github.io`.

GitHub also supports IPv6 AAAA records, but the four A records above are enough for a straightforward setup.

### 4. Wait for DNS and HTTPS

DNS can take time to propagate. GitHub will run a DNS check and provision an HTTPS certificate automatically after the custom domain is configured correctly.

When available, enable:

**Settings → Pages → Enforce HTTPS**

### 5. Recommended: verify the domain in GitHub

In your GitHub account settings, verify your custom domain for GitHub Pages. GitHub will provide a TXT DNS record. Add that TXT record at your DNS provider, then return to GitHub and complete verification. This reduces the risk of domain takeover.

## Part 4 — Updating the website later

Recommended workflow:

1. Edit the files locally.
2. Run `hugo server -D` and review the site.
3. Commit the changes in GitHub Desktop.
4. Push to GitHub.
5. GitHub Actions automatically republishes the site.

If replacing the portrait, keep the file name:

`static/images/profile/tina-headshot.jpg`

If replacing the resume, keep the file name:

`static/resume/Shih-Ting_Tai_Resume.pdf`

Keeping those names means no code changes are required.

## Common problems

### The site is not deploying

Check **Actions** first. The failing step usually tells you exactly what failed.

### The site is deployed but CSS/images are missing

Do not hard-code the temporary `github.io` URL into templates. This package uses Hugo relative URL helpers and the Pages workflow supplies the correct deployment base URL.

### The custom domain works but HTTPS is unavailable

Wait for the GitHub DNS check and certificate provisioning. Also remove conflicting A/AAAA/ALIAS/ANAME records for the apex or conflicting CNAME records for `www`.

### Do I need a CNAME file in the repository?

No. This V2 deploys through a custom GitHub Actions workflow; GitHub's documentation states that a CNAME file is ignored and not required in that deployment mode.
