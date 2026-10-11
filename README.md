# AI Club workshops

Workshop materials for AI at UC Riverside, collected in their original teaching sequence. Each lesson keeps its own scripts, instructions, and environment.

| Lesson | What to run | Dependencies and resources |
| --- | --- | --- |
| [01 · PyTorch setup](workshops/01-pytorch-setup/README.md) | `main.py`; optional `transformer.py` | Torch/NumPy run locally; sentiment analysis downloads a public Hugging Face model |
| [02 · Linear regression](workshops/02-linear-regression/README.md) | `main.py`; `housing.py` | Torch, NumPy, Matplotlib, scikit-learn; housing downloads the California housing dataset |
| [Mini · Gemini API keys](workshops/mini-gemini-api-keys/README.md) | `main.py` | Historical hosted Gemini example; requires the learner's own key and an available model |

## Run a lesson independently

Clone this collection, then work inside the lesson directory. Python 3.12 was used for the consolidation checks. For example, from the collection root:

```bash
cd workshops/01-pytorch-setup
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Deactivate with `deactivate` before creating another lesson's environment. Follow the linked lesson README for its other entrypoints and optional requirements. Workshop 2 builds on Workshop 1 conceptually; it runs from its own folder without importing Workshop 1.

Package installation needs internet access. After installation, tensor addition and synthetic regression run locally. `transformer.py` downloads model/tokenizer files on first use; `housing.py` downloads public data on first use. Later runs can reuse the libraries' local caches. Regression scripts open Matplotlib plots; `MPLBACKEND=Agg python main.py` runs without GUI windows.

The Gemini lesson keeps the original `google.generativeai` client, `gemini-1.5-flash` model name, prompts, and 100-token response limit. That historical model may be unavailable. Hosted requests were not verified; the source is retained as a historical lesson. The local lessons need no API key or account. Do not commit `.env` files or keys.

## Sources and attribution

[ATTRIBUTION.md](ATTRIBUTION.md) identifies the original repositories and contributors. [SOURCES.json](SOURCES.json) records every imported file, original commit/tree/blob SHA, retained path, and documentation edit. Original Git histories are ancestors of this collection's `main`, including after the consolidation PR's squash merge; `git log <source-sha>` and `git show <source-sha>:<original-path>` work in a full clone without the original repositories. A shallow clone must be unshallowed first. Existing lesson document and social links are preserved. The two linked workshop documents also have attributed plain-text snapshots in their lesson folders; historical text and export formatting are retained. No collection-wide license has been added.
