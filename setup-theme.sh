#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
rm -rf themes/careercanvas
mkdir -p themes
git clone --depth 1 https://github.com/felipecordero/careercanvas.git themes/careercanvas
printf '\nOfficial CareerCanvas installed. Your custom layouts/CSS remain in the project root and will continue to override the theme.\n'
