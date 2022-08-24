# import sqlite3

# coordinate = sqlite3.connect("coordinate.db")

# class Database():
#     def __init__(self):
#         self.connection = sqlite3.connect("../coordinate.db")
#         self.cursor = self.connection.cursor()

#     def db_close(self):
#         self.connection.close()

#     def 

from sqlalchemy import create_engine, Table, MetaData, table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///coordinate.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# session = Session()

# metadata = MetaData()

# base = declarative_base()

# connection = engine.connect()

# ex_table = Table("deepseaposition", metadata, autoload=True, autoload_with=engine)

# ret = session.execute(ex_table.insert(), {"phoneUDID": "1576457605007R5", 
#                                           "spin": "540, 1966",
#                                           "addition": "772, 1905",
#                                           "subtraction": "300, 1904",
#                                           "lighting": "917, 2038",
#                                           "loop": "177, 2022",
#                                           "autoloop": "541, 1117",
#                                           "autostart": "542, 1807",
#                                           "contents": "1016, 1932",
#                                           "lobby": "111, 1946",
#                                           "record": "322, 1949",
#                                           "recordcancel": "None",
#                                           "rule": "539, 1942",
#                                           "ruleswitch": "None",
#                                           "rulecancel": "1002, 287",
#                                           "musicsetting": "757, 1945",
#                                           "settingcancel": "953, 912",
#                                           "cancel": "965, 1903",
#                                           "popout": "537, 1120",
#                                           "confirm": "534, 1278",})

# session.commit()
# res = session.query(ex_table).first()
# print(res)
# pass



# ----------------------------------------------

def connect_DB():
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    metadata = MetaData()
    base = declarative_base()
    connection = engine.connect()
    return engine, session, metadata, 

def use_table(table, metadata, engine):
    ex_table = Table(table, metadata, autoload=True, autoload_with=engine)

    return ex_table

def insert_value(session, ex_table, dataform):
    """
    session: upstairs session
    ex_table: upstaris target table
    dataform: dict type
    """
    session.execute(ex_table.insert(), dataform)
    session.commit()

# if __name__ == '__main__':

#     test = {
#         "phoneUDID": '1576457605007R5',
#         "spin": "533, 2067",
#         "spin_weights": 0.6200406327843666,
#         "addition": "770, 1903",
#         "addition_weights": 0.8958635032176971,
#         "subtraction": "300, 1904",
#         "subtraction_weights": 0.7953580021858215,
#         "lighting": "917, 2038",
#         "lighting_weights": 0.809893786907196,
#         "loop": "177, 2022",
#         "loop_weights": 0.8668246269226074,
#         "autoloop": "541, 1117",
#         "autoloop_weights": 0.8128960430622101,
#         "autostart": "541, 1806",
#         "autostart_weights": 0.8496356308460236,
#         "contents": "996, 1879",
#         "contents_weights": 0.8210124671459198,
#         "lobby": "111, 1946",
#         "lobby_weights": 0.809076339006424,
#         "record": "322, 1950",
#         "record_weights": 0.7789213359355927,
#         "recordcancel": "1003, 147",
#         "recordcancel_weights": None,
#         "rule": "539, 1942",
#         "rule_weights": 0.6771748960018158,
#         "ruleswitch": "1032, 1176",
#         "ruleswitch_weights": None,
#         "rulecancel": "1002, 287",
#         "rulecancel_weights": 0.7833113372325897,
#         "musicsetting": "757, 1945",
#         "musicsetting_weights": 0.7535094618797302,
#         "settingcancel": "953, 912",
#         "settingcancel_weights": 0.7906185686588287,
#         "cancel": "965, 1903",
#         "cancel_weights": 0.5678999200463295,
#         "popout": "540, 1121",
#         "popout_weights": 0.8191843926906586,
#         "confirm": "534, 1278",
#         "confirm_weights": 0.731523796916008
#     }


#     table_name = "deepseaposition"
#     engine, session, metadata = connect_DB()
#     ex_table = use_table(table_name, metadata, engine)
#     insert_value(session, ex_table, test)