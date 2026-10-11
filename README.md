# Beauty & Wellness Customer Purchase and Retention Analysis

Week 1 project for **Data Science Orientation & Problem Definition in Beauty &
Wellness**. The main deliverable is a source-backed Word report proposing how
a beauty and wellness retailer could investigate repeat purchasing and
retention. It is a research design, not an executed customer analysis.

## Project structure

```text
beauty_wellness_data_science/
├── README.md
├── requirements.txt
├── generate_report.py
├── data/
│   └── README.md
├── docs/
│   ├── week1_beauty_wellness_problem_definition.docx
│   ├── analysis_plan.md
│   ├── research_sources.csv
│   └── variable_dictionary.csv
├── outputs/
│   └── figures/
└── src/
    ├── __init__.py
    ├── research_utils.py
    └── report_utils.py
```

No customer dataset or synthetic sample is included. The report does not
present invented findings; all five hypotheses are explicitly untested.
Potential public transaction and review datasets are discussed, but neither
was downloaded or analyzed. Verify dataset-specific licensing, reuse terms,
schema, and access conditions before use.

## Windows PowerShell setup

Open PowerShell in VS Code and run:

```powershell
Set-Location 'C:\ds task1.py\beauty_wellness_data_science'
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r .\requirements.txt
python .\generate_report.py
Test-Path .\docs\week1_beauty_wellness_problem_definition.docx
Get-Item .\docs\week1_beauty_wellness_problem_definition.docx | Select-Object FullName,Length
Start-Process .\docs\week1_beauty_wellness_problem_definition.docx
```

If PowerShell blocks activation, run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal,
then activate `.venv`. In Word, right-click the table of contents and select
**Update Field → Update entire table** to populate current page references.

## Contents

- `docs/week1_beauty_wellness_problem_definition.docx`: report with industry
  context, academic research foundation, business/data-science problem,
  objectives, seven research questions, five fully specified untested
  hypotheses, data-source options, dictionary appendix, ten-phase analysis
  workflow, evaluation criteria, privacy considerations, and 34-hour schedule.
- `docs/analysis_plan.md`: staged methodology, business definitions,
  candidate sources, privacy, and modeling readiness guidance.
- `docs/research_sources.csv`: source title/author, publication date where
  stated, URL, verification status, relevance, and limitations.
- `docs/variable_dictionary.csv`: candidate field definitions, examples,
  analytical roles, sources, required/optional status, quality checks, and
  privacy notes.
- `generate_report.py`: reproducible DOCX generator; uses project-relative paths.
- `src/`: CSV validation and Word field/hyperlink helpers.
- `requirements.txt`: Python, document, data science, statistics, and modeling
  dependencies.

Python, pandas, NumPy, Matplotlib, Seaborn, SciPy, scikit-learn, and
python-docx are included for the planned work. The report generator does not
load customer data or create synthetic findings.

## Evidence and review notes

McKinsey article titles and dates were checked on their public pages on
October 10, 2026. Academic metadata/abstracts were checked against Crossref
DOI records on October 11, 2026. One publisher article page returned HTTP 403,
which is disclosed in the report and source log; detailed study-method claims
for that paper require manual full-text review. Public dataset terms, schema,
and suitability also require manual verification before data acquisition.

Automated QA verifies DOCX presence, nonzero file size, required sections,
table of contents/page-number fields, and source hyperlinks. Rendering,
pagination, and TOC display should still be checked in Microsoft Word.
