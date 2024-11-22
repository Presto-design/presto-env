import unittest
from unittest.mock import patch

from presto_env.modal import MODAL_GPU_PER_HOUR_PRICE, get_modal_gpu_price_per_hour


class TestModal(unittest.TestCase):

    @patch("torch.cuda.is_available", return_value=True)
    @patch("torch.cuda.get_device_name", return_value="NVIDIA A100-SXM4-80GB")
    @patch("torch.cuda.device_count", return_value=2)
    def test_get_modal_gpu_price_per_hour(
        self, mock_is_available, mock_get_device_name, mock_device_count
    ):
        price = get_modal_gpu_price_per_hour()
        self.assertEqual(price, MODAL_GPU_PER_HOUR_PRICE["NVIDIA A100-SXM4-80GB"] * 2)
