from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///coordinate.db"

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

def value_transfer(udid, result):
    """
    match_result need transfer sqlite column same
    """
    dataform = {
        "phoneUDID": udid,
        "spin": result["spin"]["result"],
        "spin_weights": result["spin"]["confidence"],
        "addition": result["addition"]["result"],
        "addition_weights": result["addition"]["confidence"],
        "subtraction": result["subtraction"]["result"],
        "subtraction_weights": result["subtraction"]["confidence"],
        "lighting": result["lighting"]["result"],
        "lighting_weights": result["lighting"]["confidence"],
        "loop": result["loop"]["result"],
        "loop_weights": result["loop"]["confidence"],
        "autoloop": result["autoloop"]["result"],
        "autoloop_weights": result["autoloop"]["confidence"],
        "autostart": result["autostart"]["result"],
        "autostart_weights": result["autostart"]["confidence"],
        "contents": result["contents"]["result"],
        "contents_weights": result["contents"]["confidence"],
        "lobby": result["lobby"]["result"],
        "lobby_weights": result["lobby"]["confidence"],
        "record": result["record"]["result"],
        "record_weights": result["record"]["confidence"],
        "recordcancel": result["recordcancel"]["result"],
        "recordcancel_weights": result["recordcancel"]["confidence"],
        "rule": result["rule"]["result"],
        "rule_weights": result["rule"]["confidence"],
        "ruleswitch": result["ruleswitch"]["result"],
        "ruleswitch_weights": result["ruleswitch"]["confidence"],
        "rulecancel": result["rulecancel"]["result"],
        "rulecancel_weights": result["rulecancel"]["confidence"],
        "musicsetting": result["musicsetting"]["result"],
        "musicsetting_weights": result["musicsetting"]["confidence"],
        "settingcancel": result["settingcancel"]["result"],
        "settingcancel_weights": result["settingcancel"]["confidence"],
        "cancel": result["cancel"]["result"],
        "cancel_weights": result["cancel"]["confidence"],
        "popout": result["popout"]["result"],
        "popout_weights": result["popout"]["confidence"],
        "confirm": result["confirm"]["result"],
        "confirm_weights": result["confirm"]["confidence"],
        }

    return dataform

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