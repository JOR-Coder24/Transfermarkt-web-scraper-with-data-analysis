import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Define headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.8.2526.186 Safari/537.36"
}

# Define URL
club_name = input("Enter the club name (use '-' for spaces, e.g., manchester-united): ").strip()
club_id = input("Enter the club's unique Transfermarkt ID (e.g., 985 for Manchester United): ").strip()

# Define URL using club_name and club_id
page = f"https://www.transfermarkt.co.uk/{club_name}/rekordspieler/verein/{club_id}"

# Get the page content
page_tree = requests.get(page, headers=headers)
page_soup = BeautifulSoup(page_tree.content, 'html.parser')

# Initialize lists for data
PlayerList = []
NationList = []
AppsList = []
GoalsList = []
AssistsList = []

# Extract player names and nationalities
player_rows = page_soup.select("table.items > tbody > tr")

for row in player_rows:
    # Extract player name
    name_element = row.select_one("td.hauptlink > a")
    if name_element:
        name = name_element.get('title', 'N/A').strip()
        PlayerList.append(name)
    else:
        PlayerList.append('N/A')

    # Extract nationality
    nationality_element = row.select_one("img.flaggenrahmen")
    if nationality_element:
        nationality = nationality_element.get('title', 'N/A').strip()
        NationList.append(nationality)
    else:
        NationList.append('N/A')

    # Extract apps, goals, and assists
    stats = row.select("td.zentriert")
    if len(stats) >= 3:
        AppsList.append(int(stats[3].text.strip().replace(',', '')))
        GoalsList.append(int(stats[4].text.strip().replace(',', '')))
        AssistsList.append(int(stats[5].text.strip().replace(',', '')))
    else:
        AppsList.append(0)
        GoalsList.append(0)
        AssistsList.append(0)

# Create DataFrame
final_df = pd.DataFrame({
    "Player": PlayerList,
    "Nation": NationList,
    "Apps": AppsList,
    "Goals": GoalsList,
    "Assists": AssistsList
})

tablesave=input("Do you want to save the data to a excel spreadsheet? y/n")
if tablesave == "y":
    final_df.to_excel(f"{club_name}_records.xlsx", index=False)
    print(f"Data saved to '{club_name}_records.xlsx' successfully.")
else:
    pass


print("The most frequently listed nation is ", statistics.mode(NationList))
print("The average number of appearances in the top 25 for", club_name.replace("-", " ").title(), "is: ", round(statistics.mean(AppsList)))

max_apps = max(AppsList)
top_apps_player = PlayerList[AppsList.index(max_apps)]
print(f"The player with most appearances is", {top_apps_player}," with", {max_apps})

max_goals = max(GoalsList)
top_goals_player = PlayerList[GoalsList.index(max_goals)]
print(f"The all time top scorer is", {top_goals_player}, "with", {max_goals})

max_assists = max(AssistsList)
top_assists_player = PlayerList[AssistsList.index(max_assists)]
print(f"The all time top assister is:", {top_assists_player}, "with", {max_assists})

graphplot=input("Do you want to display a graph? y/n")
if graphplot=="y":
    # Plotting
    plt.figure(figsize=(14, 8))

    # Plot appearances
    plt.plot(final_df['Player'], final_df['Apps'], label='Appearances', marker='o')

    # Plot goals
    plt.plot(final_df['Player'], final_df['Goals'], label='Goals', marker='o')

    # Plot assists
    plt.plot(final_df['Player'], final_df['Assists'], label='Assists', marker='o')

    # Add labels and title
    plt.xlabel('Player')
    plt.ylabel('Count')
    plt.title(f"{club_name.replace('-', ' ').title()} Players' Appearances, Goals, and Assists")
    plt.xticks(rotation=90)
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.show()
else:
    exit()
