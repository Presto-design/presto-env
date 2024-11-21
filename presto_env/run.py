import datetime

from presto_env.random import random_animal, random_short_adjective


def generate_run_id():
    return f"{datetime.now().strftime('%Y%m%d-%H-%M')}-{random_short_adjective().lower()}-{random_animal().lower()}"
