import json
from models.dal.methods import get_info, get_infos, post_info, put_info
from flask import Flask, Blueprint, Response, request

from models.datamodels.films import Films_from_db, F_PostOrPut
from models.datamodels.characters import Char_from_db, C_PostOrPut
from models.datamodels.planets import Plan_from_db, P_PostOrPut
from models.datamodels.species import Species_from_db, Sp_PostOrPut
from models.datamodels.starships import Starships_from_db, St_PutOrPost
from models.datamodels.vehicles import Vehicles_from_db, V_PostOrPut


crud_app = Blueprint("crud_ops", __name__)


@crud_app.route("/")
def home():
    return "Welcome to the crud_ops home page..."


@crud_app.route("/films")
def get_films_():
    resp = get_infos("films", Films_from_db)
    return Response(resp, status=200, mimetype="application/json")

# Previous method which were updated as above.
# @crud_app.route("/films")
# def get_films_():
#     mycursor.execute(f"select * from films;")
#     datas = mycursor.fetchall()
#
#     from pydantic import parse_obj_as
#     v_datas = parse_obj_as(list[Film_from_db], datas)
#     # resp = json.dumps(dict(v_datas[0]))
#     resp = json.dumps([i.dict() for i in v_datas])
#     return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/films/<int:index>")
def get_film(index):
    resp = get_info("films", "film_id", Films_from_db, index)
    return Response(resp, status=200, mimetype="application/json")

# @crud_app.route("/films/<int:index>")
# def get_film(index):
#     mycursor.execute(f"select * from films where film_id = {index};")
#     data = mycursor.fetchall()
#     if data:
#         v_data = Films_from_db(**data[0])
#         resp = json.dumps(dict(v_data))
#         return Response(resp, status=200, mimetype='application/json')
#     else:
#         mycursor.execute(f"select film_id from films;")
#         data = mycursor.fetchall()
#         resp = {"ERROR": f"Data not found for {index}",
#                 "Chose from available": f"{data}"}
#         resp = json.dumps(resp)
#         return Response(resp, status=200, mimetype="application/json")

@crud_app.route("/films/<int:id>", methods = ['POST'])
def post_film(id):
    req_data = request.json
    result = post_info(req_data, "films", "film_id",id, F_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# @crud_app.route("/films/<int:id>", methods = ['POST'])
# def post_film(id):
#     from pydantic.error_wrappers import ValidationError
#     req_data = request.json
#     try:
#         v_data = F_PostOrPut(**req_data)
#     except ValidationError:
#         err_msg = json.dumps({"message": "bad request"})
#         return Response(err_msg, status=400, mimetype="application/json")
#
#     result = post_info(dict(v_data), "films", "film_id",id)
#
#     resp_msg = json.dumps({"message": result})
#     return Response(resp_msg, status=200, mimetype="application/json")

@crud_app.route("/films/<int:id>", methods=['PUT'])
def put_film(id):
    req_data = request.json
    result = put_info(req_data, "films", "film_id",id, F_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# @crud_app.route("/films/<int:id>", methods=['PUT'])
# def put_film(id):
#     from pydantic.error_wrappers import ValidationError
#     req_data = request.json
#     try:
#         v_data = F_PostOrPut(**req_data)
#     except ValidationError:
#         err_msg = json.dumps({"message": "bad request"})
#         return Response(err_msg, status=400, mimetype="application/json")
#
#     result = put_info(dict(v_data), "films", "film_id", id)
#     return Response(json.dumps(result), status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------

@crud_app.route("/planets", methods=["GET"])
def get_planets():
    resp = get_infos("planets",Plan_from_db)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/planets/<int:index>", methods=["GET"])
def get_planet(index):
    resp = get_info("planets", "planet_id",Plan_from_db, index)
    return Response(resp, status=200, mimetype="application/json")

@crud_app.route("/planets/<int:id_>", methods=['POST'])
def post_planet(id_):
    req_data = request.json
    result = post_info(req_data, "planets", "planet_id", id_, P_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

@crud_app.route("/planets/<int:id>", methods=['PUT'])
def put_planet(id):
    req_data = request.json
    result = put_info(req_data, "planets", "planet_id", id, P_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------

@crud_app.route("/species", methods=["GET"])
def get_species():
    resp = get_infos("species", Species_from_db)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/species/<int:index>", methods=["GET"])
def get_specie(index):
    resp = get_info("species","species_id", Species_from_db, index)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/species/<int:id_>", methods=['POST'])
def post_species(id_):
    req_data = request.json
    result = post_info(req_data, "species", "species_id", id_, Sp_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")


@crud_app.route("/species/<int:id>", methods=['PUT'])
def put_species(id):
    req_data = request.json
    result = put_info(req_data, "species", "species_id", id, Sp_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------

@crud_app.route("/starships", methods=["GET"])
def get_starships():
    resp = get_infos("starships", Starships_from_db)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/starships/<int:index>", methods=["GET"])
def get_starship(index):
    resp = get_info("starships", "starship_id", Starships_from_db, index)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/starships/<int:id_>", methods=['POST'])
def post_starship(id_):
    req_data = request.json
    result = post_info(req_data, "starships", "starship_id", id_, St_PutOrPost)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")


@crud_app.route("/starships/<int:id>", methods=['PUT'])
def put_starship(id):
    req_data = request.json
    result = put_info(req_data, "starships", "starship_id", id, St_PutOrPost)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------


@crud_app.route("/vehicles", methods=["GET"])
def get_vehicles():
    resp = get_infos("vehicles", Vehicles_from_db)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/vehicles/<int:index>", methods=["GET"])
def get_vehicle(index):
    resp = get_info("vehicles", "vehicle_id", Vehicles_from_db, index)
    return Response(resp, status=200, mimetype="application/json")

@crud_app.route("/vehicles/<int:id_>", methods=['POST'])
def post_vehicle(id_):
    req_data = request.json
    result = post_info(req_data, "vehicles", "vehicle_id", id_, V_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")


@crud_app.route("/vehicles/<int:id>", methods=['PUT'])
def put_vehicle(id):
    req_data = request.json
    result = put_info(req_data, "vehicles", "vehicle_id", id, V_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------


@crud_app.route("/characters", methods=["GET"])
def get_characters():
    resp = get_infos("characters", Char_from_db)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/characters/<int:index>", methods=["GET"])
def get_character(index):
    resp = get_info("characters", "char_id", Char_from_db, index)
    return Response(resp, status=200, mimetype="application/json")


@crud_app.route("/characters/<int:id_>", methods=['POST'])
def post_character(id_):
    req_data = request.json
    result = post_info(req_data, "characters", "char_id", id_, C_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")


@crud_app.route("/characters/<int:id>", methods=['PUT'])
def put_character(id):
    req_data = request.json
    result = put_info(req_data, "characters", "char_id", id, C_PostOrPut)
    resp_msg = json.dumps({"message": result})
    return Response(resp_msg, status=200, mimetype="application/json")

# ---------------------------------------------------------------------------------------------


# mycursor.execute(f"select * from planets")
# data = mycursor.fetchall()
# # print(data)
# # print(type(data))
# v_data = json.dumps(data)
# print(v_data)
# print(type(v_data))


# mycursor.execute(f"select * from films")
# data = mycursor.fetchall()
# print((data))
# v_data = Film_from_db(**data[0])
# print(v_data)
# v_data = json.dumps(v_data.dict())
# print(v_data)
# print(f"select * from planets where primary key 1")


# mycursor.execute(f"select * from films")
# data = mycursor.fetchall()
# from pydantic import parse_obj_as
# v_data = parse_obj_as(list[Film_from_db], data)
# print(type(v_data))
# print([i.dict() for i in v_data])
# # v_data = json.dumps([i.dict() for i in v_data])
# v_data = json.dumps(dict(v_data[0]))
# print(v_data)