#!/usr/bin/env python3
"""V8.3 site source validation (run before Hugo build, no network access required)."""
from pathlib import Path
import re,sys,hashlib
try:
 import tinycss2
except ImportError:
 tinycss2=None
ROOT=Path(__file__).resolve().parents[1]
errors=[];checks=0

def check(ok,message):
 global checks
 checks+=1
 if not ok:errors.append(message)

for lang in ('en','zh'):
 content=list((ROOT/'content'/lang).rglob('*.md'))
 check(len(content)>=11,f'{lang}: incomplete content set ({len(content)})')
 for rel in ['work/medical-ai-product.md','work/clinical-ai-at-scale.md','work/structured-validation.md','research/thoracic-aorta.md']:
  check((ROOT/'content'/lang/rel).is_file(),f'{lang}: missing page {rel}')
 product=(ROOT/f'content/{lang}/work/medical-ai-product.md').read_text(encoding='utf-8')
 clinical=(ROOT/f'content/{lang}/work/clinical-ai-at-scale.md').read_text(encoding='utf-8')
 for needle in ['Future Tech Award','futuretech.org.tw','product-flow-phases-v82','LLM','case-boundary-v81']:
  check(needle in product,f'{lang}: product content missing {needle}')
 for needle in ['94.54','1,007','55','84.96','80.97','T1C-only','0.9416','0.9514','clinical-key-outcome-v82']:
  check(needle in clinical,f'{lang}: research evidence missing {needle}')
 check('clinical-reduction-v8' not in clinical,f'{lang}: redundant old chart remains')
 check(len(re.findall(r'<li><span>0[123] ·',product))==3, f'{lang}: product flow should have 3 readable phases')
 # case navigation IDs should have matching in-page anchored destinations
 for path in (ROOT/'content'/lang/'work').glob('*.md'):
  text=path.read_text(encoding='utf-8')
  front=text.split('---',2)
  if len(front)<3:continue
  for anchor in re.findall(r'(?m)^- id:\s*([^\s]+)',front[1]):
   check(f'id="{anchor}"' in text, f'{lang}: missing case anchor {path.name}#{anchor}')

head=(ROOT/'layouts/partials/head.html').read_text(encoding='utf-8')
base=(ROOT/'layouts/_default/baseof.html').read_text(encoding='utf-8')
check('content="8.3"' in head,'V8.3 metadata not updated')
check('data-portfolio-version="8.3"' in base,'V8.3 HTML version not updated')
check(head.count('css/portfolio-v83.css')==1,'Expected exactly one consolidated CSS link')
check(not any(f'css/{x}' in head for x in ['site.css','v8-refresh.css','v81-evidence.css']),'Legacy CSS still injected')
check((ROOT/'static/css/portfolio-v83.css').is_file(),'Consolidated CSS absent')
check(len(list((ROOT/'static/css').glob('*.css')))==1,'More than one public CSS file')
check((ROOT/'docs/legacy-styles/v81-evidence.css').is_file(),'Legacy CSS archive absent')
css=(ROOT/'static/css/portfolio-v83.css').read_text(encoding='utf-8')
for needle in ['--v82-type-section','--v82-reading','experience-v55-list .experience-v55-row','experience-recognition-v82','foundation-grid-v82','research-tile-v54','product-flow-phases-v82','max-width:480px']:
 check(needle in css,f'Design-system rule missing: {needle}')
if tinycss2 is not None:
 rules=tinycss2.parse_stylesheet(css,skip_comments=True,skip_whitespace=True)
 check(not any(x.type=='error' for x in rules),'Malformed consolidated CSS')
for needle in ['experience-recognition-v82','Future Tech Award','futuretech.org.tw']:
 check(needle in (ROOT/'layouts/experience/single.html').read_text(encoding='utf-8'),f'Experience award module missing {needle}')
home=(ROOT/'layouts/index.html').read_text(encoding='utf-8')
for needle in ['about-v82-editorial','project-recognition-v82','National Taiwan University Hospital','experience-v55-row','foundation-grid-v82']:
 check(needle in home,f'Home missing {needle}')
research=(ROOT/'layouts/research/list.html').read_text(encoding='utf-8')
check(research.index('research-v516-publications')<research.index('research-v518-feature'), 'Publication index should precede image-heavy research output cards')
check(research.index('research-v518-recognition')<research.index('research-v518-engineering'),'Recognition should precede methods appendix')
check('2026.midl.io/scientific-program' in research,'Missing official MIDL verification')
check('SELECTED RESEARCH SUPPORT' in research,'Research grants section absent')
check('credential.net/81142' in (ROOT/'layouts/education/single.html').read_text(encoding='utf-8'),'Google certification verification missing')

# Asset references: matching static relative URLs in all templates and markdown, plus CSS url()
files=list((ROOT/'layouts').rglob('*.html'))+list((ROOT/'content').rglob('*.md'))
for p in files:
 t=p.read_text(encoding='utf-8')
 for m in re.finditer(r'{{\s*"((?:images|resume|css|js|research/publications)/[^"\n]+)"\s*\|\s*(?:relURL|absURL)',t):
  check((ROOT/'static'/m.group(1)).is_file(),f'Broken referenced file: {p.relative_to(ROOT)} → {m.group(1)}')
 for m in re.finditer(r'{{<\s*site-img\s+src="([^"\n]+)"',t):
  check((ROOT/'static'/m.group(1)).is_file(),f'Broken image shortcode: {p.relative_to(ROOT)} → {m.group(1)}')

for f in ['thoracic-aorta-3d-results-v81.webp','thoracic-aorta-multiplanar-annotation-v81.webp']:
 check((ROOT/'static/images/research'/f).is_file(),f'Missing original research figure: {f}')
resume=ROOT/'static/resume/Shih-Ting_Tai_Resume.pdf'
check(resume.is_file() and resume.stat().st_size>50000,'Latest resume missing')
original=Path('/mnt/data/Shih-Ting_Tai_General_PM_Resume_2026_Updated_1013(1).pdf')
if original.is_file():
 check(hashlib.sha256(original.read_bytes()).digest()==hashlib.sha256(resume.read_bytes()).digest(),'Resume not identical to Oct 13 source')

# Safe to deploy: original award JPG, transcripts, identification etc must not be publicly distributed
for name in ('IMG_9931.JPG','future_award_source.jpg','GMAT.pdf','IELTS.pdf','transcript_MS.pdf','transcript_BS.pdf','node_modules'):
 check(not any(x.name.lower()==name.lower() for x in (ROOT/'static').rglob('*')),f'Private/excluded asset in public build: {name}')
check('future_award_source.jpg' not in css,'Award photograph appears in stylesheet')

# V8.3 structural, accessibility and visual regression invariants.
home=(ROOT/'layouts/index.html').read_text(encoding='utf-8')
check(home.count('metrics-v83')==3,'Home must use a stable three-column metric grid for each project')
check(home.count('partial "clinical-evidence-visual-v83.html"')==1,'Clinical AI project requires source-grounded evidence graphic')
check('validation-workflow-v83.svg' in home,'Validation project requires a distinct test workflow graphic')
check('career-journey-v83' in home,'About should show the career journey')
check(home.index('2023–2024') < home.index('2021–2023'),'Clinical internship timeline should precede 2021–23 Testing role')
work=(ROOT/'layouts/work/list.html').read_text(encoding='utf-8')
check('validation-workflow-v83.svg' in work,'Work index missing validation graphic')
check('clinical-evidence-visual-v83.html' in work,'Work index missing evaluation diagram')
check((ROOT/'layouts/partials/clinical-evidence-visual-v83.html').is_file(),'Missing shared chart partial')
check('1,007' in (ROOT/'layouts/partials/clinical-evidence-visual-v83.html').read_text(),'Research chart denominator missing')
check('84.96%' in (ROOT/'layouts/partials/clinical-evidence-visual-v83.html').read_text(),'Sensitivity trade-off must remain visible')
check((ROOT/'static/images/projects/validation-workflow-v83.svg').is_file(),'Vector validation diagram missing')
check((ROOT/'layouts/research/single.html').read_text().count('data-lightbox')==2,'Two source-grounded figures should have enlarge actions')
check('research-lightbox-v83' in (ROOT/'static/js/site.js').read_text(),'Accessible research image viewer missing')
check('prefers-reduced-motion' in (ROOT/'static/js/site.js').read_text(),'Motion preferences not respected')
check('education-page-shell-v510{display:grid;grid-template-columns:minmax(0,1fr)' in css,'Credentials must be moved from sidebar to full-width column')
check('grid-template-columns:repeat(3,minmax(0,1fr))' in css,'Metric grid missing responsive 3-column format')
check(css.count('!important')<10,'Legacy CSS override flags have not been normalized')
check('data-portfolio-version="8.3"' in base,'Deployed version marker should be 8.3')
check('?v=8.3.0' in head,'CSS cache-bust tag missing')
check('?v=8.3.0' in base,'JavaScript cache-bust tag missing')
check(len(list((ROOT/'static/css').glob('*.css')))==1,'Expected only one public V8.3 stylesheet')
check('portfolio-v82.css' not in base+head,'Old CSS must not load publicly')
try:
 import xml.etree.ElementTree as ET
 ET.parse(ROOT/'static/images/projects/validation-workflow-v83.svg')
 check(True,'SVG is valid')
except Exception as exc: check(False,f'Invalid validation diagram SVG: {exc}')

check((ROOT/'.github/workflows/hugo.yaml').read_text().find('scripts/verify_v83.py')!=-1,'GitHub Pages not running V8.3 validation')
print(f'V8.3 source checks: {checks-len(errors)}/{checks} passed')
if errors:
 print('ERRORS:')
 for e in errors:print(' -',e)
 sys.exit(1)
