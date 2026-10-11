## Running from this collection

From the collection root, enter `workshops/01-pytorch-setup`. For a standalone environment (checked with Python 3.12):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

For the optional sentiment example:

```bash
python -m pip install -r requirements-sentiment.txt
python transformer.py
```

The tensor example runs locally after installation. Sentiment analysis uses the original default Hugging Face pipeline and downloads a public model/tokenizer on first use; the optional manifest retains Transformers 4 for that API. The historical Python 3.8/Anaconda and copy-the-script instructions below are preserved; this collection already includes both scripts. A [text snapshot of the linked workshop document](workshop-notes.txt) is included for offline reading. Its original wording and export formatting are retained; the original document link remains below.

---

# Workshop 1: Tools and Software (PyTorch Installations and Dependencies)

#### Script with more In-Depth Explanation
 - https://docs.google.com/document/d/1DZFyE8RZvltkBdzuq8VtBDb110S4A16S-Wr5XswysCI/edit?usp=sharing

## Introduction
Welcome to the AI Club's first technical workshop focused on PyTorch installations and dependencies. This workshop is designed to lay a strong foundation for your journey in AI, with an emphasis on understanding the basics of PyTorch.

## Setting Up Your Environment

### Installing Anaconda
1. Download Anaconda from [Anaconda's website](https://www.anaconda.com/download).
2. Install Anaconda by following the on-screen prompts.

### Installing PIP
- PIP is a package manager for Python, used to install and manage additional packages.
- Install PIP from [here](https://pypi.org/project/pip/).

### Creating Your Python Environment
- conda create -n pytorch3.8 python=3.8

### Activate the environment
 - conda activate pytorch3.8

### To see your environments
 - conda env list

### To deactivate the environment
 - conda deactivate

### Install PyTorch
 - pip install torch

### Install NumPy
 - pip install numpy

# Creating Your First PyTorch Script
 - Open VSCode and create a new folder for your project. Within this folder, create a file named main.py.

 - Copy the code from main.py:

# Run the script
 - python main.py

# Advanced Example: Sentiment Analysis with PyTorch

### Creating the Sentiment Analysis Script
 - Create a new Python file named transformer.py in your project directory.
 - Copy the the code from transformer.py:

### Run the script
 - python transformer.py

# Conclusion
Thank you for participating in our workshop. We hope this README helps you set up and explore PyTorch effectively. Don't hesitate to reach out to us if you have any questions or need further assistance.

### Social Links: 
 - Discord: https://discord.gg/tmd2hQE4SK 
 - Instagram: https://www.instagram.com/ucrai_/  
 - Highlander Link: https://highlanderlink.ucr.edu/organization/ai_at_ucr 
 - LinkedIn: https://www.linkedin.com/company/ai-at-ucr/ 

