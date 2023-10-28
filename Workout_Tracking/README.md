---

# Workout Tracking

This is a Python script that logs your physical activities to a Google Sheets document, allowing you to keep track of your workouts. It uses the Nutritionix API to gather exercise information based on user input and then stores it in a Google Sheets document using the Sheety API.

## Prerequisites

Before you can use this script, you'll need to set up a few things:

1. **Nutritionix API Credentials:** You need to obtain API credentials from Nutritionix. Once you have them, set the `NUTRITIONIX_APP_ID` and `NUTRITIONIX_API` environment variables to your API ID and API key.

2. **Sheety API Token:** You should get an API token from Sheety and set it as the `SHEETY_TOKEN` environment variable.

3. **Python Dependencies:** This script requires Python and some external libraries like `requests` and `os`. You can install these dependencies using pip:

   ```bash
   pip install requests
   ```

## Usage

1. Run the script by executing it with Python:

   ```bash
   python main.py
   ```

2. The script will prompt you to input information about your training or exercise.

3. It will then use the Nutritionix API to retrieve exercise details and post them to a Google Sheets document using the Sheety API.

4. You can access your workout log in the Google Sheets document specified in the `shetee_post_endpoint`.

5. The workout log will include the date, time, exercise name, duration, calories burned, and distance (if applicable).

6. Thank you for using this script to track your workouts! ❤️

## Contributing

If you have any suggestions or improvements for this script, feel free to create a pull request. Your contributions are welcome!

---

