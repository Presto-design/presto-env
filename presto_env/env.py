from datetime import datetime
import os
from pathlib import Path
import tempfile
import uuid

from presto_env.modal import IS_MODAL_REMOTE


class PrestoEnv:

    PRESTO_HOME = "PRESTO_HOME"

    @staticmethod
    def create_temp_folder() -> Path:
        if PrestoEnv.PRESTO_HOME in os.environ:
            folder_name = f"{datetime.now().strftime('%Y%m%d-%H-%M')}_{uuid.uuid4()}"
            path = Path(os.environ[PrestoEnv.PRESTO_HOME]) / "temporary" / folder_name
            path.mkdir(parents=True, exist_ok=True)
            return path
        else:
            path = Path(tempfile.gettempdir())
            return path

    @staticmethod
    def run_folder(project: str, run_id: str) -> Path:
        if IS_MODAL_REMOTE():
            # You're running in the run folder!
            return Path("./")
        else:
            if PrestoEnv.PRESTO_HOME in os.environ:
                path = (
                    Path(os.environ[PrestoEnv.PRESTO_HOME]) / "runs" / project / run_id
                )
                path.mkdir(parents=True, exist_ok=True)
                return path
            else:
                return Path("./runs") / project / run_id

    @staticmethod
    def bulk_assets_folder() -> Path:
        if not PrestoEnv.PRESTO_HOME in os.environ:
            raise EnvironmentError(
                f"Please set ${PrestoEnv.PRESTO_HOME} environment variable"
            )

        return Path(os.environ[PrestoEnv.PRESTO_HOME]) / "bulk_assets"

    @staticmethod
    def datasets_folder() -> Path:
        if PrestoEnv.PRESTO_HOME in os.environ:
            return Path(os.environ[PrestoEnv.PRESTO_HOME]) / "datasets"
        else:
            return Path("./datasets")
