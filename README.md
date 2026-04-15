

## **Group members**
**Group 3**

| Name | Student ID |
|------|------------|
| Zixin Fan | 300296371 |
| Sophie Séguin | 300225009 | 
| Nathan Amuaro |  | 
| Zheng Yew Wong | 30051183 | # L1_L2_project
This project studies L1 (Lasso) and L2 (Ridge) regularization on sparse linear models, including synthetic data generation, experimental evaluation, and analysis of prediction accuracy, parameter estimation, and variable selection.

## **Programming Task distribution**
- Zixin Fan
  - Synthetic dataset generation and experimental setup.
  - Analysis of predictive performance, parameter estimation accuracy, and variable selection performance.
    - Independent Gaussian
      - Predictive Performance vs Sample Size (n) following Experiment 1  
        (Analyzed how increasing sample size reduces test error and improves generalization)
      - Variable Selection Performance vs Penalty Term (λ) following Experiment 2  
        (Analyzed how λ controls sparsity, including under- and over-regularization effects)
      - Predictive Performance vs Sparsity Level (s) following Experiment 2  
        (Analyzed how model sparsity affects Lasso vs Ridge performance)
      - Variable Selection vs Sample Size (n) following Experiment 3  
        (Analyzed how increasing n improves support recovery accuracy)
      - Parameter Estimation Accuracy based on 04_bias_variance  
        (Analyzed bias–variance tradeoff and compared stability of Ridge vs Lasso)
    - Correlated Gaussian
      - Variable Selection Performance vs Feature Correlation (ρ) following Experiment 1  
        (Analyzed how correlation degrades Lasso’s support recovery while Ridge remains stable)
      - Predictive Performance vs Noise (σ) following Experiment 2  
        (Analyzed how increasing noise impacts test error and model robustness)
      - Variable Selection Performance vs Penalty Term (λ) following Experiment 3  
        (Analyzed how λ controls sparsity under correlated features and affects over-shrinkage)
    - High Dimensional (d > n)
      - Variable Selection Performance vs Dimension (d)
        (Analyzed how increasing dimensionality degrades support recovery in both independent and correlated settings)
      - Variable Selection Performance vs Sample Size (n)
        (Analyzed how increasing sample size helps recover true support and alleviates the high-dimensional difficulty)
      - Variable Selection Performance vs Correlation (ρ)
        (Analyzed how feature correlation further deteriorates Lasso’s recovery while Ridge remains more stable)
      - Variable Selection Performance vs Penalty Term (λ) on Lasso
        (Analyzed how λ controls sparsity in high-dimensional settings, including under- and over-regularization effects)
  - High-dimensional regime (d > n) – analysis of model behaviour, explanation of ridge uniqueness and lasso sparsity, and evaluation of prediction error and support recovery.
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

## Project Structure

- `data_generation.py`  
  Contains the function for generating synthetic data (X, y, w*, support).  
  You can change parameters (n, d, s, sigma, signal) to test different settings.
  
- `main_results.ipynb`  
  Main notebook for experiments.  
  All results, plots, and analysis should be done here using the generated data.

  ## Statement of AI usage
  ChatGPT (OpenAI, 2026) was used for brainstorming ideas and assisting with bug fixes during the development of this code.
