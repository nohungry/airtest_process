# import sqlite3

# coordinate = sqlite3.connect("coordinate.db")

# class Database():
#     def __init__(self):
#         self.connection = sqlite3.connect("../coordinate.db")
#         self.cursor = self.connection.cursor()

#     def db_close(self):
#         self.connection.close()

#     def 

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///coordinate.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()

metadata = MetaData()

base = declarative_base()

connection = engine.connect()

ex_table = Table("deepseaposition", metadata, autoload=True, autoload_with=engine)

ret = session.execute(ex_table.insert(), {"phoneUDID": "1576457605007R5", 
                                          "spin": "540, 1966",
                                          "addition": "772, 1905",
                                          "subtraction": "300, 1904",
                                          "lighting": "917, 2038",
                                          "loop": "177, 2022",
                                          "autoloop": "541, 1117",
                                          "autostart": "542, 1807",
                                          "contents": "1016, 1932",
                                          "lobby": "111, 1946",
                                          "record": "322, 1949",
                                          "recordcancel": "None",
                                          "rule": "539, 1942",
                                          "ruleswitch": "None",
                                          "rulecancel": "1002, 287",
                                          "musicsetting": "757, 1945",
                                          "settingcancel": "953, 912",
                                          "cancel": "965, 1903",
                                          "popout": "537, 1120",
                                          "confirm": "534, 1278",})

session.commit()
res = session.query(ex_table).first()
print(res)
pass