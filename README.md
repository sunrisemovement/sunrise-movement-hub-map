# sunrise-movement-hub-map
Code for the map on this page: https://www.sunrisemovement.org/hubs/

## Spreadsheet powering the map:
https://docs.google.com/spreadsheets/d/1ZX3bzLhbnq1MICD_siWDw2hxeP0SGXGoHyuXpzp-rzA/edit#gid=0

## How to install into Squarespace:
Copy the entire contents of the `hub_map.html` page and paste it into a new [Code block component](https://support.squarespace.com/hc/en-us/articles/206543167-Using-the-Code-Block) in Squarespace (ensure that HTML is selected in the dropdown menu).

## How to develop locally:

1. Download [flask](http://flask.pocoo.org/)
2. Run `FLASK_APP=app.py flask run` in the project directory
3. Visit `localhost:5000`

This will load a mocked-up version of the sunrisemovement.org homepage which embeds the map.
