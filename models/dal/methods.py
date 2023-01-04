import pymysql.cursors
import json
from models.datamodels.vehicles import Vehicles_from_db
from models.datamodels.starships import Starships_from_db

connection = pymysql.connect(
    user='root',
    password='root',
    database='practice',
    cursorclass=pymysql.cursors.DictCursor
)
mycursor = connection.cursor()


def get_infos(table:str, validator):
    ''' Takes table name as argument and returns data from table in json format '''

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


def post_info(req_data, table, primary_key, primary_val, validator):

    from pydantic.error_wrappers import ValidationError
    try:
        v_data = validator(**req_data)
        data = dict(v_data)
    except ValidationError:
        return f"bad request...!!!"

    columns_ = ", ".join(data.keys())
    values_1 = list(data.values())
    values_1.append(primary_val)

    try:
        mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}")
        connection.commit()
        return f"Successs, data is Posted in table {table}...!!!"
    except:
        return f"[ERROR] Could not POST data in {table} for id {primary_val}"


def put_info(req_data, table, primary_key, primary_val, validator):

    from pydantic.error_wrappers import ValidationError
    try:
        v_data = validator(**req_data)
        data = dict(v_data)
    except ValidationError:
        return f"bad request...!!!"

    columns_ = ", ".join(data.keys())
    # print(columns_.split(', '))
    values_1 = list(data.values())
    values_1.append(primary_val)

    col_val_pair = []
    for k,v in zip(columns_.split(','), list(data.values())):
        col_val_pair.append(f'''{k}="{(v)}"''')

    # Uncomment below statement to print the query.
    # print(f"update {table} set {', '.join(col_val_pair)} where {primary_key}={primary_val}")

    try:
        mycursor.execute(f"update {table} set {', '.join(col_val_pair)} where {primary_key}={primary_val}")
        connection.commit()
        return f"Success, {primary_key}: {primary_val} is updated...!!!"

    except:
        return f"[ERROR] Could not update data in {table} for id {primary_val}"



        # if data.get("url") is not "Null":
        #     columns_ = ", ".join(data.keys())
        #     primary_value = data.get("url").split("/")[-2]
        #     print(primary_value)
        #     # print()
        #     values_1 = list(data.values())
        #     values_1.append(primary_value)
        #     # print("values_2:", values_1)
        #
        #     # query = f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}"
        #     # query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}"
        #     query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)} ON DUPLICATE KEY UPDATE {primary_key}= {primary_value};"
        #     print(query)
        #     print()
        #     print()
        #
        #     try:
        #         # mycursor.execute(f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}")
        #         # mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}")
        #         mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)} ON DUPLICATE KEY UPDATE {primary_key}= {primary_value};")
        #         connection.commit()
        #         print(f"{table} is updated with id {primary_value}...!!!")
        #
        #     except:
        #         print(f"Could not add data in {table} for id {primary_value}")
        #     print("*" * 30)
        #
        #
        # else:
        #     columns_ = ", ".join(data.keys())
        #     # print()
        #     values_1 = list(data.values())
        #     values_1.append(primary_val)
        #     # print("values_2:", values_1)
        #
        #     # query = f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}"
        #     # query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}"
        #     query = f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)} ON DUPLICATE KEY UPDATE {primary_key}= {primary_val};"
        #     print(query)
        #     print()
        #     print()
        #
        #     try:
        #         # mycursor.execute(f"insert into {table} ({', '.join(data.keys())}) values {tuple(data.values())}")
        #         # mycursor.execute(f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)}")
        #         mycursor.execute(
        #             f"insert into {table} ({columns_},{primary_key}) values {tuple(values_1)} ON DUPLICATE KEY UPDATE {primary_key}= {primary_val};")
        #         connection.commit()
        #         print(f"{table} is updated with id {primary_val}...!!!")
        #
        #     except:
        #         print(f"Could not add data in {table} for id {primary_val}")
        #     print("*" * 30)



# TestCases
# get_infos("films", Films_from_db)
# get_infos("vehicles", Vehicles_from_db)
# get_infos("starships", Starships_from_db)

# get_info("vehicles", "vehicle_id", Vehicles_from_db, 4)