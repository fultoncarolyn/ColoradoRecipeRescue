import logging

from starter.environment import Environment

env = Environment.from_env()
logging.basicConfig(level=env.root_log_level)
logging.getLogger('starter').setLevel(level=env.starter_log_level)

print("Analyzing data")
