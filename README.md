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

## Environment Variable

Presto uses a single environment variable `PRESTO_HOME` to manage all data storage locations. The following subdirectories are automatically read/created under `PRESTO_HOME`:

- `/runs` - Stores run data locally (e.g. `$PRESTO_HOME/runs/:project/:run_id`)
- `/datasets` - Saves datasets as we build them locally (e.g. HF arrow files, other artifacts)
- `/bulk_assets` - Stores large scale asset folders (e.g. from Himalaya)
- `/temp` - Location for temporary folders (prevents filling primary hard drive with huge temp files)

If `PRESTO_HOME` is not set, most functions will fall back to local directories in the current working directory, except for bulk assets which requires the environment variable to be set.

## Example usage

```python
from presto_env import ModalEnv
from presto_env.run import generate_run_id
run_dir = ModalEnv.run_folder("ppo_himalaya", generate_run_id())

temp_dir = ModalEnv.create_temp_folder()
```
