from config import DECISION_TYPES

# If you want to train or test an established model and/or start with established memories fill out the info below.
# The established model/memories should be in  /run_archive/<name of game>/run00##/
# You can just paste the entire run folder into /run_archive/<name of game>/  then change run to "run####" where #### is a 4 digit number (0001, 0002, 0003, etc.)

INITIAL_RUN_NUMBER = None
INITIAL_MODEL_VERSION = [None for d_t in range(DECISION_TYPES)]
INITIAL_MEMORY_VERSION = [None for d_t in range(DECISION_TYPES)]
INITIAL_ITERATION = None 
"""
INITIAL_RUN_NUMBER = 5
INITIAL_MODEL_VERSION = [32 for d_t in range(DECISION_TYPES)]
INITIAL_MEMORY_VERSION = [65 for d_t in range(DECISION_TYPES)]
INITIAL_ITERATION = None """