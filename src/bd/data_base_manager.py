import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.path_utils import get_database_path


logger = logging.getLogger(__name__)

class DataBaseManager:
    def __init__(self):
        db_file = get_database_path()
        db_path = f"sqlite:///{db_file}"
        print(db_path)
        try:
            self.engine = create_engine(db_path, echo=False)
            self.Session = sessionmaker(bind=self.engine)
        except Exception as e:
            logger.error(f"Ошибка инициализации базы данных: {str(e)}")
            raise

    def get_session(self):
        try:
            return self.Session()
        except Exception as e:
            logger.error(f"Ошибка создания сессии: {str(e)}")
            raise

    def close(self):
        try:
            self.engine.dispose()
        except Exception as e:
            logger.error(f"Ошибка закрытия соединений: {str(e)}")
            raise