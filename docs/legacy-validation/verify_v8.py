#!/usr/bin/env python3
"""Offline source-level release checks for Tina Tai Portfolio V8.0 (stdlib only)."""
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
check('content="8.1"' in head,'Release metadata is not current')
check((ROOT/'layouts/_default/baseof.html').read_text().count('id="main-content"')==1,'Missing main content anchor')
for lang in ('en','zh'):
    case=(ROOT/f'content/{lang}/work/clinical-ai-at-scale.md').read_text()
    product=(ROOT/f'content/{lang}/work/medical-ai-product.md').read_text()
    check('94.5%' in case and '1,007' in case and '55 FP' in case,f'{lang}: missing evaluation outcome or denominator')
    check('Future Tech Award' in product and 'case-award-v8' in product,f'{lang}: missing team award')
print(f'Passed {checked-len(errors)}/{checked} offline source assertions.')
if errors:
    print('ERRORS:')
    print('\n'.join(' - '+e for e in errors))
    sys.exit(1)
