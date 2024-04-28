from app.ingestion import run
import logging

# Configure logging
log_format = ("%(asctime)s - %(levelname)s - %(name)s "
              "- %(funcName)s - %(message)s")

logging.basicConfig(format=log_format,
                    level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    run()
