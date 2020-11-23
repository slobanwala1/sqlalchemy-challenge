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
from flask import Flask, jsonify
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
station = database.classes.station

session_link = Session(engine)

app = Flask(__name__)

# Routes:
@app.route("/")
def main():
    """List all routes that are available."""
    return (
        f"Hawaii Temperature Analysis by Shanil Lobanwala<br/>"
        f"Available Routes:<br/><br/>"
        f"dictionary with date(key), prcp(value), and returns JSON of dict:<br/>"
        f"/api/v1.0/precipitation<br/><br/>"
        f"JSON list of stations:<br/>"
        f"/api/v1.0/stations<br/><br/>"
        f"JSON list of temperature observations for prev. year of most active station:<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"JSON list of min temp, avg temp and max temp for given start date:<br/>"
        f"/api/v1.0/<start><br/><br/>"
        f"JSON list of min temp, avg temp and max temp for given start date or end date:<br/>"
        f"/api/v1.0/<start>/<end>"
    )

if __name__ == "__main__":
    app.run(debug = True)
