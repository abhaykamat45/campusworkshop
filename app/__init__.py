"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7m65269vf5qb90a80-a.oregon-postgres.render.com",
        database="todo_x05f",
        user="root",
        password="AhKvIjCxdcvNi4a7DXAy251NOEvvSdOB")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
