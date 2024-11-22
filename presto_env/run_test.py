import unittest

from presto_env.run import generate_run_id


class TestRun(unittest.TestCase):

    def test_generate_run_id(self):
        run_id = generate_run_id()
        self.assertIsInstance(run_id, str)
        self.assertIn("-", run_id)
