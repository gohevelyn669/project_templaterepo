# Basic template for projects
Description

## Structure 
- data/ # (ignored) raw data or links to sources
- notebooks/ # exploratory notebooks
- src/ # training and evaluation scripts
- results/ # output files (ignored by git)
  
- environment.yml # reproducible environment
- README.md
- .gitignore

## Quickstart
```bash
conda env create -f environment.yml
conda activate project_templaterepo
python src/train.py --seed 42
python src/evaluate.py --model results/model_seed42.joblib
