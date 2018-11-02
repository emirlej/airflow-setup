# Name: Emir Lejlic
# Date: 02.11.2018
#
# Setting up Apache Airflow using Linux WSL on Windows :)

# airflow needs a home, ~/airflow is the default,
# but you can lay foundation somewhere else if you prefer
# (optional)
export AIRFLOW_HOME="<insert>/<path>/<to_airflow_home>" # This is added to my .bashrc file

# TODO: Should maybe setup an own airflow conda environment
# TODO: Need to have a en
ENVIRONMENT_FILE=""

# FIXME: Pseudo code
conda create environment
conda choose environment
export AIRFLOW_HOME
init db 

# Install airflow: https://anaconda.org/conda-forge/airflow
conda install -c conda-forge airflow 

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler

# visit localhost:8080 in the browser and enable the example dag in the home page

# More info may be found here: https://airflow.readthedocs.io/en/stable/installation.html
