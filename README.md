# NOAA CMORPH Precipitation Data Scraper 🌧️

I made this script for a [good friend](https://github.com/XdstruCTor) of mine that needed to get a large volume of weather data for his Data Science project. I developed this python script scrapes NetCDF (.nc) files from the NOAA CMORPH PDS hourly precipitation dataset hosted on an AWS S3-backed HTML index. It automatically downloads .nc files from every day between January 1, 2000 and December 31, 2020, storing them in date-specific directories.

## 📦 Features
•	Navigates through a structured online directory by date.

•	Downloads all .nc (NetCDF) files found in HTML tables.

•	Organizes downloaded data by date (e.g., downloaded_files/year_2000_month_01_day_01/).

•	(Optionally) includes a function to process NetCDF data (requires additional implementation).


 ## 🛠️ Requirements

Install the following libraries before running:
```bash
pip install requests beautifulsoup4 netCDF4
```

## 🧪 Usage

1.	Clone this repo or copy the scraper.py file.
2.	Run the script:
 ```bash
python scraper.py
```
The files will be downloaded into a folder named downloaded_files, organized by year, month, and day.

## 📌 Notes
•	The script is set to scrape data from 2000 to 2020. You can change this range by editing the for year in range(...) loop.

•	The process_netcdf() function is a placeholder. You can extend it to analyze NetCDF contents after downloading.

## 💡 Future Improvements
•	Add multi-threading for faster downloads.

•	Enable resume capability in case of interruptions.

•	Add CLI flags for date range filtering.

•	Convert .nc to .csv automatically.
