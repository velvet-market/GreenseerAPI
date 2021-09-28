from flask import Flask, jsonify, request
from db import *

# def get_bin_info():
#     conn = open_connection()
#     with conn.cursor() as cursor:
#         result = cursor.execute('SELECT * FROM bins;')
#         bin_items = cursor.fetchall()
#         bin_json = jsonify(bin_items)

#     conn.close()
#     return bin_json

# def add_item(item_dict):
#     conn = open_connection()
#     with conn.cursor() as cursor:
#         cursor.execute('INSERT INTO items (timestamp, prediction, binID) VALUES(%s, %s, %s)', (item_dict["timestamp"], item_dict["prediction"], item_dict["binID"]))
#     conn.commit()
#     conn.close()

app = Flask(__name__)
@app.route('/bin', methods=["POST"])
def put_bin():
    bdata = request.data
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO bin (binID, type, count, capacity, incorrect) VALUES (%s, %s, %s, %s, %s)", (bdata["id"], bdata["type"], bdata["count"], bdata["capacity"], bdata["incorrect"]))

@app.route('/item', methods=["POST"])
def put_item():
    idata = request.data
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO items (binID, prediction, timestamp) VALUES (%s, %s, %s)", (idata["id"], bdata["prediction"], bdata["timestamp"]))      
        cursor.execute("UPDATE bin SET count = count + 1 WHERE binID = (%s)", (idata["id"]))
        cursor.execute("UPDATE bin SET incorrect = incorrect + 1 WHERE type != (%s)", (idata["prediction"]))

# @app.route('/pizza', methods=["GET"])
# def get_data():
#     conn = open_connection()
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM items")
#         items_data = cursor.fetchall()

#         cursor.execute("SELECT * FROM bins")
#         bins_data = cursor.fetchall()

#         print(items_data)
#         print(bins_data)

#         items_json = jsonify(items_data)
#         bins_json = jsonify(bins_data)

#         bins_json["items"] = {}
#         for items in items_json:
#             if items["prediction"] not in bins_json["items"]:
#                 bins_json["items"][items["prediction"]] = 0
#             else 
#                 bins_json["items"][items["prediction"]] += 1

#         bins_json["timeline"] = [(x["timestamp"], x[""])]

if __name__ == '__main__':
  app.run(debug=True)