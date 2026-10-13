# AGENTS.md for MLGEO2026_UWNETID

## Project
Course repository for ESS 469, Autumn 2026: homeworks and the final project.
README.md provides the baseline from which to clone this repository.

## Environment and compute
- `pixi` is the foundation of the python code in this environment.
- The files `pixi.toml` and `pixi.lock` are a package deal and are always committed together.
- All files will be intsalled and ran through `pixi`. Other package installers are not permitted.

## Data and provenance
- All data is to be handled carefully and deliberately. Raw data is never altered and only ever read in.
- Where applicable attach data locators (DOIs, URLs, etc) from fetched and downloaded data
- Fetched and downloaded data is to be retrieved via code in a script in this repository. This could be a python, SQL, or other script in this repository.
- Data product files (statistics, figures, other analysis, etc) are to be written to a distinct product folder in this repository. Do not place products in the same locations as raw data.

## Code and workflow
- Use relative not absolute paths; this repository is homebase for reading, writing, and running code.
- Notebooks are to be ran sequentially and never out of order.
- All mass running commands (Restart Kernel, Run All Cells, etc) must run through and finish a notebook without issue. If issues do arise, make a note of it, reporting which notebook and which cell failed.
- Do not change code if there are minor syntax or similar issues; report all mistakes noting which and what cell contained the mistake.
- README.md defines the commands to be used to verify the efficacy of this repository. Any other metrics are auxillary to the README.md commands at best.

## Reporting and credit
- If values are reported state its units and referntial information. These could be temporal identifiers, resolution, geolocators, or other metadata-type information.
- AI drafted commits are to be made with a template as follows: "AI draft for <relevant application>; <summary of draft>".

## Verification
- Run `pixi run smoke` before reporting any result, and show its last line.
- Report the exact commands you ran and the commit hash they ran on.
- If a check fails or a value cannot be fetched, say so; do not substitute an estimate.