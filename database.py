import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://2d1KPCHFnP4uEtv.root:Px4FYj0q6GtBTKiC@gateway01.us-east-1.prod.aws.tidbcloud.com/test")

