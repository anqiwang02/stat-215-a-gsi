# STAT 215A — GSI Materials

This GitHub repo contains weekly discussion section materials, lab assignments/instructions, and homework assignments (as they're added) for **STAT 215, Fall 2026**.

> **Read this first:** [discussion/week1/lab-instructions.pdf](discussion/week1/lab-instructions.pdf) contains the general rules that apply to **ALL LABS**.

## Questions & discussion

Questions and discussions between students can be posted on Ed Discussions. That way everyone else can see your questions and the answers, and we don't have to answer the same questions a million billion times. Preferably you will answer each other's questions. It is our intention to only jump in when the question is one that only we can answer.

Please think carefully before asking questions specifically about the projects. For example, questions concerning how to do something specific in Python (e.g. "how do I format the data for linear regression in sklearn?") are fine, but questions asking what other people did for their analysis are not (e.g. "what are some findings that people have come across in the TBI project"). Questions asking about clarifications are fine.

## Repo structure

```
discussion/
├── slides.txt          # link to the Google Slides deck used in discussion section
└── week1/
    ├── lab-instructions.tex / .pdf   # general rules that apply to ALL LABS
    └── quarto-example.ipynb / .pdf   # demo: rendering notebooks to PDF with Quarto

lab0/                    # the warm-up lab (not representative of later labs' difficulty/openness)
├── instructions/
│   └── lab0-instructions.tex / .pdf
├── code/
│   └── environment.yaml / environment-r.yaml   # conda environments (Python / R)
└── data/
    └── USArrests.csv, stateCoord.csv
```

- `discussion/` — Weekly discussion section materials. Future `week#/` folders will hold that week's materials.
- `lab0/` — Lab 0, the warm-up lab.
- `lab#/` (future) — Each lab follows the same pattern: `instructions/` for the handout, `code/` for starter code/environments, `data/` for datasets.

## Acknowledgements

Thanks to Nico Sanchez, Anthony Ozerov, Chengzhong Ye, Theo Saarinen, Omer Ronen, James Duncan, Tiffany Tang, Zoe Vernon, Rebecca Barter, and other past STAT 215A GSIs for sharing their material.

This document was originally written by Rebecca Barter for STAT 215A in Fall 2017, has been lightly updated in subsequent years, and was significantly revised for STAT 214.