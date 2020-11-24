# sqlalchemy-challenge


**Data Analysis For SQLAlchemy Homework - Surfs Up! by Shanil Lobanwala**

## Links to files

For this homework The first portion is *Step 1 - Climate Analysis and Exploration*. The link to that directory is: [Step 1 - Climate Analysis and Exploration](https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/climate_starter.ipynb). The second portion is *Step 2 - Climate App* and is located at: [Step 2 - Climate App](https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/app.py). Finally the fun portion to see the data in a visual form was in the *Bonus* portion. That is located in the first Jupyter Notebook file. The *graphs* are located in [Images](https://github.com/slobanwala1/sqlalchemy-challenge/tree/main/Images). Here's the link to the [Instructor prompt](https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Instructor_README.md). Heres my analysis after working on the whole project:


### SQLAlchemy Analysis:

Hawaii does indeed have a very mild temperature throughout the whole year and seems like a very nice place to vacation. If we look at the graphs:

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/precipitation_last_12_months.png" width="681">

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Temperature_observation_histogram.png" width="681">

Clearly the frequency of temperatures is mostly in the 70s, however yes there is a decent amount of rain/precipitation each year. Just have to make sure to dodge the months that have a lot of rain each year when planning your trip.

### Climate App:

It was really interesting to create an sort of api for my analysis because watching how the app generated and displayed all the data was really awesome. The api had multiple routes, heres a list of them:

**< host >/** - Lists all the paths

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/List_of_paths.PNG" width="500">

**< host >/api/v1.0/precipitation** -  dict with date(key), prcp(value), and returns JSON of dict

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/List_of_precipitation.PNG" width="500">

**< host >/api/v1.0/stations** - JSON list of stations

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/List_of_stations.PNG" width="500">

**< host >/api/v1.0/tobs** - JSON list of temperature observations for prev. year of most active station

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/List_of_tobs.PNG" width="500">

**< host >/api/v1.0/< start_date >** - JSON list of min temp, avg temp and max temp for given start date:

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Start_date_temp_obs.PNG" width="500">

**< host >/api/v1.0/< start_date >/< end_date >** - JSON list of min temp, avg temp and max temp for given start date or end date

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Start_End_date_temp_obs.PNG" width="500">

**ERROR HANDLING** - Handle errors for both start date and end date validation, one by one

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Date_Error_Handling.PNG" width="500">


### Bonus:

plt.savefig() loves to hide the axis indicators lots of times however, these plots show us the average, min, as well as the max temperatures of the days we want to go on vacation. 
From what is shown it is around the 70 degrees F or more each day, confirming the analysis that Hawaii has very mild and warm/hot temperature year round, with precipitation 
but even during that its warm/humid. For speciifics the Trip Avg Temp plot shows us the average temperature for the vacation is high 70s almost 80 degrees F. The Daily Normals for 
trip dates shows us that the even the min temp is high 60 degrees F.

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Temperature_observation_bar.png" height="500">

<br>
<br>
<img src="https://github.com/slobanwala1/sqlalchemy-challenge/blob/main/Images/Daily_normals_graph.png" width="500">


All in all it was an interesting analysis, I knew Hawaii was hot but all year long is kind of wild and really interesting. The homework really got me excited to go to Hawaii for vacation
because of the good weather, just to make sure to avoid precipitation/rainy days. Thanks again for the chance to work on such an interesting homework!