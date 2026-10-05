# environments_mpm

A small demo package (`envtest`) used in Lecture 1 of Modern Programming Methods,
"GitHub and Python environments". Fork this repository into your personal GitHub
account, clone your fork, and follow the instructions in the lecture notes.

The runtime dependencies are declared in `pyproject.toml`. Create the Conda
environment with `conda env create -f environment.yml`, or install the project
into an active Python environment with `pip install -e .` (equivalently,
`pip install -r requirements.txt`). The example scripts can then be run from the
repository root, including `python scripts/summarize_measurements.py`.

A worked solution to the lecture's exercises is on the `2026final` branch, which is
added after the lecture.
