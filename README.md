# U.S. Bikeshare Data Explorer

Interactive command-line application for exploring bikeshare data from Chicago, New York City and Washington. Users select a city, month and day of the week, and the program dynamically filters the data before calculating travel, station and rider statistics.

## Features

- Validates city, month and weekday selections.
- Filters large CSV datasets with pandas.
- Reports the most common travel month, day and hour.
- Identifies popular start stations, end stations and routes.
- Calculates total and average trip duration.
- Summarizes user type, gender and birth-year data when available.
- Displays raw trip records in optional five-row batches.
- Allows users to restart the analysis without relaunching the program.

## Technologies

- Python
- pandas
- Command-line interface

## Repository structure

- `US_Bike_Share.py` — interactive data explorer
- `chicago.csv` — Chicago bikeshare data
- `new_york_city.csv` — New York City bikeshare data
- `washington.csv` — Washington bikeshare data
- `requirements.txt` — Python dependencies

## Running the application

Create and activate a virtual environment, then install the dependency:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Run the program from the repository root so it can locate the CSV files:

```bash
python US_Bike_Share.py
```

Follow the prompts to select a city, month and weekday. Enter `all` when you do not want to apply a month or weekday filter.

## Statistics produced

- Most frequent month, weekday and start hour
- Most commonly used start and end stations
- Most frequent station combination
- Total and average trip duration
- User-type counts
- Gender and birth-year statistics where available

## Data source

The datasets were provided for Udacity's Programming for Data Science with Python project and contain anonymized bikeshare trips from the first half of the year.

## Limitations

- Available demographic columns differ by city.
- The included datasets cover a limited period and should not be treated as a complete representation of annual travel behaviour.
- CSV files are intentionally included for reproducibility, which increases the repository size.

