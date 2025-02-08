""" Configuration file for the project. """
import os

# Paths to directories
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PAIRS_SOURCE_DIR = os.path.join(BASE_DIR, 'pairs')
PAGES_SOURCE_DIR = os.path.join(BASE_DIR, 'pages')

OCR_OUTPUT_DIR = os.path.join(BASE_DIR, 'ocr_output')
LLM_OUTPUT_DIR = os.path.join(BASE_DIR, 'llm_output')

LLM_API_KEY = "openai-api-key"