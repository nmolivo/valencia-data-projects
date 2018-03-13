# Using the city of Valencia's Open Data
The materials in this folder are created and used by Natalie Olivo and Nicole Eickhoff during their data-vacation where they present their code and findings to the attendees of the Valencia Big Data Meetup [URL] at X location at Y time on ZZ/03/2018.
Brief descriptions of the directories in this folder:

<b>vb_datacollection</b>
1. vbscraper.py - This contains a Python Script (.py) executed on an AWS instance to obtain Valencia's bike-share (ValenBisi) data from Valencias Open Data Website.
2. valenbisi_scraper.ipynb - The backbone to vbscraper.py, commented in both English and Spanish for members to see how we collected data in a hands-on way. This is compatible with Jupyter Notebook.<br><Br>
*** Request for access to API key: 16/02/2018 ***

<b>vb_analysis</b>
1. 00_dataconcat.ipynb - We combine all data collected from our vbscraper.py
2. 01_eda.ipynb - Exploratory Data Analysis
3. 02_arima.ipynb - Autoregressive Integrated Moving Average Model
4. 03_feateng - varables for distance to CRIDA activities, hour, available per 15 minutes, available per hour

<b>vb_data</b><br>
Repository for storing datasets.<br><br>
This analysis was conducted with only station data. No data on rebalancing activity or individual bike rides were used.<br>
All data for this project was used for non-commercial purposes.
