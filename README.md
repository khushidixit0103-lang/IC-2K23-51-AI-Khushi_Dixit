# Artificial Intelligence Lab Repository

**Course Code:** IC-709D / IC-703 C  
**Subject:** Artificial Intelligence Lab  
**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Department / Institute:** International Institute of Professional Studies (IIPS), DAVV  

---

## 📌 Repository Overview

This repository contains the complete laboratory curriculum implementations, datasets, models, visualizations, and documentation for the **Artificial Intelligence Lab** as prescribed by the university syllabus.

Each laboratory experiment is structured into dedicated self-contained directories containing:
- Modular, PEP-8 compliant Python source code (`.py`) / Jupyter Notebooks (`.ipynb`)
- Dedicated documentation (`README.md`) with problem statements, algorithms, input/output specifications, execution instructions, and learning outcomes
- Genuine experimental results and generated plots/visualizations

---

## 📂 Directory Structure

```text
IC-2K23-51-AI-Dishan_Sheikh/
├── Lab1/                  # AI Problem Formulation & Intelligent Problem Solving (CO1)
├── Lab2/                  # Heuristic Search Algorithms (CO2)
├── Lab3/                  # AI Programming Frameworks & Data Preparation (CO2, CO5)
├── Lab4/                  # Knowledge Representation & Logical Reasoning (CO1, CO3)
├── Lab5/                  # Machine Learning for Intelligent Decision Making (CO4, CO5)
├── Lab6/                  # Deep Learning Fundamentals using PyTorch (CO4, CO5)
├── Lab7/                  # Explainable AI, Adversarial AI & Advanced Applications (CO4, CO5)
├── datasets/              # Shared datasets used across experiments
├── models/                # Saved models, serialized weights, and checkpoints
├── docs/                  # Flowcharts, architecture diagrams, reports, and analysis
│   ├── algorithm-flowcharts/
│   ├── architecture-diagrams/
│   ├── performance-analysis/
│   └── reports/
├── requirements.txt       # Project dependencies
├── .gitignore             # Standard git exclusions
└── README.md              # Repository overview and documentation
```

---

## 📑 Syllabus & Lab Mapping

| Lab | Topic | Experiments / Core Activities | Course Outcomes |
|---|---|---|---|
| **Lab 1** | AI Problem Formulation & Intelligent Problem Solving | Production Rule Systems, Water Jug Problem, Missionaries & Cannibals Problem, Vacuum Cleaner Problem, State-Space Representation, Rule-based Decision Making | CO1 |
| **Lab 2** | Heuristic Search Algorithms | Generate & Test, Breadth-First Search (BFS), Depth-First Search (DFS), Hill Climbing, Best-First Search, A* Search, 8-Puzzle, Maze Solver, Route Planning | CO2 |
| **Lab 3** | AI Programming Frameworks & Data Preparation | NumPy, Pandas, Matplotlib, Data Cleaning, Missing Value Handling, Label Encoding, Feature Selection, Data Visualization | CO2, CO5 |
| **Lab 4** | Knowledge Representation & Logical Reasoning | Rule-based Representation, Predicate Representation, Semantic Networks, Frames, Conceptual Dependency, Logical Inference Engine | CO1, CO3 |
| **Lab 5** | Machine Learning for Intelligent Decision Making | Feature Matrix Creation, Decision Tree Classifier, Evaluation Metrics, Decision Tree Visualization (Placement, Disease, Loan) | CO4, CO5 |
| **Lab 6** | Deep Learning Fundamentals using PyTorch | Tensors, Autograd, Linear Regression, Neural Network Basics, Loss Functions, Optimizers, Training Loops, Model Evaluation | CO4, CO5 |
| **Lab 7** | Explainable AI & Adversarial AI | Grad-CAM Visualization, Fast Gradient Sign Method (FGSM), ResNet Image Classification, PCA Dimensionality Reduction | CO4, CO5 |

---

## 🛠️ Environment Setup & Installation

### Prerequisites
- Python 3.10+ (Recommended Python 3.11 or 3.12)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anonymousclient/IC-2K23-51-AI-Dishan_Sheikh.git
   cd IC-2K23-51-AI-Dishan_Sheikh
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows (Command Prompt / PowerShell):
   .\venv\Scripts\activate
   # On Linux / macOS:
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```


---

## 🚀 Complete Experiment Execution Index

| Lab | Experiment Directory | Primary Python Script | Execution Command |
|---|---|---|---|
| **Lab 1** | Lab1/Production_Rule_System/ | production_system.py | python Lab1/Production_Rule_System/production_system.py |
| | Lab1/Water_Jug_Problem/ | water_jug.py | python Lab1/Water_Jug_Problem/water_jug.py |
| | Lab1/Missionaries_Cannibals/ | missionaries_cannibals.py | python Lab1/Missionaries_Cannibals/missionaries_cannibals.py |
| | Lab1/Vacuum_Cleaner/ | acuum_cleaner.py | python Lab1/Vacuum_Cleaner/vacuum_cleaner.py |
| | Lab1/State_Space_Representation/ | state_space.py | python Lab1/State_Space_Representation/state_space.py |
| | Lab1/Rule_Based_Decision_Making/ | decision_system.py | python Lab1/Rule_Based_Decision_Making/decision_system.py |
| **Lab 2** | Lab2/Generate_And_Test/ | generate_and_test.py | python Lab2/Generate_And_Test/generate_and_test.py |
| | Lab2/BFS/ | fs.py | python Lab2/BFS/bfs.py |
| | Lab2/DFS/ | dfs.py | python Lab2/DFS/dfs.py |
| | Lab2/Hill_Climbing/ | hill_climbing.py | python Lab2/Hill_Climbing/hill_climbing.py |
| | Lab2/Best_First_Search/ | est_first_search.py | python Lab2/Best_First_Search/best_first_search.py |
| | Lab2/A_Star/ | _star.py | python Lab2/A_Star/a_star.py |
| | Lab2/Eight_Puzzle/ | eight_puzzle.py | python Lab2/Eight_Puzzle/eight_puzzle.py |
| | Lab2/Maze_Solver/ | maze_solver.py | python Lab2/Maze_Solver/maze_solver.py |
| | Lab2/Route_Planning/ | 
oute_planner.py | python Lab2/Route_Planning/route_planner.py |
| | Lab2/Heuristic_Comparison/ | comparison.py | python Lab2/Heuristic_Comparison/comparison.py |
| **Lab 3** | Lab3/Dataset_Loading_EDA/ | eda.py | python Lab3/Dataset_Loading_EDA/eda.py |
| | Lab3/Data_Cleaning_Missing_Values/ | cleaning.py | python Lab3/Data_Cleaning_Missing_Values/cleaning.py |
| | Lab3/Data_Encoding/ | encoding.py | python Lab3/Data_Encoding/encoding.py |
| | Lab3/Feature_Engineering_Selection/ | eature_engineering.py | python Lab3/Feature_Engineering_Selection/feature_engineering.py |
| **Lab 4** | Lab4/Rule_Based_KR/ | 
ule_based.py | python Lab4/Rule_Based_KR/rule_based.py |
| | Lab4/Predicate_Logic/ | predicate_logic.py | python Lab4/Predicate_Logic/predicate_logic.py |
| | Lab4/Semantic_Network/ | semantic_network.py | python Lab4/Semantic_Network/semantic_network.py |
| | Lab4/Frame_Representation/ | rame_representation.py | python Lab4/Frame_Representation/frame_representation.py |
| | Lab4/Logical_Inference_Engine/ | inference_engine.py | python Lab4/Logical_Inference_Engine/inference_engine.py |
| | Lab4/Conceptual_Dependency/ | conceptual_dependency.py | python Lab4/Conceptual_Dependency/conceptual_dependency.py |
| **Lab 5** | Lab5/Decision_Tree_Classifier/ | decision_tree.py | python Lab5/Decision_Tree_Classifier/decision_tree.py |
| | Lab5/Student_Placement_Prediction/ | placement_prediction.py | python Lab5/Student_Placement_Prediction/placement_prediction.py |
| | Lab5/Disease_Prediction/ | disease_prediction.py | python Lab5/Disease_Prediction/disease_prediction.py |
| | Lab5/Loan_Approval_Prediction/ | loan_prediction.py | python Lab5/Loan_Approval_Prediction/loan_prediction.py |
| **Lab 6** | Lab6/Tensor_Operations/ | 	ensor_ops.py | python Lab6/Tensor_Operations/tensor_ops.py |
| | Lab6/Autograd_Differentiation/ | utograd_demo.py | python Lab6/Autograd_Differentiation/autograd_demo.py |
| | Lab6/Linear_Regression_DL/ | linear_regression.py | python Lab6/Linear_Regression_DL/linear_regression.py |
| | Lab6/Neural_Network_Basics/ | 
eural_network.py | python Lab6/Neural_Network_Basics/neural_network.py |
| | Lab6/Model_Training_Evaluation/ | 	rain_evaluate.py | python Lab6/Model_Training_Evaluation/train_evaluate.py |
| **Lab 7** | Lab7/Feature_Importance_XAI/ | eature_importance.py | python Lab7/Feature_Importance_XAI/feature_importance.py |
| | Lab7/PCA_Dimensionality_Reduction/ | pca_demo.py | python Lab7/PCA_Dimensionality_Reduction/pca_demo.py |
| | Lab7/FGSM_Adversarial/ | gsm_demo.py | python Lab7/FGSM_Adversarial/fgsm_demo.py |
| | Lab7/GradCAM_Visualization/ | gradcam_demo.py | python Lab7/GradCAM_Visualization/gradcam_demo.py |
| | Lab7/Transfer_Learning_Demo/ | 	ransfer_learning.py | python Lab7/Transfer_Learning_Demo/transfer_learning.py |

---

## 📊 Comprehensive Reports & Visualizations

- [Lab Report Summary](docs/reports/Lab_Report_Summary.md)
- [Cross-Lab Performance Analysis](docs/performance-analysis/Performance_Analysis_Report.md)
- [System Architecture Diagrams](docs/architecture-diagrams/Architecture_Diagrams.md)
