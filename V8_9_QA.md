# V8.9 Quality Assurance

Run `python3 scripts/verify_v89.py`. The source checker validates bilingual content, portfolio and CSS markers, citation/verification links, assets and source case routes, privacy exclusions, absence of retired incorrect microscopy figures, and that the 8 products / 5 clients / 10+ reports remain one workstream.

Additional checks should include real rendered screenshots after Hugo deployment: English/Traditional Chinese; 1440px desktop and 390px mobile; light and dark theme; testing Hero graphics; all official external links; PDF resume download.

**Build caveat:** A source-level or reconstructed-template preview does not equal a successfully completed Hugo production build; the actual build runs in the GitHub Actions workflow.
