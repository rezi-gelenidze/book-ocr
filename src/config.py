""" Configuration file for the project. """
import os

# Paths to directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RAW_SOURCE_DIR = os.path.join(BASE_DIR, 'raw')
OPTIMIZED_SOURCE_DIR = os.path.join(BASE_DIR, 'optimized')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
REVISED_SOURCE_DIR = os.path.join(BASE_DIR, 'revised')

LLM_API_KEY = "OPENAI_API_KEY"