from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from setup_psql_env import get_database
from sqlalchemy.ext.declarative import declarative_base

import models

# Setup environment and create a session
db = get_database()
Session = sessionmaker(bind=db)
session = Session()

meta = MetaData()
meta.bind = db

# Create database from SQLAlchemy models
models.Base.metadata.create_all(db)