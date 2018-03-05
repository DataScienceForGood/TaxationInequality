# Taxation Inequality
This project is designed to visualise and explore correlations between taxation income arising from lower and upper income brackets.

#### DSG Basel
This is an open data project managed by [Data Science for Good, Basel](http://bit.ly/DSGBasel). Please join us if you would like to participate!

## Repository structure
Data sources go in `/data`

Analysis code, etc goes in `/code`, should be placed under subdirectories when possible

Planning documents go in `/planning`

Analysis results, visualisations go in `/results`

## Getting going with Python
In `/code/python_gis_environment.yml` is a `YAML` file, for use in configuring a `conda` environment. I strongly recommend you install `conda` and use this environment file to configure an environment. We can all maintain a consistent configuration in this way.

### Configuring conda
Use the command `conda env create -f code/python_gis_environment.yml` to create an environment that includes Python 3.6, as well as all required libraries for analysing GIS data.

If you require extra libraries, install them using `conda install` and then export a new environment file with the command `conda env export > python_gis_environment.yml`. Then commit the new environment, and let everyone in the Slack channel know.
