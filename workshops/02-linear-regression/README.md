## Running from this collection

From the collection root, enter `workshops/02-linear-regression`. Create this lesson's environment (checked with Python 3.12):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
python housing.py
```

`main.py` generates data locally. `housing.py` downloads the public California housing dataset through scikit-learn on first use, then reuses its cache. Both scripts display Matplotlib plots; use `MPLBACKEND=Agg python main.py` or `MPLBACKEND=Agg python housing.py` for a run without GUI windows. Random inputs and training results vary between runs. The original housing example's target shape can produce a broadcasting warning; its training behavior is preserved. A [text snapshot of the linked workshop document](workshop-notes.txt) is included for offline reading. Its original wording and export formatting are retained; the original document link remains below.

---

## Workshop 2: Dive Into Linear Regression with PyTorch

### Follow Along on GitHub
[Link to Workshop Document to Follow Along](https://docs.google.com/document/d/1DAKWIrIulB-Pldfk3CpiCNAQXdOjHC1D2bLJ_xgM_EY/edit?usp=sharing)

### Introduction
Welcome to the AI Club's second technical workshop! Building on our previous session on PyTorch installations and dependencies, today we're taking a step into the world of machine learning with a focus on linear regression using PyTorch. This workshop is designed to be interactive and hands-on, so get ready to code along and explore the basics of linear regression!

### Quick Recap of PyTorch
#### What is PyTorch?
- A toolbox for AI, mainly deep learning.
- Uses Python, making it easy to learn and use.

#### Key Features
- **User-friendly**: Great for beginners.
- **Flexible**: Like building with LEGO, it lets you create and modify AI models easily.
- **Debug-friendly**: Simplifies finding and fixing code issues.

### Understanding Linear Regression
#### What is Linear Regression?
- **Definition**: Linear Regression is a statistical method used in machine learning. It predicts a response (dependent variable) based on a single or multiple predictors (independent variables).
- **How It Works**: It finds a linear relationship between input variables (X) and an output variable (Y). This relationship is represented as Y = aX + b, where a is the slope and b is the intercept.

#### Why It's a Fundamental Concept in Machine Learning
- **Foundation for Understanding**: Linear regression is one of the simplest and most fundamental algorithms in machine learning. It lays the groundwork for understanding more complex models.
- **Interpretability**: It's straightforward and easy to interpret, making it a great starting point for those new to machine learning.
- **Basics of Model Training**: Learning linear regression introduces core concepts like loss functions, gradient descent, and overfitting, which are essential in more advanced machine learning algorithms.
