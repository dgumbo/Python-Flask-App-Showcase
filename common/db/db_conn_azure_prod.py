from sqlalchemy import create_engine

db_server="denzil.database.windows.net"
db_username="denzil"
db_password="Shorgan01"
db_name = "python-flask-test"
db_driver = 'SQL Server Native Client 11.0'

DATABASE_CONNECTION = f'mssql://{db_username}:{db_password}@{db_server}/{db_name}?driver={db_driver}'

# import urllib
# params = urllib.parse.quote_plus(f"DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};UID={db_username};PWD={db_password}")
# engine = create_engine(f"mssql+pyodbc://{db_username}:{db_password}@{db_server}")


# def db_config(app):
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc://{db_username}:{db_password}@{db_server}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db = SQLAlchemy(app)
#     return db
#     # db_model = db.Model
 
def db_connection_azure_prod(app):
    engine = create_engine(DATABASE_CONNECTION)
    connection = engine.connect()

    return connection

 