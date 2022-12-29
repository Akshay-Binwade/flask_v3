import pymysql.cursors
import json
from models.datamodels.vehicles import Vehicles_from_db
from models.datamodels.starships import Starships_from_db

connection = pymysql.connect(
    user='****',
    password='****',
    database='starwarsDB',
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = connection.cursor()



def get_infos(table:str, validator):
    'Takes table name as argument and returns data from table in json format'

    mycursor.execute(f"select * from {table};")
    datas = mycursor.fetchall()
    # breakpoint()
    from pydantic import parse_obj_as
    # v_datas = parse_obj_as(list[Films_from_db], datas)
    v_datas = parse_obj_as(list[validator], datas)
    # breakpoint()
    resp = json.dumps([i.dict() for i in v_datas])

    return resp



def get_info(table:[str], primary_key:[str], validator, index:[int]):
    ''' Takes tables name, primary key and index number as argument and returns
    either result in json form or gives the error message and suggestion to
    chose from available data '''

    mycursor.execute(f"select * from {table} where {primary_key} = {index};")
    data = mycursor.fetchall()
    if data:
        v_data = validator(**data[0])
        resp = json.dumps(dict(v_data))
        return resp
    else:
        mycursor.execute(f"select {primary_key} from {table};")
        data = mycursor.fetchall()
        resp = {"ERROR": f"Data not found for {index}",
                "Chose from available": f"{data}"}
        resp = json.dumps(resp)
        return resp


# TestCases
# get_infos("films", Films_from_db)
# get_infos("vehicles", Vehicles_from_db)
# get_infos("starships", Starships_from_db)

# get_info("vehicles", "vehicle_id", Vehicles_from_db, 4)