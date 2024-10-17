# Transfermarkt_record_holders_data
Script to extract data on the record holders for a club. Creates a table and graph for top appearances, goals and assists and provides additional stats

This Python script scrapes data from the Transfermarkt website for the top 25 record-holding players of Manchester United. The data collected includes player names, nationalities, appearances, goals, and assists. The script saves this data to an Excel file and provides statistical insights, such as the most frequent nationality and the average number of appearances. Additionally, it offers the option to visualise the data in a graph.

UPDATE-User_Input_Scraper.py This allows the user to input a club of their choice to get the stats. They need to enter the club name(with hyphens in place of spaces) and the club's Transfermarkt ID number. I added a list of IDs for testing. 

## Requirements:

Python 3.x

Required Python libraries:
requests
beautifulsoup4
pandas
matplotlib
statistics

## Results:
Table showing scraped data: Man_Utd_records.xlsx

Optional Graph produced:
![Screenshot 2024-09-17 125406](https://github.com/user-attachments/assets/28610dc9-1758-4639-8e7d-8530dc62a397)


