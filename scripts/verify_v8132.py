#!/usr/bin/env python3
"""Deployment checks for full-replacement V8.13.2 Hugo source; run before build."""
from pathlib import Path
import hashlib, re, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent.parent
errors=[]; count=0
def ck(val, note):
 global count
 count+=1
 if not val:errors.append(note)
def read(p):return (ROOT/p).read_text(encoding='utf-8')
head=read('layouts/partials/head.html');base=read('layouts/_default/baseof.html')
home=read('layouts/index.html');work=read('layouts/work/list.html');research=read('layouts/research/list.html')
nav=read('layouts/partials/header.html');about=read('layouts/about/single.html')
aorta=read('layouts/research/single.html');exp=read('layouts/experience/single.html')
css=read('static/css/portfolio-v8132.css');homecss=read('static/css/home-v8132.css')
workflow=read('.github/workflows/hugo.yaml')
ck('content="8.13.2"' in head,'V8.13.2 meta marker')
ck('data-portfolio-version="8.13.2"' in base,'V8.13.2 page marker')
ck('portfolio-v8132.css' in head and 'home-v8132.css' in head,'versioned CSS entrypoints')
ck('?v=8.13.2' in head and '?v=8.13.2' in base,'CSS/JS cache bust')
ck('scripts/verify_v8132.py' in workflow,'CI validation')
ck('hugo build' in workflow,'Hugo build action')
ck('2026 Future Tech Award' in home and 'NYCU project recognition' in home,'award attribution')
ck('IMG_9931' not in home,'excluded award photo')
ck('partial "case-metrics-v88.html"' in home,'shared homepage metrics component')
ck(home.count('partial "case-metrics-v88.html"')==3,'exactly 3 homepage metric groups')
ck('partial "case-metrics-v88.html"' in work,'Work uses shared metrics')
ck('case-metrics-v88-item' in read('layouts/partials/case-metrics-v88.html'),'shared metric structure')
ck('Read case study' in home and 'Read case study' in work,'consistent CTA')
ck('Explore project' not in work,'removed legacy CTA')
ck('class="evidence-v84-numbers"' in read('layouts/partials/work-evidence-visual-v84.html'),'underlying evidence graphic intact')
ck('evidence-v84-numbers{display:none}' in css,'repeated micro stats visually removed')
for target in ('medical-ai-product','clinical-ai-at-scale','structured-validation'):
 ck(home.count('"work/'+target+'/" | relLangURL')>=2,'home direct project link '+target)
for who in ('aitewan','research','clinical','bipi'):
 ck('#xp-v86-'+who+'-title' in home,'role deep link '+who)
 ck('id="xp-v86-'+who+'-title"' in exp,'role target exists '+who)
ck(nav.find('"research/" | relLangURL')<nav.find('"education/" | relLangURL'),'header order Research before Education')
ck(home.find('id="research"')<home.find('id="education"'),'homepage order matches header')
ck('href="{{ "work/clinical-ai-at-scale/" | relLangURL }}"' in research,'research card to direct Clinical AI')
ck('href="#brain-tumor-research"' not in research,'no inconsistent in-page research link')
ck('id="brain-tumor-research"' not in research,'no duplicated research output section')
ck(research.count('research-pub-thumb-v88')==2,'research talk and poster beside publications')
ck('research-v85-award' in research and research.count('<article class="research-v85-award">')==2,'research recognition preserved')
ck(aorta.count('class="metric-row-v63"')==0 and 'class="research-note-facts-v63"' in aorta,'no duplicate aorta result metrics')
ck('mailto:{{ .Site.Params.email }}' in about and 'mailto:{{ .Site.Params.email }}' in home,'contact entrypoints present')
for lang in ('en','zh'):
 ck((ROOT/f'content/{lang}').is_dir(),f'language directory {lang}')
 for item in ('medical-ai-product','clinical-ai-at-scale','structured-validation'):
  s=read(f'content/{lang}/work/{item}.md')
  ck('displayMetrics:' in s and s.count('  label:')>=3,f'{lang} structured outcomes {item}')
  ck('visual:' in s and 'heroStats:' in s,f'{lang} original case metadata preserved {item}')
 for num in ('94.54','84.96','80.97','1,007','55'):
  ck(num in read(f'content/{lang}/work/clinical-ai-at-scale.md'),f'{lang} canonical evaluation {num}')
 for p in ('work/medical-ai-product.md','work/clinical-ai-at-scale.md','work/structured-validation.md','research/thoracic-aorta.md'):
  ck((ROOT/f'content/{lang}/{p}').is_file(),f'{lang} content {p}')
for p in ('static/css/portfolio-v88.css','static/css/home-v88.css'):
 ck(not (ROOT/p).exists(),'removed obsolete stylesheet '+p)
for p in (ROOT/'layouts').rglob('*.html'):
 s=p.read_text(encoding='utf-8')
 for name in re.findall(r'{{\s*"((?:images|resume|css|js)/[^"\n]+)"\s*\|\s*(?:relURL|absURL)',s):
  ck((ROOT/'static'/name).is_file(),f'missing asset {p.name} {name}')
for p in ('images/research/midl-poster.webp','images/research/amlds-talk.webp','images/research/amlds-award-v519.webp','images/research/thesis-award-v519.webp','images/profile/tina-homepage-portrait-v530.webp'):
 ck((ROOT/'static'/p).is_file(),'missing image '+p)
for p in ('images/research/thoracic-aorta-3d-results-v81.webp','images/research/thoracic-aorta-multiplanar-annotation-v81.webp'):
 ck((ROOT/'static'/p).is_file(),'missing original study image '+p)
ck('research-lightbox-v83' in aorta,'research figure zoom retained')
ck('Campus Highlights' in read('layouts/education/single.html') or 'CAMPUS HIGHLIGHTS' in read('layouts/education/single.html'),'education retained')
ck('xp-v86-impact' in exp,'Experience layout retained')
try:
 import tinycss2
 for name,code in [('portfolio',css),('home',homecss)]:
  err=[x for x in tinycss2.parse_stylesheet(code,skip_whitespace=True,skip_comments=True) if x.type=='error']
  ck(not err,'CSS parse error '+name)
except ImportError:pass
try:
 import yaml
 for lang in ('en','zh'):
  for item in ('medical-ai-product','clinical-ai-at-scale','structured-validation'):
   s=read(f'content/{lang}/work/{item}.md');y=yaml.safe_load(s.split('---',2)[1]);a=y['displayMetrics']
   ck(len(a)==3 and all(x.get('value') and x.get('label') for x in a),'frontmatter metrics parse '+lang+item)
except ImportError:pass
for name in ('IMG_9931.JPG','future_award_source.jpg','GMAT.pdf','IELTS.pdf'):
 ck(not any(p.name.lower()==name.lower() for p in (ROOT/'static').rglob('*')),'private raw asset '+name)
resume=ROOT/'static/resume/Shih-Ting_Tai_Resume.pdf'
ck(resume.is_file() and resume.stat().st_size>50_000,'resume PDF exists')
source=Path('/mnt/data/Shih-Ting_Tai_General_PM_Resume_2026_Updated_1013(1).pdf')
if source.is_file():
 ck(hashlib.sha256(resume.read_bytes()).digest()==hashlib.sha256(source.read_bytes()).digest(),'latest resume unchanged')
ck((ROOT/'.github/workflows/hugo.yaml').is_file(),'hidden GitHub workflow included')

# V8.13.2 accuracy: consortium work and third-party reports are the same assignment.
for lang in ('en','zh'):
    c=read(f'content/{lang}/work/structured-validation.md')
    ck('xray-testing-evidence-v89.svg' in c and 'xray-tube-testing-hero-v89.svg' in c, f'{lang} new original X-ray visuals')
    ck('heroStats:' in c and c.split('heroStats:',1)[1].split('snapshot:',1)[0].count('value:')==3, f'{lang} three test metrics only')
    ck('3871' in c and 'ISO/IEC 17025' in c and 'accreditation.taftw.org.tw' in c, f'{lang} accreditation context')
    ck('ionizingradiation' in c and 'jcchen' in c, f'{lang} consortium/laboratory links')
    ck(('member recruitment' in c or 'recruited' in c or '會員招募' in c or '招募' in c), f'{lang} member recruitment')
    ck(('small-animal CT' in c or '小動物 CT' in c) and 'two university' in c or ('小動物 CT' in c and '兩個大學' in c), f'{lang} separate quantitative research')
    ck('testing-measurement-v521.webp' not in c and 'testing-hero-v521.webp' not in c, f'{lang} no false microscopy visual')
    ck('10+' in c and '8' in c and '5' in c, f'{lang} reported test metrics preserved')
for name in ('xray-tube-testing-hero-v89.svg','xray-testing-evidence-v89.svg'):
    asset=ROOT/'static/images/projects/detail-v521'/name
    ck(asset.is_file(), 'new validation image present '+name)
    if asset.is_file():
        ET.fromstring(asset.read_text(encoding='utf-8'))
        ck('CONCEPTUAL' in asset.read_text(encoding='utf-8') or 'ILLUSTRATIVE' in asset.read_text(encoding='utf-8'), 'non-photo disclaimer '+name)
ck('X-ray' in exp and 'consortium' in exp.lower() and 'third-party' in exp.lower(), 'Experience role correctly scoped')
ck('X-ray tube' in home and '球管' in home, 'homepage third-case summary corrected')
ck('X-ray tube tests to reports' in read('layouts/partials/work-evidence-visual-v84.html'),'work tile domain accuracy')
for name in ('testing-hero-v521.webp','testing-measurement-v521.webp','work-testing-v519.webp'):
    ck(not any(x.name==name for x in (ROOT/'static').rglob('*')), 'outdated misleading visual removed '+name)


# V8.13.2: conservatively scoped client engagement and recruiter-readable presentation.
for lang in ('en','zh'):
    case=read(f'content/{lang}/work/structured-validation.md')
    ck(('professor' in case.lower() if lang=='en' else '教授' in case), f'{lang} origin of company introduction explicit')
    ck(('agreement' in case.lower() if lang=='en' else '合約' in case), f'{lang} agreement coordination reflected')
    ck(('X-ray' in case if lang=='en' else 'X 光' in case) and '10+' in case and '8' in case and '5' in case, f'{lang} primary testing outputs preserved')
    ck(('separate research' in case.lower() if lang=='en' else '獨立研究' in case), f'{lang} CT work separate')
    ck(not any(x in case.lower() for x in ('cold outreach','independently sourced','acquired five clients','closed five deals')), f'{lang} no invented sales ownership')
    ai=read(f'content/{lang}/work/clinical-ai-at-scale.md')
    ck(('false alarms' in ai if lang=='en' else '錯誤提示' in ai),f'{lang} plain language AI explanation')
for marker in ('professor-introduced companies', 'membership and agreement paperwork', 'TAF laboratory accredited scope'):
    ck(marker in exp, f'Experience conservative client handling and accreditation: {marker}')
ck('professor-introduced industry contacts' in home,'home conservative client attribution')
ck('xp-v811-compact' in exp and exp.count('xp-v811-compact')>=2,'compact earlier role template')
ck(exp.count('xp-v86-contributions li')==0 if False else exp.count('class="xp-v86-contributions"')==3,'contribution lists preserved')
ck('font-size:.84rem' in css and 'case-margin-nav-v526' in css,'case navigation readability')
ck('DELIVERY SCOPE' in exp and 'TRAINING SCOPE' in exp,'scope vs impact distinguished')
ck('aria-current="location"' in nav, 'current section navigation state included')
ck('if eq .Site.Language.Lang "zh"' in base, 'localized skip-to-content')
ck('{{ if $isZh }}家醫療中心{{ else }}medical centers{{ end }}' in research, 'research evidence labels localized')
ck('模型開發用 MRI 病例' in read('content/zh/work/clinical-ai-at-scale.md'), 'clinical study cohort labels localized')
ck('Graduation Ceremony Representative' in read('layouts/education/single.html'), 'ceremonial representative preserved')

# V8.13.2 localization and language-specific evidence rules.
edu=read('layouts/education/single.html');home=read('layouts/index.html');honors=read('layouts/partials/experience-recognition-v86.html')
for val in ('卡內基美隆大學','國立陽明交通大學','生醫光電研究所','生物醫學影像暨放射科學系','機器學習與生醫應用','磁振造影原理','書卷獎','傑出口頭報告獎','放射腫瘤科實習表現優異獎'):
 ck(val in edu,'localized Education content: '+val)
for val in ('國立陽明交通大學','卡內基美隆大學','傑出論文獎','第一作者 · 短論文海報發表','獲傑出口頭報告獎'):
 ck(val in home,'localized homepage content: '+val)
for val in ('書卷獎','Outstanding Oral Presentation','Honor Student Award'):
 ck(val in edu,'bilingual original/reference: '+val)
ck('放射腫瘤科實習表現優異獎' in honors,'individual award correct department')
ck('傑出口頭報告獎' in research,'Research awards translated')
ck('本次正式發表名稱維持英文' not in research,'original paper titles preserved without fabricated translation')
ck('padding-top:clamp(36px,3.5vw,42px)' in homecss,'desktop homepage About baseline adjusted')
ck('@media (max-width:770px)' in homecss,'mobile About alignment restored')
ck('content="8.13.2"' in head,'release version 8.13')
ck('Certificate of Excellence' in edu,'English award name preserved')

# V8.13.2 FINAL regression — containment and zh localization.
ck('grid-template-columns:repeat(3,minmax(0,1fr))' in css, 'Research three-column metric container')
ck('.research-area-card-v64 .research-proof-row-v64>em' in css, 'Research child metrics constrained')
ck('white-space:normal' in css and 'overflow-wrap:break-word' in css, 'Research metrics allow natural wrapping')
ck('@media(max-width:560px)' in css, 'mobile single-column Research metrics')
ck('主要研究{{ else }}PRIMARY RESEARCH' in research, 'Research primary classification localized')
ck('基礎研究 · 國科會{{ else }}FOUNDATIONAL RESEARCH' in research, 'Research foundational classification localized')
ck('DSC · segmentation overlap' in research, 'shortened and comprehensible DSC label')
for name in ('medical-ai-product','clinical-ai-at-scale'):
 s=read('content/zh/work/'+name+'.md')
 ck('## 重點總結' in s and '## Takeaway' not in s,'zh case conclusion translated '+name)
ck('本頁核心數據統一採用碩士論文中的' in read('content/zh/work/clinical-ai-at-scale.md'), 'Clinical AI final cohort explanation localized')
for item in ('案例背景','專案關鍵數據','專案摘要','案例導覽'):
 ck(item in read('layouts/work/single.html'),'case aria localized '+item)
ck('Tina Tai 首頁' in read('layouts/partials/header.html'),'header brand aria localized')
ck('研究成果' in aorta,'aorta results aria localized')
for p in ('static/css/portfolio-v813.css','static/css/home-v813.css','scripts/verify_v813.py'):
 ck(not (ROOT/p).exists(), 'no obsolete stylesheet / verifier '+p)

print(f'V8.13.2 offline source checks: {count-len(errors)}/{count} passed')

# Regression guard: Go's dot changes in `with .Params.snapshot`. Refer to page language through `$`.
single=read('layouts/work/single.html')
ck('{{ with .Params.snapshot }}' in single,'case snapshot is present')
ck('aria-label="{{ if eq $.Lang "zh" }}專案摘要{{ else }}Project brief{{ end }}"' in single,'correct snapshot root language')
ck('aria-label="{{ if eq .Lang "zh" }}專案摘要' not in single,'invalid nested language lookup absent')
for p in (ROOT/'layouts').rglob('*.html'):
 s=p.read_text(encoding='utf-8')
 ck(s.count('{{')==s.count('}}'),f'Go template brace count: {p.relative_to(ROOT)}')
if errors:
 print('V8.13.2 source checks FAILED:')
 for e in errors:print(' -',e)
 sys.exit(1)
print(f'V8.13.2 source checks passed: {count}/{count}')
