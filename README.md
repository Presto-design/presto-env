    ███████ ██████████
    ███████ ████████████
    ███████ ██████████████
    ███████        ███████
    ███████         ██████
    ███████        ███████
    ███████       ████████
    ███████ █████████████
    ███████ ████████████
    ███████ █████████
    ███████
    ███████
    ███████
    ██████
    ████

# Presto

This package helps our constellation of packages to know where to store data, and where they're running

## Env vars

Presto will try to use the following environment variables, and fallback if they do not exist:

- `PRESTO_RUNS` This is the directory to store run data locally (e.g. `$PRESTO_RUNS/:project/:run_id`). Will default to the root of the repo being run
- `PRESTO_DATASETS` This is a directory to save datasets as we build them locally (e.g. save the HF arrow files, save other artifacts we create)
- `PRESTO_BULK_ASSETS` This is where we store down the large scale asset folders (e.g. from Himalaya)
- `PRESTO_TEMPORARY` Where to create temporary folders. Falls back to system temp (the purpose of this is to not fill your primary hard drive with huge temp files)

## Example usage

```python
from presto_env import ModalEnv
from presto_env.run import generate_run_id
run_dir = ModalEnv.run_folder("ppo_himalaya", generate_run_id())

temp_dir = ModalEnv.create_temp_folder()

```
