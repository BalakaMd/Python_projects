# Telegram weather alert

## Introduction
This Python script is designed to provide weather updates via a Telegram bot.
It fetches current weather data for a specified location and sends it to one or more Telegram chats.
This README provides a brief overview of the script and instructions on how to set it up.

## Getting Started
Before using this script, you need to complete the following steps:

1. **OpenWeather API Key**: You'll need an API key from OpenWeather to access their weather data.
2.  You can obtain an API key by signing up on their website [here](https://openweathermap.org/api).

3. **Telegram Bot**: Create a Telegram bot and obtain the API token.
   You can do this by talking to the [BotFather](https://core.telegram.org/bots#botfather) on Telegram.

5. **Telegram Chat IDs**: You need to obtain the chat IDs for the users or groups where you want to send weather updates.
   The script is currently set up to send updates to a list of `CHATS_ID`, which you should replace with the actual chat IDs.

## Usage
1. Clone or download this repository to your local machine.

2. Open the script in your preferred code editor.

3. Replace the following placeholders with your actual API keys, coordinates, and chat IDs:
   - `API_KEY`: Your OpenWeather API key.
   - `MY_LAT` and `MY_LONG`: Latitude and longitude for the location you want weather updates for.
   - `TG_TOKEN`: Your Telegram bot API token.
   - `CHATS_ID`: List of chat IDs where you want to send updates.

4. Run the script.

## Understanding the Code
- The script uses the `requests` library to fetch weather data from OpenWeather using their REST API.

- It then parses the JSON response to extract relevant weather information, including the weather description, current temperature, feels-like temperature, maximum and minimum temperatures, and humidity.

- The code is set up to send the weather information as a message to the specified Telegram chats. However, this part of the code is currently commented out. To enable it, uncomment the relevant code section and update the message text as needed.

## Dependencies
The script uses the following Python libraries, which you can install using `pip`:
- `requests`: For making HTTP requests to the OpenWeather API.
- `telegram` (optional): For sending messages via Telegram. Uncomment this part of the code if you want to enable Telegram notifications.

## Disclaimer
This script is a basic example and may require further customization to suit your specific needs.
Make sure to handle your API keys and sensitive information securely.

## Author
BalakMd

If you have any questions or encounter issues with the script, feel free to reach out to the author for assistance.

Happy coding!
