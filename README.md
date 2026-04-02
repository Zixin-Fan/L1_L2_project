

## **Group members**
**Group 3**

| Name | Student ID |
|------|------------|
| Zixin Fan | 300296371 |
| Sophie Séguin | 300225009 | 
|  |  | 
|  |  | # L1_L2_project
This project studies L1 (Lasso) and L2 (Ridge) regularization on sparse linear models, including synthetic data generation, experimental evaluation, and analysis of prediction accuracy, parameter estimation, and variable selection.

## **Task distribution**
- Zixin Fan
  - Synthetic dataset generation and experimental setup.
  - Analysis of predictive performance, parameter estimation accuracy, and variable selection performance.
  - High-dimensional regime (d > n) – analysis of model behaviour, explanation of ridge uniqueness and lasso sparsity, and evaluation of prediction error and support recovery.
  - Slides preparation and participation in code testing and validation.
- Sophie Seguin
  - Designed and coded all computational experiments, including:
    - Bias vs. regularisation strength under orthonormal design.
    - Support recovery (F1 score, recall, precision) as functions of correlation, sample size, dimensionality, and sparsity.
    - Learning curves (test MSE vs. n) and sparsity paths (non‑zero coefficients vs. λ).
    - High‑dimensional regime experiments (d > n), analysing prediction error and support recovery.
    - Noise sensitivity experiments (test MSE vs. σ).
    - Bias‑variance decomposition (bias calculation and variance quantification).
  - Participated in code testing, validation
  - Adding decoy variables to data generation
  - Writing and correction of the final report

## Project Structure

- `data_generation.py`  
  Contains the function for generating synthetic data (X, y, w*, support).  
  You can change parameters (n, d, s, sigma, signal) to test different settings.
  
- `main_results.ipynb`  
  Main notebook for experiments.  
  All results, plots, and analysis should be done here using the generated data.

  ## Statement of AI usage
  ChatGPT (OpenAI, 2026) was used for brainstorming ideas and assisting with bug fixes during the development of this code.
