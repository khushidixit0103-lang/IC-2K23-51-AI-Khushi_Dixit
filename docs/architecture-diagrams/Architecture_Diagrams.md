# System & Algorithm Architecture Diagrams

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D  
**Subject:** Artificial Intelligence Lab  

---

## 1. Production Rule Forward-Chaining Engine (Lab 1 & Lab 4)

```mermaid
flowchart TD
    WM["Working Memory (Facts & Assertions)"] --> MATCH["Pattern Matcher (Evaluate Antecedents)"]
    KB["Rule Base (IF P THEN C)"] --> MATCH
    MATCH --> CS["Conflict Set (Triggered Rules)"]
    CS --> RESOLVE["Conflict Resolution (Priority / Recency)"]
    RESOLVE --> FIRE["Execution Engine (Fire Rule Consequent)"]
    FIRE -->|"Assert New Fact"| WM
    FIRE --> AUDIT["Execution Audit Log"]
```

---

## 2. A* Search Evaluation Cycle (Lab 2)

```mermaid
flowchart TD
    START(["Start Node S0"]) --> OPEN["Priority Queue (Open List)"]
    OPEN -->|"Pop node with min f(n) = g(n) + h(n)"| CURRENT["Current Node N"]
    CURRENT --> GOAL{"Is N Goal?"}
    GOAL -->|"Yes"| SUCCESS(["Reconstruct Optimal Path"])
    GOAL -->|"No"| CLOSED["Add N to Closed List"]
    CURRENT --> EXPAND["Generate Successors M"]
    EXPAND --> EVAL["Compute g(M), h(M), f(M)"]
    EVAL -->|"If M not in Closed or lower cost"| OPEN
```

---

## 3. Machine Learning Decision Pipeline (Lab 5)

```mermaid
flowchart LR
    RAW["Raw Dataset (CSV)"] --> PRE["Data Preprocessing & Cleaning"]
    PRE --> SPLIT["80:20 Stratified Partition"]
    SPLIT --> TRAIN["Training Set (24 samples)"]
    SPLIT --> TEST["Test Set (6 samples)"]
    TRAIN --> INDUCT["Decision Tree Induction (Min Gini Impurity)"]
    INDUCT --> MODEL["Trained Tree Model"]
    TEST --> INFER["Hold-out Inference"]
    MODEL --> INFER
    INFER --> EVAL["Evaluation Metrics (Confusion Matrix, F1-Score)"]
```

---

## 4. Deep Learning Training & Backprop Loop (Lab 6)

```mermaid
flowchart TD
    BATCH["Mini-Batch Input X, Ground Truth Y"] --> FORWARD["Forward Pass (Affine Dot Product + ReLU)"]
    FORWARD --> PREDICT["Output Activation (Sigmoid/Softmax)"]
    PREDICT --> LOSS["Loss Computation (Cross-Entropy / MSE)"]
    LOSS --> BACKWARD["Backpropagation (Chain Rule dL/dW, dL/db)"]
    BACKWARD --> OPTIM["Optimizer Step (SGD / Adam: Update Weights)"]
    OPTIM --> EPOCH{"Epoch Finished?"}
    EPOCH -->|"Next Batch"| BATCH
    EPOCH -->|"Complete"| VAL["Validation Evaluation & Loss Logging"]
```

---

## 5. Grad-CAM Visual Explainability Pipeline (Lab 7)

```mermaid
flowchart LR
    IMG["Input Image"] --> CNN["Conv Layers Backbone"]
    CNN --> ACT["Terminal Conv Activation Maps A^k"]
    ACT --> HEAD["Classification Head"]
    HEAD --> SCORE["Target Class Score Y^c"]
    SCORE --> GRAD["Backprop Gradient dY^c / dA^k"]
    GRAD --> GAP["Global Average Pooling (Weights alpha_k)"]
    ACT --> COMB["Weighted Linear Combination"]
    GAP --> COMB
    COMB --> RELU["ReLU Filter (Positive Evidence)"]
    RELU --> HEATMAP["Grad-CAM Saliency Map"]
    HEATMAP --> OVERLAY["Superimposed Heatmap on Input"]
```
