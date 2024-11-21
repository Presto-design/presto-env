import os
import torch


def IS_MODAL_REMOTE():
    return os.environ.get("MODAL_IS_REMOTE", "0") == "1"


MODAL_GPU_PER_HOUR_PRICE = {
    "NVIDIA H100 80GB HBM3": 4.56,
    "NVIDIA H100": 4.56,
    "NVIDIA A100-SXM4-80GB": 3.40,
    "NVIDIA A100-SXM4-40GB": 2.78,
    "NVIDIA A10": 1.10,
    "NVIDIA L4": 0.80,
    "Tesla T4": 0.59,
    "cpu": 0.135,
}


def get_modal_gpu_price_per_hour() -> float | None:

    gpu_name = None
    gpu_count = 1
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name()
        gpu_count = torch.cuda.device_count()

    if gpu_name is None:
        return MODAL_GPU_PER_HOUR_PRICE["cpu"]

    if gpu_name in MODAL_GPU_PER_HOUR_PRICE:
        return MODAL_GPU_PER_HOUR_PRICE[gpu_name] * gpu_count

    raise ValueError(f"Unknown GPU: {gpu_name}")
