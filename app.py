# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 05:48:44 2020

@author: slobanwala
"""
# Imports necessary
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, request, jsonify
import datetime as dt

# Routes:
# / - Home page, List all routes that are available.
# /api/v1.0/precipitation - dictionary with date(key), prcp(value), and returns JSON of dict
# /api/v1.0/stations - JSON list of stations
# /api/v1.0/tobs - JSON list of temperature observations for prev. year of most active station.
# /api/v1.0/<start> - JSON list of min temp, avg temp and max temp for given start date
# /api/v1.0/<start>/<end> - JSON list of min temp, avg temp and max temp for given start date or end date

# Do the same process as we did in the analysis to create engine and grab the tables
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

database = automap_base()
database.prepare(engine, reflect = True)

measurement = database.classes.measurement
# station was giving error so had to capitalize it
Station = database.classes.station

session_link = Session(engine)

app = Flask(__name__)


# Routes:
@app.route("/")
def main():
    print("List all routes that are available.")
    return (
        f"Hawaii Temperature Analysis by Shanil Lobanwala<br/>"
        f"Available Routes:<br/><br/>"
        f"dict with date(key), prcp(value), and returns JSON of dict:<br/>"
        f"< host >/api/v1.0/precipitation<br/><br/>"
        f"JSON list of stations:<br/>"
        f"< host >/api/v1.0/stations<br/><br/>"
        f"JSON list of temperature observations for prev. year of most active station:<br/>"
        f"< host >/api/v1.0/tobs<br/><br/>"
        f"JSON list of min temp, avg temp and max temp for given start date:<br/>"
        f"< host >/api/v1.0/<start><br/><br/>"
        f"JSON list of min temp, avg temp and max temp for given start date or end date:<br/>"
        f"< host >/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    print("dict with date(key), prcp(value), and returns JSON of dict")

    print("Returning precipitation api request...")
    # Query the dates and grab the first date and convert it to date time.
    dates_query = session_link.query(func.max(func.strftime("%Y-%m-%d", measurement.date))).all()
    date_only = dates_query[0][0]
    date_convert = dt.datetime.strptime(date_only, "%Y-%m-%d")
    first_date = date_convert - dt.timedelta(365)
    
    # Filter the precipitation data with date we grabbed and grab everything that is greater and equal
    # to the filter date
    precipitation_date_value_data = session_link.query(func.strftime("%Y-%m-%d", measurement.date), measurement.prcp).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= first_date).all()
    
    # Store in dict and return the dict after parsing through all values
    precipitation_date_value_arr = {}
    for data in precipitation_date_value_data:
        precipitation_date_value_arr[data[0]] = data[1]

    return jsonify("Returning precipitation api request...", precipitation_date_value_arr)

@app.route("/api/v1.0/stations")
def stations():
    print("JSON list of stations:")

    print("Returning station api request...")
    # query stations list, each station has an index, station id, name, latitude, longitude
    # and elevation
    stations = session_link.query(Station).all()

    # Store dict values into a list for easier Json printing
    stations_list = []
    
    for station in stations:
        station_dict = {}
        station_dict["id"] = station.id
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        station_dict["latitude"] = station.latitude
        station_dict["longitude"] = station.longitude
        station_dict["elevation"] = station.elevation
        stations_list.append(station_dict)

    return jsonify("Returning stations api request...", stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    print("JSON list of temperature observations for prev. year of most active station:")
    
    print("Returning tobs api request...")
    
    # temp data for last year, grab last date again.
    dates_query = session_link.query(func.max(func.strftime("%Y-%m-%d", measurement.date))).all()
    date_only = dates_query[0][0]
    date_convert = dt.datetime.strptime(date_only, "%Y-%m-%d")
    first_date = date_convert - dt.timedelta(365)
    
    # Query session for temp measurements from last year, has date, station and temp
    temps_obs_query = session_link.query(measurement).\
        filter(func.strftime("%Y-%m-%d", measurement.date) >= first_date).all()
    
    # Store dict values into a list for easier Json printing
    tobs_json_list = []
    for t in temps_obs_query:
        temp_obs_dict = {}
        temp_obs_dict["date"] = t.date
        temp_obs_dict["station"] = t.station
        temp_obs_dict["tobs"] = t.tobs
        tobs_json_list.append(temp_obs_dict)
    
    return jsonify("Returning tobs api request...", tobs_json_list)

@app.route("/api/v1.0/<start>")
def start_date_only(start):
    print("JSON list of min temp, avg temp and max temp for given start date:")
    
    print("Returning start_date api request...")
    return jsonify("Returning start_date api request...")


# if statement to handle debug and running the application
if __name__ == "__main__":
    app.run(debug = True)
