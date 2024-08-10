import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# import pymysql

# connection = pymysql.connect(
#   host = "gateway01.us-east-1.prod.aws.tidbcloud.com",
#   port = 4000,
#   user = "2d1KPCHFnP4uEtv.root",
#   password = "<PASSWORD>",
#   database = "test",
#   ssl_verify_cert = True,
#   ssl_verify_identity = True,
#   ssl_ca = "<CA_PATH>"
# )

engine = create_engine(db_connection_string, 
                   connect_args=  {
                        "ssl": {
                          "ssl_ca": "C:\\Users\\TAGORE\\Downloads\\isrgrootx1.pem"
                        }
                      }
                      )




def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()