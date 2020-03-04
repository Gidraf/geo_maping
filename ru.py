from flask import Flask, jsonify
import csv
import requests

counties_csv = open('counties.csv')
sub_counties_csv = open('sub_counties.csv')
csv_counties = csv.reader(counties_csv)
csv_sub_counties = csv.reader(sub_counties_csv)
COUNTIES = []
SUB_COUNTIES = []
iso = 0;
# app = Flask(__name__)


for row in csv_counties:
    resp = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={row[1]}&key=AIzaSyBLALBYBwVAJrFshQ6dWKiNaCqySBQskSI")
    location = resp.json().get("results")[0].get("geometry").get("location")
    county = {
        "name":row[1],
        "location": location,
        "iso":f"0{iso}"
    }
    iso = iso + 1
    COUNTIES.append(county)
    print (iso)
for row in csv_sub_counties:                                    
    resp = requests.get(f"""https://maps.googleapis.com/maps/api/geocode/json?address={row[2]}&key=AIzaSyBLALBYBwVAJrFshQ6dWKiNaCqySBQskSI""")
    if len(resp.json().get("results"))==0:
        location = resp.json().get("results")[0].get("geometry").get("""location""")
        sub_county = {
            "name":row[2],
             "location": location,
             "county_index":f""
        }
        SUB_COUNTIES.append(sub_county)
    print("No location found")
    
    print (f"No location found on {row[2]}")
    print ("------------------------------")
    print (resp.text)


