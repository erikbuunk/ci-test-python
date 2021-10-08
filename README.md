# dataroom-python

This Python framework is based ont the original Stata setup for the data room.

## Instructions

You can clone this project by clicking on the `Use this template`.

Do not feel that you have to fit you project in this structure. Use it as a starting point. After cloning you can adjust everything to your liking (remove/add scripts/directories) to your liking.

## Directory structure on X

`X:\Dataroom\` followed by a folder per doctoral student in the format"

```
<year>_<MPI username>
```

For example: `2021_buue`

Then a replicable folder for every chapter:

```
<year>_<MPI username>_Ch<n>_<name>
```

For example: `2021_buue_Ch1_Dataroom`

# Installation

- Optional: create a virtual or conda environment and activate this environment
- `pip install -r requirements.txt`

# Running the project

Update the `02_script/config.json` with the correct settings

```
$ cd 02_scripts
$ python main.py
```
