# stat-215-a-gsi
This repo contains weekly discussion section materials and lab instructions, along with homework assignments as they're added.

Please see [discussion/week1/lab-instructions.pdf](discussion/week1/lab-instructions.pdf) for general rules that apply to ALL LABS.


## Repo structure

- `discussion/` — Weekly discussion section materials.
  - `slides.txt` — link to the Google Slides deck used in discussion section.
  - `week1/`:
    - `lab-instructions.tex`/`.pdf` — general lab instructions that contain rules that apply to ALL LABS.
    - `quarto-example.ipynb`/`.pdf` — a demo notebook showing how to render Jupyter notebooks to PDF with [Quarto](https://quarto.org).
  - Future `week#/` folders will contain materials relevant to the discussion section that week.
- `lab0/` — Lab 0 (the warm-up lab; not representative of the difficulty/openness of later labs).
  - `instructions/` — `lab0-instructions.tex`/`.pdf`, the lab handout.
  - `code/` — `environment.yaml` / `environment-r.yaml`, conda environment files for the Python and R setups used in the lab.
  - `data/` — `USArrests.csv`, `stateCoord.csv`, the datasets used in the lab.

Future `lab#/` folders follow the same pattern: `instructions/` for the handout, `code/` for starter code/environments, `data/` for datasets.