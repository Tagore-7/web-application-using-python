import sqlalchemy

# print(sqlalchemy.__version__)

from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2d1KPCHFnP4uEtv.root:Px4FYj0q6GtBTKiC@gateway01.us-east-1.prod.aws.tidbcloud.com/test"

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

with engine.connect() as conn:
  
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())
  print(result_dicts)



  # print("type(result):", type(result))
  # result_all = result.all()
  # print("type(result.all())", type(result_all))
  # print("result.all():", result_all)
  # first_result = result_all[0]
  # print("type(first_result):", type(first_result))
  # first_result_dict = dict(result_all[0])
  # print(f"type(first_result_dict): {type(first_result_dict)}")
  # print(f"first_result_dict: {first_result_dict}")
  