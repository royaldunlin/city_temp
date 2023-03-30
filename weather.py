#!/usr/bin/python

import argparse
import csv
import requests

API_URL = "https://api.worldweatheronline.com/premium/v1/weather.ashx"

def get_cities(state_code, min_population):
    cities = []
    with open('uscities.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['state_id'] == state_code and int(row['population']) >= min_population:
                first_zip = row['zips'].split(" ")[0]
                cities.append((row['city'], int(row['population']), first_zip))
    return cities

def get_average_temperature(zip_code, month, api_key):
    params = {
        'key': api_key,
        'q': zip_code,
        'format': 'json',
        'cc': 'no',
        'fx': 'no',
        'mca': 'yes'
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Unable to fetch data from the API (status code: {response.status_code})")

    data = response.json()
    avg_temp = float(data['data']['ClimateAverages'][0]['month'][month - 1]['avgMinTemp_F'])

    return avg_temp

def print_results(results, state_code):
    for city in results:
        print(f"{city[0]}, {state_code} - {city[1]:.0f}ºF")

def main(api_key, state_code, month, min_population, num_cities):
    cities = get_cities(state_code, min_population)
    cities_with_temps = []

    for city in cities:
        zip_code = city[2]
        avg_temp = get_average_temperature(zip_code, month, api_key)
        cities_with_temps.append((city[0], avg_temp))

    cities_with_temps.sort(key=lambda x: x[1])
    print_results(cities_with_temps[:num_cities], state_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the coolest cities in a given state.")
    parser.add_argument('-k', '--api_key', required=True, help="World Weather Online API key.")
    parser.add_argument('-s', '--state', required=True, help="Two-letter state code (e.g., 'CA', 'NY').")
    parser.add_argument('-m', '--month', type=int, required=True, help="Month as an integer (1-12).")
    parser.add_argument('-p', '--population', type=int, required=True, help="Minimum population of the cities.")
    parser.add_argument('-n', '--num_cities', type=int, required=True, help="Number of cities to return.")

    args = parser.parse_args()

    main(args.api_key, args.state.upper(), args.month, args.population, args.num_cities)
