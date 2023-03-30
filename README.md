Coolest Cities Finder

This script finds the coolest cities (based on the lowest average temperature) in a specified US state for a given month. The list of cities can be filtered by a minimum population, and the number of cities returned can be controlled.

Prerequisites

- Python 3.6 or higher
- requests library installed (install using pip install requests)
- World Weather Online API key (get one from https://www.worldweatheronline.com/developer/)
- uscities.csv file in the same directory as the script (download from https://simplemaps.com/data/us-cities)

Usage

To run the script, use the following command:

python3 ./weather.py -k API_KEY -s STATE_CODE -m MONTH -p MIN_POPULATION -n NUM_CITIES

Replace the following placeholders with appropriate values:

API_KEY: Your World Weather Online API key
STATE_CODE: Two-letter state code (e.g., 'CA', 'NY')
MONTH: Month as an integer (1-12)
MIN_POPULATION: Minimum population of the cities
NUM_CITIES: Number of cities to return

Example
To find the top 10 coolest cities in Oklahoma with a population of at least 5,000 people for the month of August, use the following command:

python3 ./weather.py -k <key> -s OK -m 8 -p 5000 -n 10

Output
The script will print the list of cities with their average temperature for the specified month, sorted in ascending order of temperature. For example:

Grove, OK - 70ºF
Miami, OK - 70ºF
Guymon, OK - 70ºF
Tahlequah, OK - 71ºF
Bartlesville, OK - 71ºF
Vinita, OK - 71ºF
Poteau, OK - 71ºF
Pryor Creek, OK - 71ºF
Ponca City, OK - 72ºF
Sallisaw, OK - 72ºF
License

This project is licensed under the MIT License.
