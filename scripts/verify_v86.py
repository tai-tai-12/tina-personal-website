#!/usr/bin/env python3
"""V8.6 offline assertions for site content, shared visuals, credential proofs and deploy metadata."""
from pathlib import Path
import re,sys,hashlib,xml.etree.ElementTree as ET
try: import tinycss2
except ImportError: tinycss2=None
ROOT=Path(__file__).resolve().parents[1]
errors=[];checked=0

def check(ok,label):
 global checked
 checked+=1
 if not ok: errors.append(label)

def get(path): return (ROOT/path).read_text(encoding='utf-8')

for lang in ('en','zh'):
 pages=list((ROOT/'content'/lang).rglob('*.md'))
 check(len(pages)>=11,f'Not enough {lang} content pages')
 for part in ['work/medical-ai-product.md','work/clinical-ai-at-scale.md','work/structured-validation.md','research/thoracic-aorta.md']:
  check((ROOT/'content'/lang/part).is_file(),f'{lang} missing {part}')
 clinical=get(f'content/{lang}/work/clinical-ai-at-scale.md')
 product=get(f'content/{lang}/work/medical-ai-product.md')
 for word in ('94.54','1,007','55','84.96','80.97','T1C-only','0.9416','0.9514'):
  check(word in clinical,f'{lang} clinical evidence lacks {word}')
 for word in ('Future Tech Award','futuretech.org.tw','product-flow-phases-v82','LLM','case-boundary-v81'):
  check(word in product,f'{lang} product evidence lacks {word}')
 for p in (ROOT/'content'/lang/'work').glob('*.md'):
  t=p.read_text(encoding='utf-8'); front=t.split('---',2)
  if len(front)>2:
   for aid in re.findall(r'(?m)^- id:\s*([^\s]+)',front[1]):
    check(f'id="{aid}"' in t,f'{lang} missing navigation anchor {p.name}:{aid}')

home=get('layouts/index.html');work=get('layouts/work/list.html');edu=get('layouts/education/single.html');card=get('layouts/partials/work-evidence-visual-v84.html')
head=get('layouts/partials/head.html');base=get('layouts/_default/baseof.html');css=get('static/css/portfolio-v86.css')
check('content="8.6"' in head,'Missing head 8.5 version')
check('data-portfolio-version="8.6"' in base,'Missing HTML V8.6 version')
check('portfolio-v86.css' in head and '?v=8.6.0' in head,'Missing V8.6 CSS cache bust')
check('?v=8.6.0' in base,'Missing V8.6 JS cache bust')
check(len(list((ROOT/'static/css').glob('*.css')))==1,'Public CSS needs single entry point')
check(not any(p.name in ('portfolio-v83.css','portfolio-v84.css') for p in (ROOT/'static/css').glob('*.css')),'Old CSS still public')
check(home.count('partial "work-evidence-visual-v84.html"')==3,'Home does not use visual system for all three cases')
check(work.count('partial "work-evidence-visual-v84.html"')==3,'Work does not use visual system for all three cases')
check('work-product-v519.webp' not in home+work,'Old heterogeneous photo still used in Home/Work list')
check('validation-workflow-v83.svg' not in home+work,'Old heterogeneous validation image still used in Home/Work list')
check('clinical-evidence-visual-v83.html' not in home+work,'Old standalone clinical visual still used in Home/Work list')
for kind in ('product','clinical','validation'):
 check(f'"Kind" "{kind}"' in home and f'"Kind" "{kind}"' in work,f'Missing shared {kind} visual in Home/Work')
for token in ('evidence-v84-head','evidence-v84-eyebrow','evidence-v84-title','evidence-v84-footer','evidence-v84-steps','evidence-v84-bars','94.54%','84.96%','80.97%','1,007','55','~67%','10+'):
 check(token in card,f'Unified Work component missing {token}')
check('aria-label=' in card and 'aria-hidden=' in card,'Evidence visual accessibility labels missing')
check('{{ if $isZh }}' in card and 'Physician needs' in card and '醫師需求' in card,'Work visual EN/ZH localization broken')
for name in ('Licensed Medical Radiation Technologist','Outstanding Thesis Award','Google Ads Search','Data Science Fundamentals with Python','IBM Relational Database Administrator','Fundamentals of Visualization with Tableau','CS50'):
 check(name in edu,f'Credential directory missing {name}')
check(edu.count('credential-col-heading-v84')==3,'Credential directory should have 3 matching headings')
check(edu.count('credential-col-v84')==3,'Credential directory should have 3 matching columns')
check(edu.count('credential-list-v84')==3,'Credential directory should have 3 matching lists')
check('Data Science & Smart Instrumentation' not in edu,'Unverified training item not removed')
check('https://cs50.harvard.edu/ai/' not in edu,'Course description should not be a certification verifier')
for url in ('https://cs50.harvard.edu/certificates/1d4e0491-7302-4f56-84c1-fffb139622ae',
 'https://www.credential.net/81142a9a-5143-4e81-97be-9354d8667e3e',
 'https://www.credential.net/f2b46cae-5532-4190-80f1-9da00bf7dd7d',
 'https://www.coursera.org/verify/specialization/FJCM0NEN2YEI',
 'https://www.coursera.org/verify/professional-cert/TEEVL5E2DS84',
 'https://www.coursera.org/verify/FSKBD3NK1OJD'):
 check(url in edu, f'Certificate verification URL missing {url}')
check(edu.count('class="credential-links-v84"')==5,'Expected 5 curated credential groups')
for rule in ('.evidence-visual-v84{','.evidence-v84-steps{','.credential-col-heading-v84{','.credential-list-v84 li strong{','@media(max-width:480px)','prefers-reduced-motion'):
 check(rule in css,f'CSS is missing V8.4 component rule {rule}')
if tinycss2:
 rules=tinycss2.parse_stylesheet(css,skip_comments=True,skip_whitespace=True)
 check(not any(x.type=='error' for x in rules),'CSS parse errors detected')
# Relative static references in source templates and markdown.
for f in list((ROOT/'layouts').rglob('*.html')) + list((ROOT/'content').rglob('*.md')):
 t=f.read_text(encoding='utf-8')
 for r in re.finditer(r'{{\s*"((?:images|resume|css|js|research/publications)/[^"\n]+)"\s*\|\s*(?:relURL|absURL)',t):
  check((ROOT/'static'/r.group(1)).is_file(),f'Broken {f}: {r.group(1)}')
 for r in re.finditer(r'{{<\s*site-img\s+src="([^"\n]+)"',t):
  check((ROOT/'static'/r.group(1)).is_file(),f'Broken shortcode image {f}: {r.group(1)}')

check('scripts/verify_v86.py' in get('.github/workflows/hugo.yaml'),'Deploy does not validate V8.6')
for name in ('future_award_source.jpg','IMG_9931.JPG','GMAT.pdf','IELTS.pdf','transcript_MS.pdf','transcript_BS.pdf'):
 check(not any(p.name.lower()==name.lower() for p in (ROOT/'static').rglob('*')),f'Private file leaked: {name}')
check(not any(p.is_dir() and p.name=='node_modules' for p in (ROOT/'static').rglob('*')),'node_modules leaked')
res=ROOT/'static/resume/Shih-Ting_Tai_Resume.pdf'
check(res.is_file() and res.stat().st_size>50000,'Resume missing')
original=Path('/mnt/data/Shih-Ting_Tai_General_PM_Resume_2026_Updated_1013(1).pdf')
if original.exists():check(hashlib.sha256(original.read_bytes()).hexdigest()==hashlib.sha256(res.read_bytes()).hexdigest(),'Resume does not match Oct 13 version')
check(get('layouts/research/single.html').count('data-lightbox')==2,'Original aorta images lack lightbox controls')
check('research-lightbox-v83' in get('static/js/site.js'),'Image lightbox removed')
check('prefers-reduced-motion' in get('static/js/site.js'),'Motion reduction missing')
for asset in ('thoracic-aorta-3d-results-v81.webp','thoracic-aorta-multiplanar-annotation-v81.webp'):
 check((ROOT/'static/images/research'/asset).exists(),f'Original research figure missing {asset}')
try:
 ET.parse(ROOT/'static/images/projects/validation-workflow-v83.svg')
 check(True,'Legacy vector asset valid')
except Exception as e:check(False,f'Invalid vector asset {e}')

# V8.6 narratives, ceremony attribution, photo handling and no duplicate resume-like skills section.
about=get('layouts/about/single.html');research=get('layouts/research/list.html')
for name in ('about-v85-intro-grid','about-v85-lenses','about-v85-leadership-feature-grid','about-v85-community','about-v85-personal-grid','about-v85-photo'):
 check(name in about,f'About missing {name}')
check('capability-grid-v517' not in about,'Old About skills catalog remains')
check('foundation-grid-v63 foundation-grid-v82' not in home,'Home teaser duplicates the detailed About capabilities grid')
check('My story & leadership' in home and '閱讀我的故事與領導經歷' in home,'Home link to leadership story missing')
check('leadership-list-v517' not in about,'Old About activity chronology remains')
check('President, Department Student Association' in about,'Leadership centerpiece missing')
check('Selected MSBA Student Ambassador' in about,'Ambassador role missing')
check('Medical Camp for High School Students' in about and 'University Basketball Team Manager' in about,'About is missing student activities')
check('Hip-Hop Dance Club' in about,'Dance Club identity missing')
check('2020</span>' not in about,'Unverified dates for early activities should be omitted')
check('Graduation Ceremony Representative' in edu and '上台受獎' in edu,'Graduation ceremony recognition not properly attributed')
check('Commencement Speaker' not in edu+about and 'class president' not in edu.lower(),'Incorrect speaking or office claim')
check('CEREMONIAL REPRESENTATION' in edu and 'STUDENT LEADERSHIP' in edu,'Education classification missing')
check(edu.count('edu-v86-section edu-v86-campus')==3,'Expected 3 uniform Campus Highlights')
check('Selected Research Honors' in research and '精選研究榮譽' in research,'Research awards heading missing')
check(research.count('class="research-v85-award"')==2,'Research needs two recognition cards')
check('amlds-award-v519.webp' in research and 'thesis-award-v519.webp' in research,'Original awards missing')
check('future_award_source' not in research and 'IMG_9931' not in research,'Excluded Future Tech image referenced')
for rule in ('.about-v85-intro-grid{','.about-v85-lenses{','.about-v85-leadership-feature-grid{','.research-v85-award{','.edu-v86-section{' ,'@media(max-width:480px)'):
 check(rule in css,f'Missing V8.6 styling: {rule}')
for lang in ('en','zh'):
 t=get(f'content/{lang}/about/index.md')
 check('images/about/' not in t,'Old giant photo still embedded inside About prose')
 check(t.count('---')>=2,f'{lang} About frontmatter damaged')
# V8.6 focused information-architecture checks.
experience=get('layouts/experience/single.html')
recognition=get('layouts/partials/experience-recognition-v86.html')
check(edu.count('edu-v86-section edu-v86-coursework')==3, 'All degrees need consistent Selected Coursework')
check(edu.count('edu-v86-section edu-v86-campus')==3, 'All degrees need Campus Highlights')
check(edu.count('SELECTED COURSEWORK')==3, 'Coursework heading must be identical in all degree sections')
check('Fall 2026 · In progress' in edu and '2026 秋季 · 修習中' in edu, 'CMU current coursework must be labeled in progress')
check('CEREMONIAL REPRESENTATION' in edu and 'STUDENT INVOLVEMENT' in edu and 'STUDENT LEADERSHIP' in edu,'Campus subtype distinctions missing')
check('Commencement Speaker' not in edu and 'commencement speaker' not in edu.lower(),'Graduation ceremony misrepresented')
check(experience.count('class="xp-v86-role reveal"')==4, 'Four common experience roles missing')
check(experience.count('class="xp-v86-impact"')==4, 'One primary outcome needed per experience')
check(experience.count('class="xp-v86-detail"')==4, 'One selected-contributions section needed per experience')
check(experience.count('partial "experience-recognition-v86.html"')==2, 'Individual and team recognition should share a component')
for token in ('~67%', '94.5%', '1,040', '264 retrospective', '1,007 → 55', '3–6', '10+','8','5 clients'):
 check(token in experience, f'Missing experience evidence: {token}')
check('PROJECT RECOGNITION' in recognition and 'INDIVIDUAL RECOGNITION' in recognition, 'Recognition category differentiation missing')
check('Team' in recognition or 'team/project recognition' in recognition,'Future Tech must remain a team/project award')
for token in ('.xp-v86-role{','.xp-v86-impact{','.edu-v86-course-list{','.edu-v86-highlight{','.xp-v86-recognition{'):
 check(token in css, f'Missing V8.6 CSS component: {token}')
check('portfolio-v85.css' not in head+base, 'Legacy CSS URL still used in head/base')
check('data-portfolio-version="8.6"' in base,'Version missing in HTML data attribute')
print(f'V8.6 checks: {checked-len(errors)}/{checked} passed')
if errors:
 for e in errors:print('ERROR:',e)
 sys.exit(1)
