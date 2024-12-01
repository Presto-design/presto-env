from pathlib import Path
import unittest
from presto_env.env import PrestoEnv
from presto_env.run import generate_run_id
from presto_env.modal import get_modal_gpu_price_per_hour, MODAL_GPU_PER_HOUR_PRICE
import os
from unittest.mock import patch


class TestPrestoEnv(unittest.TestCase):

    @patch.dict(os.environ, {PrestoEnv.PRESTO_HOME: "./test_presto_home"})
    def test_get_temp_folder(self):
        temp_folder = PrestoEnv.create_temp_folder()
        self.assertTrue(temp_folder.exists())
        print(temp_folder)
        self.assertTrue(str(temp_folder).startswith("test_presto_home/temporary/"))

    @patch.dict(os.environ, {PrestoEnv.PRESTO_HOME: "./test_presto_home"})
    def test_get_run_folder(self):
        run_folder = PrestoEnv.run_folder("project", "run_id")
        self.assertEqual(run_folder, Path("./test_presto_home/runs/project/run_id"))

    @patch.dict(os.environ, {PrestoEnv.PRESTO_HOME: "./test_presto_home"})
    def test_get_bulk_assets_folder(self):
        bulk_assets_folder = PrestoEnv.bulk_assets_folder()
        self.assertEqual(bulk_assets_folder, Path("./test_presto_home/bulk_assets"))

    @patch.dict(os.environ, {PrestoEnv.PRESTO_HOME: "./test_presto_home"})
    def test_get_datasets_folder(self):
        datasets_folder = PrestoEnv.datasets_folder()
        self.assertEqual(datasets_folder, Path("./test_presto_home/datasets"))


if __name__ == "__main__":
    unittest.main()
