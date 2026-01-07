Daily-Codeforces
=================

Quick instructions to run the Python solutions locally.

**Prerequisites**
- Python 3.8 or newer installed.
- Optional: create and activate a virtual environment.

**Setup (recommended)**
- Create a virtual environment (PowerShell):

  python -m venv venv
  .\venv\Scripts\Activate.ps1

- Create a virtual environment (WSL / Linux / macOS):

  python3 -m venv venv
  source venv/bin/activate

- If a `requirements.txt` is present, install dependencies:

  pip install -r requirements.txt

**Run a solution**

Each script reads from standard input. Example for `1520D.py`:

1) Create a sample input file `input.txt` with the following contents:

```
1
5
1 2 3 3 4
```

This means: 1 test case, n=5, array = [1,2,3,3,4].

2) Run the script and provide the input file via stdin.

PowerShell / Windows:

  python 1520D.py < input.txt

WSL / Linux / macOS:

  python3 1520D.py < input.txt

Or use an inline input (WSL / bash):

  printf "1\n5\n1 2 3 3 4\n" | python3 1520D.py

**Notes**
- Scripts expect input from stdin and print output to stdout.
- No external dependencies are required for most problems in this repo.
- If you want, I can add simple test runners or example input files for each problem.
