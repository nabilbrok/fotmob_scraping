import soccerdata as sd
import pandas as pd
from datetime import datetime
import os
pd.set_option('display.max_columns', None)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def liga():
    tanya = input("Mau liga apa? (Inggris/Italia/Spanyol/Jerman/Prancis): ").lower()
    if tanya == "inggris":
        liga = "ENG-Premier League"
    elif tanya == "italia":
        liga = "ITA-Serie A"
    elif tanya == "spanyol":
        liga = "ESP-La Liga"
    elif tanya == "jerman":
        liga = "GER-Bundesliga"
    elif tanya == "prancis":
        liga = "FRA-Ligue 1"
    else:
        print("Pilihan Tidak Tersedia")
    return liga

def musim():
    season = input("Mau musim apa? (Contohnya : \"2012/2013\" atau \"2013/2014\"): ").lower()
    return season

def team():
    tim = input("Mau tim apa? (Contohnya : \"Arsenal\" atau \"Chelsea\"): ").lower()
    return tim

def tabel_liga():

    league = liga()
    season = musim()

    fotmob = sd.FotMob(leagues=league, seasons=season)    

    league_table = fotmob.read_league_table()

    df = pd.DataFrame(league_table)

    if df.select_dtypes(include=['datetime64[ns, UTC]']).shape[1] > 0:
        for column in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
            df[column] = df[column].dt.tz_localize(None)

    # Create the directory if it doesn't exist
    directory = 'E:\\Coding\\Python\\scrape_fotmob\\hasil_cetakan'
    os.makedirs(directory, exist_ok=True)  # Creates the directory if it doesn't exist

    # Clean up league and season strings for the filename
    safe_league = league.replace(" ", "_").replace("-", "_")  # Replace spaces and dashes
    safe_season = season.replace("/", "_")  # Replace slashes

    # Create the Excel file path
    file_path = f'{directory}\\fotmob_{safe_league}_{safe_season}_{timestamp}.xlsx'

    # Write to Excel
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]
        # Loop through each column and set the width to fit the content
        for column in df.columns:
            max_len = max(
                df[column].astype(str).map(len).max(),  # Get max length in each column
                len(column)  # Get column header length
            )
            col_idx = df.columns.get_loc(column)  # Get the column index
            worksheet.set_column(col_idx, col_idx, max_len + 17) 

    print(f"File saved as {file_path}")

    print(f"File saved as {file_path}")

def jadwal_liga():

    league = liga()
    season = musim()

    fotmob = sd.FotMob(leagues=league, seasons=season)    

    schedule = fotmob.read_schedule()

    df = pd.DataFrame(schedule)

    # Ensure datetime columns are timezone unaware
    if df.select_dtypes(include=['datetime64[ns, UTC]']).shape[1] > 0:
        for column in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
            df[column] = df[column].dt.tz_localize(None)


    # Create the directory if it doesn't exist
    directory = 'E:\\Coding\\Python\\scrape_fotmob\\hasil_cetakan'
    os.makedirs(directory, exist_ok=True)  # Creates the directory if it doesn't exist

    # Clean up league and season strings for the filename
    safe_league = league.replace(" ", "_").replace("-", "_")  # Replace spaces and dashes
    safe_season = season.replace("/", "_")  # Replace slashes

    # Create the Excel file path
    file_path = f'{directory}\\fotmob_jadwal_{safe_league}_{safe_season}_{timestamp}.xlsx'

    # Write to Excel
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]
        # Loop through each column and set the width to fit the content
        for column in df.columns:
            max_len = max(
                df[column].astype(str).map(len).max(),  # Get max length in each column
                len(column)  # Get column header length
            )
            col_idx = df.columns.get_loc(column)  # Get the column index
            worksheet.set_column(col_idx, col_idx, max_len + 17) 

    print(f"File saved as {file_path}")

def statistik_liga():

    league = liga()
    season = musim()
    tim_apa = input("Mau data tim apa? (Tim yang ada di liga saat musim itu (HARUS LENGKAP!) (Contohnya : \"Valencia\"): ").title()

    fotmob = sd.FotMob(leagues=league, seasons=season)    

    match_stats = fotmob.read_team_match_stats(opponent_stats=False, team=f'{tim_apa}')

    df = pd.DataFrame(match_stats)

    # Ensure datetime columns are timezone unaware
    if df.select_dtypes(include=['datetime64[ns, UTC]']).shape[1] > 0:
        for column in df.select_dtypes(include=['datetime64[ns, UTC]']).columns:
            df[column] = df[column].dt.tz_localize(None)


    # Create the directory if it doesn't exist
    directory = 'E:\\Coding\\Python\\scrape_fotmob\\hasil_cetakan'
    os.makedirs(directory, exist_ok=True)  # Creates the directory if it doesn't exist

    # Clean up league and season strings for the filename
    safe_league = league.replace(" ", "_").replace("-", "_")  # Replace spaces and dashes
    safe_season = season.replace("/", "_")  # Replace slashes

    # Create the Excel file path
    file_path = f'{directory}\\fotmob_jadwal_{safe_league}_{safe_season}_{timestamp}.xlsx'

    # Write to Excel
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1')

        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]
        # Loop through each column and set the width to fit the content
        for column in df.columns:
            max_len = max(
                df[column].astype(str).map(len).max(),  # Get max length in each column
                len(column)  # Get column header length
            )
            col_idx = df.columns.get_loc(column)  # Get the column index
            worksheet.set_column(col_idx, col_idx, max_len + 24) 

    print(f"File saved as {file_path}")

def main():
    mw_apa = input("Mau data apa? (liga/statistik/jadwal): ").lower()
    if mw_apa == "liga":
        tabel_liga()
    elif mw_apa == "jadwal":
        jadwal_liga()
    elif mw_apa == "statistik":
        statistik_liga()
    else:
        print("Pilihan Tidak Tersedia")


main()