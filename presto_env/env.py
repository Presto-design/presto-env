from datetime import datetime
import os
from pathlib import Path
import tempfile
import uuid

from presto_env.modal import IS_MODAL_REMOTE


class PrestoEnv:

    PRESTO_TEMPORARY = "PRESTO_TEMPORARY"
    PRESTO_BULK_ASSETS = "PRESTO_BULK_ASSETS"
    PRESTO_RUNS = "PRESTO_RUNS"
    PRESTO_DATASETS = "PRESTO_DATASETS"

    @staticmethod
    def get_temp_folder() -> Path:
        if PrestoEnv.PRESTO_TEMPORARY in os.environ:
            folder_name = f"{datetime.now().strftime('%Y%m%d-%H-%M')}_{uuid.uuid4()}"
            path = Path(os.environ[PrestoEnv.PRESTO_TEMPORARY]) / folder_name
            path.mkdir()
            return path
        else:
            path = Path(tempfile.gettempdir())
            return path

    @staticmethod
    def get_run_folder(project: str, run_id: str) -> Path:
        if IS_MODAL_REMOTE():
            # You're running in the run folder!
            return Path("./")
        else:
            if PrestoEnv.PRESTO_RUNS in os.environ:
                return Path(os.environ(PrestoEnv.PRESTO_RUNS)) / project / run_id
            else:
                return Path("./runs") / project / run_id

    @staticmethod
    def get_bulk_assets_folder() -> Path:
        if not PrestoEnv.PRESTO_BULK_ASSETS in os.environ:
            raise EnvironmentError(
                f"Please set ${PrestoEnv.PRESTO_BULK_ASSETS} environment variable"
            )

        return Path(os.environ[PrestoEnv.PRESTO_BULK_ASSETS])

    @staticmethod
    def get_datasets_folder() -> Path:
        if PrestoEnv.PRESTO_DATASETS in os.environ:
            return Path(os.environ[PrestoEnv.PRESTO_DATASETS])
        else:
            return Path("./datasets")
