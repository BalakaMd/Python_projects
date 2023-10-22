# Musical Time Mashine - Top 100 Songs to Spotify Playlist

This Python script allows you to create a Spotify playlist with the most popular songs from a your specific date according to the Billboard Hot 100 chart.

## Getting Started

To use this script, you'll need Python and a Spotify Developer account. Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/BalakaMd/Python_projects/Musical Time Mashine.git
   cd your-repo
   ```

2. Install the required Python libraries using `pip`:
   ```bash
   pip install requests beautifulsoup4 spotipy
   ```

3. Set up your Spotify Developer credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app and note down the Client ID and Client Secret.
   - Set the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET in the script.

4. Run the script:
   ```bash
   python billboard_to_spotify.py
   ```

5. Follow the prompts to enter the date you want to travel to and authorize Spotify access.
6. The script will create a private Spotify playlist with the popular songs from that date.

## Example Usage

```python
date = input("Which year did you want to travel to? Type the date in this format YYYY-MM-DD: ")
# ...

SPOTIPY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
# ...

# ...

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt",
    username='YOUR_SPOTIFY_USERNAME', ))

# ...
```

## Requirements

- Python 3.x
- Requests
- BeautifulSoup
- Spotipy


## Acknowledgments

- [Billboard](https://www.billboard.com) for providing the Hot 100 data.
- [Spotify](https://developer.spotify.com) for the music information and playlist creation.

```
