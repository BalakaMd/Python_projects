---

# Weather Alert

This is a Python script that checks the weather forecast for a specific location and sends an alert via Twilio if rain is expected.
It utilizes the OpenWeatherMap API to fetch weather data and Twilio for sending SMS alerts.

## Getting Started

### Prerequisites

Before you can use this script, you'll need:

- Python installed on your system.
- A valid OpenWeatherMap API key. You can obtain one [here](https://openweathermap.org/api).
- A Twilio account with your Account SID and Auth Token. You can sign up for Twilio [here](https://www.twilio.com/try-twilio).

### Installation

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/BalakaMd/Python_projects/weather_alert.git
   cd weather_alert
   ```

2. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the `main.py` file in a text editor or an Integrated Development Environment (IDE).

4. Update the following variables with your own credentials:

   - `API_KEY`: Your OpenWeatherMap API key.
   - `MY_LAT` and `MY_LONG`: Your latitude and longitude coordinates.
   - `ACCOUNT_SID` and `AUTH_TOKEN`: Your Twilio account credentials.
   - `from_` and `to`: Twilio phone numbers for sending and receiving SMS alerts.

## Usage

Run the script with the following command:

```bash
python main.py
```

The script will check the weather forecast for your specified location and send an SMS alert if rain is expected.
You'll receive a message if rain is in the forecast, along with a notification of the message status.


## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/api) for weather data.
- [Twilio](https://www.twilio.com/) for SMS alerts.

Feel free to contribute, report issues, or suggest improvements to this repository!

---
