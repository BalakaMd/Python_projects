# International Space Station (ISS) Tracker

This Python script is designed to track the International Space Station (ISS) and send an email notification when the ISS is passing overhead your location during the night. It utilizes data from the [Open Notify API](http://api.open-notify.org/iss-now.json) for real-time ISS position and the [Sunrise-Sunset API](https://api.sunrise-sunset.org/json) for sunrise and sunset times.

## Prerequisites

Before you can use this script, you need to have the following set up:

- Python 3.x
- The `requests` library to make HTTP requests.
- A Gmail account with less secure apps access enabled (for sending email notifications).
- The `smtplib` library for sending emails.

## Getting Started

1. Clone this repository to your local machine or download the script directly.
   
2. Open the script and replace the placeholders with your Gmail email address and password.

```python
email = "example@gmail.com"
password = "@@@@@"
```

3. Update your geographical coordinates (latitude and longitude) to match your location.

```python
MY_LAT = 32.821150
MY_LONG = 34.969876
```

4. Run the script to start tracking the ISS.

## How It Works

- The script periodically checks the current ISS position using the Open Notify API.

- It compares the ISS position to your location and checks if it is within 5 degrees of latitude and longitude.

- It also checks if it is nighttime by comparing the current time with sunrise and sunset times obtained from the Sunrise-Sunset API.

- If both conditions are met (the ISS is overhead and it's nighttime), the script sends an email notification to your Gmail account.

## Contributing

Feel free to contribute to this project by submitting issues, proposing enhancements, or making pull requests.

## Acknowledgments

- The script uses data from the Open Notify API and Sunrise-Sunset API.

## Disclaimer

This script requires your Gmail credentials, so be cautious about using your primary email account.
It is recommended to create a secondary Gmail account for this purpose and use it in the script.
