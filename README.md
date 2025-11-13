# Assignment 5: Quicksort Algorithm — Implementation, Analysis, and Randomization

## Overview

This repository contains the implementation, analysis, and experimental evaluation of the **Quicksort algorithm**, including both **deterministic** and **randomized** versions.

The goal of this project is to:
- Implement the Quicksort algorithm in Python.
- Analyze its **time and space complexity**.
- Study the effect of **randomization** on pivot selection and performance.
- Empirically compare both versions across various input distributions.

This assignment demonstrates how pivot selection impacts Quicksort’s efficiency and how randomization reduces the likelihood of worst-case behavior, providing valuable insights into algorithm optimization and scalability.


## Repository Structure
├── deterministic_quicksort.py # Deterministic Quicksort implementation (pivot = last element)

├── randomized_quicksort.py # Randomized Quicksort implementation (pivot = random)

├── performance_comparison.py # Safe empirical performance test script with graphs

├── Assignmnent 5 Report.docx # Detailed technical report and analysis

├── README.md # Instructions on how to run

Implementation Details

### Deterministic Quicksort
- Uses the **last element** as the pivot.
- Recursively sorts elements less than and greater than the pivot.
- Performs poorly on **sorted** or **reverse-sorted** data (worst-case (O(n^2)).

File: deterministic_quicksort.py

## Randomized Quicksort

- Randomly selects a pivot for each partition.

- Prevents deterministic degradation on structured inputs.

- Maintains expected O(nlogn) time for all input distributions.

File: randomized_quicksort.py

Empirical Performance Analysis
## Experiment Script

The script performance_comparison.py compares runtime performance between deterministic and randomized Quicksort implementations.

It:

- Tests multiple input sizes (up to 8,000 elements).

- Uses three input types:

Random

Sorted

Reverse-sorted

- Plots results as graphs using matplotlib.

# Safety Features

- Limits recursion depth to prevent crashes.

- Caps maximum input size.

- Catches recursion errors gracefully.

- Saves plots automatically as .png files.

To generate results, run:

python performance_comparison.py


You will see console output showing timing results and generated performance graphs


