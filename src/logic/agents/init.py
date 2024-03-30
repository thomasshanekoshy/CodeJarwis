import os

from logic.config import Config
from logic.logger import Logger

from logic.keyword_extraction.BERT_extractor import Extractor

def init_devika():
    config = Config()
    logger = Logger()

    logger.info("Initializing Devika...")
    sqlite_db = config.get_sqlite_db()
    screenshots_dir = config.get_screenshots_dir()
    pdfs_dir = config.get_pdfs_dir()
    projects_dir = config.get_projects_dir()
    logs_dir = config.get_logs_dir()

    logger.info("Initializing Prerequisites Jobs...")
    os.makedirs(os.path.dirname(sqlite_db), exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)
    os.makedirs(pdfs_dir, exist_ok=True)
    os.makedirs(projects_dir, exist_ok=True)
    os.makedirs(logs_dir, exist_ok=True)
    
    

    logger.info("Loading sentence-transformer BERT models...")
    prompt = "Light-weight keyword extraction excercise for BERT model loading.".strip()
    Extractor(prompt).extract_keywords()
    logger.info("BERT model loaded successfully.")