# Amazon Price Tracker

A Python script that monitors the price of a specific Amazon product and sends an email alert when the price drops below a set threshold.

## Features
- Scrapes product price and title from an Amazon product page
- Sends email notifications when price drops below the specified threshold
- Uses environment variables for secure credential management
- Customizable product URL and price threshold

## Prerequisites
- Python 3.x
- Required Python packages (install via pip):
  - `beautifulsoup4`
  - `requests`
  - `python-dotenv`

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker
