
# FotMob Data Scraper

A Python-based data scraper for FotMob to extract league tables, schedules, and team statistics from various football leagues. This project uses `soccerdata`, `pandas`, and `xlsxwriter` to organize and save the data into Excel files.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
  - [League Table](#league-table)
  - [Schedule](#schedule)
  - [Team Statistics](#team-statistics)
- [Output](#output)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fotmob-data-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fotmob-data-scraper
   ```
3. Install the required Python packages:
   ```bash
   pip install soccerdata pandas xlsxwriter
   ```

## Usage

1. Run the script:
   ```bash
   python fotmob_data_scraper.py
   ```
2. Follow the prompts to select the league, season, and team as needed.

## Functionality

This project provides three main functionalities:

### 1. League Table
Fetches and saves the league table for a specified season and league.

- **Prompted Input:** League, Season
- **Example Usage:** Select "liga" to get the league table for the chosen league and season.

### 2. Schedule
Fetches and saves the match schedule for a specified league and season.

- **Prompted Input:** League, Season
- **Example Usage:** Select "jadwal" to retrieve the schedule.

### 3. Team Statistics
Fetches and saves individual team match statistics for a specified season.

- **Prompted Input:** League, Season, Team Name (e.g., "Valencia")
- **Example Usage:** Select "statistik" to get match statistics for a specified team.

## Output

Excel files are generated and saved in the specified directory path: `E:\Coding\Python\scrape_fotmob\hasil_cetakan`. The files are named according to the type of data, league, and season, with a timestamp to prevent overwriting.

### Output Examples:
- `fotmob_ENG_Premier_League_2019_2020_YYYYMMDD_HHMMSS.xlsx` (for a league table)
- `fotmob_jadwal_ESP_La_Liga_2020_2021_YYYYMMDD_HHMMSS.xlsx` (for a schedule)
- `fotmob_stats_FRA_Ligue_1_2021_2022_YYYYMMDD_HHMMSS.xlsx` (for team statistics)

---
