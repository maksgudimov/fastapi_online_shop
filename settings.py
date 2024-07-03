import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


engine = create_engine(f"postgresql+psycopg2://"
                       f"{env('DB_USERNAME')}:"
                       f"{env('DB_PASSWORD')}@"
                       f"{env('DB_HOSTNAME')}/"
                       f"{env('DB_NAME')}",
                       echo=True,)


engine.connect()
