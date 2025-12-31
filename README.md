Towards automated causal discovery in the social sciences


This project implements a non-experimental replication framework to validate Causal Discovery algorithms, the Additive Noise Model (ANM) and Information-Geometric Causal Inference (IGCI). By mapping 11 causal pairs from established RCT meta-analyses to observational datasets, this repository makes a step forward towards how "Big Data" can be used to verify causal claims in social science.


Project Structure

The repository is organized into three primary functional areas to ensure reproducibility and clarity:

EDA.ipynb (Exploratory Data Analysis): Contains the statistical profiling of the observational datasets (NSCH 2024, CLASS, and FFCWS). It includes normality testing (Shapiro-Wilk), correlation analysis, and the identification of "Indication Bias" and "Data Sparsity" issues.

Test.ipynb (Causal Inference Testing): The core execution engine. This notebook runs the ANM and IGCI algorithms across all 11 causal pairs. It calculates directionality scores, confidence intervals, and p-values to determine if the observational data matches the experimental ground truth.

VIS.ipynb (Visualizations): Generates the comparative plots used in the final report, including the mapping of meta-analytic effect sizes ($g$) against algorithmic confidence scores.


Open Science & FAIR Principles

This project is built as a Replication Research initiative, adhering to the following standards:

Findable & Accessible: Utilizes public, high-resolution datasets (NSCH, IPCSR) with documented retrieval steps.

Interoperable: Provides code to transform raw survey data (ordinal/categorical) into continuous numerical formats suitable for causal discovery.

Reusable: All notebooks are documented to allow for the external validation of our "Non-Experimental Replication" methodology.



Key Findings

Accuracy: The framework achieved a 72.7% accuracy in replicating the expected causal direction or identifying the absence of a signal (Null Replications).

Indication Bias: The analysis successfully identified "Treatment Assignment Bias" in clinical data, where the algorithm correctly inferred that symptom severity drives treatment entry.

Algorithm Performance: IGCI proved significantly more robust for Gaussian social-science variables compared to the ANM.


Installation & Usage

Clone the repository.

Ensure you have cdt, numpy, pandas, and scipy installed.

Run EDA.ipynb to verify data integrity.

Run Test.ipynb to execute the causal discovery benchmarks.
