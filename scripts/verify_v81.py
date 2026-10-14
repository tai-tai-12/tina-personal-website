#!/usr/bin/env python3
"""Offline source-level release checks for Tina Tai Portfolio V8.1 (stdlib only)."""
from pathlib import Path
import hashlib
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
checked=0

def check(condition,message):
    global checked
    checked+=1
    if not condition: errors.append(message)

# Paired pages and frontmatter contracts.
for lang in ('en','zh'):
    pages=sorted((ROOT/'content'/lang).rglob('*.md'))
    check(bool(pages),f'{lang}: content missing')
    for p in pages:
        t=p.read_text(encoding='utf-8')
        check(t.startswith('---\n') and t.find('\n---',4)>0,f'Invalid frontmatter: {p}')
        check('title:' in t[:t.find('\n---',4)],f'Missing title: {p}')
    print(f'{lang}: {len(pages)} pages')
enpaths={p.relative_to(ROOT/'content/en') for p in (ROOT/'content/en').rglob('*.md')}
zhpaths={p.relative_to(ROOT/'content/zh') for p in (ROOT/'content/zh').rglob('*.md')}
check(enpaths==zhpaths,f'Language page mismatch: {enpaths^zhpaths}')

# All locally referenced assets are present (URL strings in Hugo templates and shortcodes).
for p in list((ROOT/'layouts').rglob('*.html'))+list((ROOT/'content').rglob('*.md')):
    t=p.read_text(encoding='utf-8')
    for match in re.finditer(r'(?:(?:src|href)\s*=\s*|\b(?:src|href)\s+)"(?:{{\s*)?"((?:images|resume|css|js|research/publications)/[^"\n]*)"',t):
        ref=match.group(1)
        check((ROOT/'static'/ref).is_file(),f'Broken static reference: {p.relative_to(ROOT)} => {ref}')
    for match in re.finditer(r'{{<\s*site-img\s+src="([^"\n]+)"',t):
        check((ROOT/'static'/match.group(1)).is_file(),f'Broken shortcode asset: {p} => {match.group(1)}')

# Section anchors for localized case-study navigation.
for lang in ('en','zh'):
    for p in (ROOT/'content'/lang/'work').glob('*.md'):
        if p.name=='_index.md': continue
        t=p.read_text(encoding='utf-8')
        pre=t.split('---',2)[1]
        for ident in re.findall(r'(?m)^- id:\s*([^\s]+)',pre):
            check(f'id="{ident}"' in t, f'Missing anchored case-study section: {p.name} #{ident}')

# Entire website should not leak original private evidence vault.
for term in ('transcript_MS.pdf','transcript_BS.pdf','IELTS_20250716','GMAT','Medical Radiation Technologist License','unofficial_academic_record','node_modules'):
    check(not any(term in x.name for x in (ROOT/'static').rglob('*')),f'Private/irrelevant asset may be published: {term}')

resume=ROOT/'static/resume/Shih-Ting_Tai_Resume.pdf'
check(resume.exists() and resume.stat().st_size>50000,'Latest resume PDF missing/truncated')
check((ROOT/'static/css/v8-refresh.css').exists(),'Missing V8 stylesheet')
head=(ROOT/'layouts/partials/head.html').read_text(encoding='utf-8')
check('v8-refresh.css' in head,'V8 CSS not included')
check('content="8.1"' in head,'Incorrect release metadata')
check((ROOT/'layouts/_default/baseof.html').read_text().count('id="main-content"')==1,'Missing main content anchor')
for lang in ('en','zh'):
    case=(ROOT/f'content/{lang}/work/clinical-ai-at-scale.md').read_text()
    product=(ROOT/f'content/{lang}/work/medical-ai-product.md').read_text()
    check('94.5%' in case and '1,007' in case and '55 FP' in case,f'{lang}: missing evaluation outcome or denominator')
    check('Future Tech Award' in product and 'case-award-v8' in product,f'{lang}: missing team award')
# V8.1 evidence assertions.
check('v81-evidence.css' in head, 'V8.1 CSS not included')
check((ROOT/'static/css/v81-evidence.css').is_file(),'V8.1 CSS missing')
for lang in ('en','zh'):
    clinical=(ROOT/f'content/{lang}/work/clinical-ai-at-scale.md').read_text()
    product=(ROOT/f'content/{lang}/work/medical-ai-product.md').read_text()
    check(all(w in clinical for w in ['84.96','80.97','94.54','3.99','T1C-only','88.62','0.9416','0.9514']),f'{lang}: incomplete research tradeoff / validation notes')
    check('249' in clinical and '264' in clinical and 'retrospect' in clinical.lower() or ('249' in clinical and '264' in clinical and lang=='zh'), f'{lang}: missing scope distinction')
    check('product-flow-v81' in product and 'LLM' in product and 'MY CONTRIBUTION' in product if lang=='en' else 'product-flow-v81' in product and 'LLM' in product and '我的貢獻' in product, f'{lang}: product/team attribution missing')
    check('futuretech.org.tw' in product,f'{lang}: official project reference missing')
    check('IMG_9931' not in product,f'{lang}: original award photo accidentally referenced')
    check('TFDA clearance' not in product, f'{lang}: unsupported regulatory claim')
check(all((ROOT/'static/images/research'/f).is_file() for f in ['thoracic-aorta-3d-results-v81.webp','thoracic-aorta-multiplanar-annotation-v81.webp']), 'Original aorta figures missing')
check('MIDL' in (ROOT/'layouts/research/list.html').read_text() and 'https://2026.midl.io/scientific-program' in (ROOT/'layouts/research/list.html').read_text(), 'Official MIDL link missing')
check('SELECTED RESEARCH SUPPORT' in (ROOT/'layouts/research/list.html').read_text(), 'Research grant evidence missing')
check('credential.net/81142' in (ROOT/'layouts/education/single.html').read_text() and 'coursera.org/verify/professional-cert/TEEVL5E2DS84' in (ROOT/'layouts/education/single.html').read_text(), 'Credential verification missing')
check(not any(p.name.lower()=='img_9931.jpg' for p in (ROOT/'static').rglob('*')), 'User-excluded award photo published')
check('future_award_source.jpg' not in str(list(ROOT.rglob('*'))), 'Do not publish award source photo')
print(f'Passed {checked-len(errors)}/{checked} offline source assertions.')
if errors:
    print('ERRORS:')
    print('\n'.join(' - '+e for e in errors))
    sys.exit(1)
