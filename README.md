# SteamCharts Web Scraper

## Description
This app written in python navigates to Steamcharts.com and pulls data from the top 25 games on Steam (ranked by most current players) and returns a csv file.
I am collecting this data for another project I am working on and thought I would share this for anyone else that may want to begin pulling from this site. 

## Installation and Usage

This python script requires you to have Google Chrome downloaded.

Required packages:
- selenium
- pandas
- webriver-manager

You may have to update the save path on line 58 within scrape.py to provide your system with a valid path to save the file. 