# Transfermarkt Player Statistics Scraper

This Python script allows users to extract and analyze player statistics (appearances, goals, assists) from the Transfermarkt website for a specific football club. The script fetches data from a club's record players page, processes it, and provides insights on player statistics. Additionally, the data can be saved to an Excel spreadsheet, and the script offers the option to display a graph of the players' statistics.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `matplotlib` library

To install the required libraries, you can use pip:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

## How to Use

1. **Input Club Name and ID:**
   When prompted, enter the club name (e.g., "manchester-united") and the club's unique Transfermarkt ID (e.g., 985 for Manchester United). These inputs will be used to construct the URL for the club's record players page.

2. **Data Extraction:**
   The script will scrape data for the following statistics:
   - Player Name
   - Nationality
   - Appearances
   - Goals
   - Assists

3. **Save Data (Optional):**
   After the data is scraped, you will be asked if you'd like to save the data to an Excel file. If you choose "y," the data will be saved in a file named `<club_name>_records.xlsx`.

4. **Analysis:**
   The script will provide the following insights:
   - The most frequently listed nationality.
   - The average number of appearances for the top 25 players.
   - The player with the most appearances.
   - The top scorer in the list.
   - The player with the most assists.

5. **Graph Plot (Optional):**
   After the analysis, you will be prompted if you want to display a graph comparing players' appearances, goals, and assists. If you choose "y," a line plot will be shown.

## Example Output

```
Enter the club name: manchester-united
Enter the club's unique Transfermarkt ID (e.g., 985 for Manchester United): 985
Do you want to save the data to an excel spreadsheet? (y/n) : y
Data saved to 'manchester-united_records.xlsx' successfully.
The most frequently listed nation is England
The average number of appearances in the top 25 for Manchester United is: 218
The player with most appearances is: Ryan Giggs with 802
The top scorer of the 25 is: Wayne Rooney with 253
The top assister of the 25 is: Ryan Giggs with 162
Do you want to display a graph? y/n y
```

## Notes

- The script is designed to scrape the "Record Players" page for a given club, which includes a list of players and their statistics.
- Data can be saved to an Excel file for further analysis.
- The graph displays the players' statistics (Appearances, Goals, and Assists) on the same plot for comparison.

## Limitations

- The script only supports clubs listed on Transfermarkt.
- It assumes the data structure on the Transfermarkt page remains the same. If the website's layout changes, the script may need to be updated.
