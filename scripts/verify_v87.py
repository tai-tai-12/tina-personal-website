#!/usr/bin/env python3
"""V8.7 homepage design/IA checks before GitHub Pages Hugo build."""
from pathlib import Path
import re, hashlib, sys, xml.etree.ElementTree as ET
root=Path(__file__).resolve().parent.parent
n=0;errors=[]
def check(ok,name):
 global n
 n+=1
 if not ok: errors.append(name)
def load(path):return (root/path).read_text(encoding='utf-8')
home=load('layouts/index.html');head=load('layouts/partials/head.html');base=load('layouts/_default/baseof.html');styles=load('static/css/home-v87.css');oldstyles=load('static/css/portfolio-v86.css')
check('content="8.7"' in head,'head version missing')
check('data-portfolio-version="8.7"' in base,'base version missing')
check('css/home-v87.css' in head and '{{ if .IsHome }}' in head,'home-only stylesheet scope missing')
check('?v=8.7.0' in head and '?v=8.7.0' in base,'asset cache bust missing')
check('scripts/verify_v87.py' in load('.github/workflows/hugo.yaml'),'workflow does not run V8.7 QA')
check('{{ define "main" }}' in home and home.strip().endswith('{{ end }}'),'home template wrapper')
check(home.count('{{ if $isZh }}')==home.count('{{ else }}'),'EN/ZH conditional count')
for label,anchor in [('work','#work'),('experience','id="experience"'),('research','id="research"'),('education','id="education"'),('about','id="about"')]:check(anchor in home,f'{label} homepage section or scroll link absent')
check(home.count('partial "work-evidence-visual-v84.html"')==3,'3 original shared case visuals missing')
for project in ('medical-ai-product','clinical-ai-at-scale','structured-validation'):
 check(home.count('"work/'+project+'/" | relLangURL')>=2,f'{project} direct case links missing')
check(home.count('class="home-v87-case reveal"')==3,'expected 3 equal presentation case cards')
check(home.count('class="home-v87-xp-row"')==4,'expected 4 selected experience lines')
check(home.count('class="home-v87-education-row"')==3,'expected complete B.S., M.S., MSBA timeline')
check(home.count('class="home-v87-research-card"')==2,'expected 2 research first-author cards')
for text in ('M.S. Business Analytics','M.S. Biophotonics','B.S. Biomedical Imaging','Minor in Biomedical Engineering','Clinical Intern','Product Manager','Test Manager'):
 check(text in home,'home missing '+text)
for word in ('~67%','94.5%','90.16%','264','10+','2026 Future Tech Award','Outstanding Oral Presentation Award'):
 check(word in home,'home metric or award missing '+word)
check('NYCU project recognition' in home and '陽明交大團隊／專案獲獎' in home,'team recognition attribution missing')
check('Read case study' in home and '閱讀完整案例' in home,'user direct case action missing')
check('All case studies' in home and '案例總覽' in home,'Work overview CTA missing')
check('home-v87-hero-actions' in home and 'href="#work"' in home,'hero CTA must show cases on home')
check('career-journey-v83' not in home and 'foundation-grid' not in home,'duplicated About skills or timeline remains')
check('Future Tech Award' in home and 'IMG_9931' not in home,'excluded award photo referenced')
check('home-v87-section-heading' in styles and '.home-v87-education-row' in styles,'missing homepage component styling')
for bp in ('770px','540px','1000px'):
 check(bp in styles,'responsive breakpoint '+bp+' missing')
check('prefers-reduced-motion' in styles,'reduced motion styles missing')
try:
 import tinycss2
 for name,code in [('home',styles),('base',oldstyles)]:
  bad=[x for x in tinycss2.parse_stylesheet(code,skip_comments=True,skip_whitespace=True) if x.type=='error']
  check(not bad,'CSS parse error: '+name)
except ImportError:pass
for lang in ('en','zh'):
 pagefiles=list((root/'content'/lang).rglob('*.md'))
 check(len(pagefiles)>=11,'missing bilingual inner content '+lang)
 for fn in ('work/medical-ai-product.md','work/clinical-ai-at-scale.md','work/structured-validation.md','research/thoracic-aorta.md'):
  check((root/'content'/lang/fn).is_file(),f'missing {lang} case {fn}')
 for word in ('94.54','84.96','80.97','1,007','55'):
  check(word in load(f'content/{lang}/work/clinical-ai-at-scale.md'),f'{lang} canonical research metric missing {word}')
for src in (root/'layouts').rglob('*.html'):
 s=src.read_text(encoding='utf-8')
 for name in re.findall(r'{{\s*"((?:images|resume|css|js)/[^"\n]+)"\s*\|\s*(?:relURL|absURL)',s):
  check((root/'static'/name).is_file(),f'static asset missing {src.name}:{name}')
for img in ('images/profile/tina-homepage-portrait-v530.webp','images/research/midl-poster.webp','images/research/amlds-talk.webp'):
 check((root/'static'/img).is_file(),'homepage image missing '+img)
check('class="xp-v86-role' in load('layouts/experience/single.html'),'V8.6 experience layout damaged')
check('edu-v86-coursework' in load('layouts/education/single.html'),'V8.6 education layout damaged')
for private in ('future_award_source.jpg','IMG_9931.JPG','GMAT.pdf','IELTS.pdf'):
 check(not any(f.name.lower()==private.lower() for f in (root/'static').rglob('*')),'private material published '+private)
resume=root/'static/resume/Shih-Ting_Tai_Resume.pdf'
check(resume.is_file() and resume.stat().st_size>50_000,'resume missing')
orig=Path('/mnt/data/Shih-Ting_Tai_General_PM_Resume_2026_Updated_1013(1).pdf')
if orig.exists():check(hashlib.sha256(resume.read_bytes()).digest()==hashlib.sha256(orig.read_bytes()).digest(),'resume mismatches approved Oct 13 version')
check('project' in load('layouts/work/list.html').lower(),'Work overview removed')
print(f'V8.7 source validation: {n-len(errors)}/{n} checks passed')
if errors:
 for e in errors:print('FAIL:',e)
 sys.exit(1)
