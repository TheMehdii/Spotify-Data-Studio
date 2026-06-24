# 🎵 Spotify Data Studio: Advanced Music Data Management & Analytics System

An advanced, production-grade **Data Engineering and Interactive Analytics Dashboard** designed to securely load, clean, analyze, and visualize multi-dimensional music streaming data. This system is built from scratch utilizing modular design patterns and strict software engineering principles.

---

## 🏛️ Project Architecture & OOP Principles
This project is built around a highly structured, decoupled **Object-Oriented Programming (OOP)** architecture rather than a simple scripting style. 

* **Encapsulation:** Implemented defensive data auditing inside domain models (such as ensuring metrics like song popularity or acoustic attributes remain strictly within valid logical bounds).
* **Inheritance & Polymorphism:** Designed abstract base classes for data processing pipelines, allowing interchangeable execution of various mathematical cleaning algorithms.

---

## 🛠️ Core Features

### 1. Missing Value Imputation
The system provides structural, polymorphic techniques to handle missing (`NaN`) dataset variables safely:
* **Mean Imputer:** Replaces missing variables with the evaluated mathematical average of the feature column.
* **Median Imputer:** Uses the central trend median to bypass data skewness issues.
* **KNN Imputer:** Integrates a $K$-Nearest Neighbors model to intelligently infer values based on similar acoustic properties.

### 2. Statistical Outlier Handling
To prevent anomalous entries from skewing data insights, two distinct filtering layers are included:
* **IQR Method (Interquartile Range):** Identifies and filters outliers beyond the standard 1.5 IQR boundary.
* **Z-Score Method:** Evaluates data dispersion relative to standard deviations from the dataset mean.

### 3. Dynamic Data Loading & Instant Append
* **Atomic I/O Operations:** Implements memory-efficient data loading capable of handling massive datasets (100,000+ entries) flawlessly.
* **Live Appending:** Allows real-time user addition of new songs via interactive terminal prompts, automatically syncing the on-disk file storage (in append mode) and active RAM cache simultaneously.

### 4. Advanced Analytics & Data Storytelling
Deep data insights are rendered through clear mathematical modeling and visual structures:
* **Box Plots:** For illustrating distribution spreads and tracking data purity before and after outlier removals.
* **Correlation Matrix Heatmaps:** Unveiling systemic statistical dependencies across distinct musical characteristics (e.g., Loudness vs. Acousticness).

### 5. Interactive CLI Dashboard
Features a fully managed, error-proof Command-Line Interface menu loop that catches user exceptions gracefully to prevent crashes.

---

## 🗂️ Directory & File Structure

The workspace follows a strict modular structure to maintain a clear separation of concerns:

```text
spotify_studio/
│
├── data/
│   └── spotify_tracks.csv       # The main Spotify dataset containing audio features
│
└── src/
    ├── __init__.py              # Python package initialization file
    ├── data_loader.py           # Handles secure file streaming, RAM synchronization & appending
    ├── data_cleaner.py          # Formulates the OOP structure for Imputers & Outlier Handlers
    ├── data_analyzer.py         # Conducts calculations for insights and correlation metrics
    ├── data_visualizer.py       # Draws publication-grade plots (Box Plots, Heatmaps)
    └── main.py                  # The main application orchestration file and interactive CLI