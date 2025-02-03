# README

This repo contains a wrapper-class for the elabFTW API to connect to the API via Python and create ressoruces programmatically. It serves as an entry point on how to interact with the API which is documented here: (API Docs: https://doc.elabftw.net/api/v2/)

## Installation

### Using `uv`

This is the preferrable way as it also installs and manages the Python Installation for you (https://docs.astral.sh/uv/guides/install-python/)

- Install`uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Run Jupyter: `uvx jupyter notebook`

Installation of `uv` on Windows: https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2

### Using `pip`

This assuems that you have Python 3.10 or higher installed on your computer. (Look into https://github.com/pyenv/pyenv for that)

- Create a virtual environment: `python3 -m venv .venv`
- Acrivate it: `source .venv/bin/activate`
- Install rquired packages: `pip install -r requirements.txt`
- Run Jupyter: `jupyter notebook`
- Continue in the browser

### Using `pipenv`

This assuems that you have Python 3.10 or higher _and_ `pipenv` installed on your computer. (Look into https://github.com/pyenv/pyenv for that)

- `pipenv install`
- `pipenv shell`
- Run Jupyter: `jupyter notebook`
- Continue in the browser

## Usage

- Open `Create_ressources.ipynb` in the Jupyter Notebook environment.
- Create an API Key in elabFTW
- Paste it in the cell containing `API_KEY = ""` like `API_KEY = "21-281392723209017a789ahiuduhed783e2huiwdqjbkxsa789z2e4efb56cd858f121"`
- Run all cells
- Check created ressources