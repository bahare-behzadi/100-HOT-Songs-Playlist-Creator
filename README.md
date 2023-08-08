# 100-HOT-Songs-Playlist-Creator
Craft personalized playlists commemorating your anniversary days with the best songs. This app parses Billboard Hot 100 data and compiles curated Spotify playlists, transforming memories into melodies. Celebrate with music! A Spotify account and Developer Dashboard credentials are required.

## Prerequisites

- Python 3.x
- `spotipy` library (install using `pip install spotipy`)
- `requests` library (install using `pip install requests`)
- `beautifulsoup4` library (install using `pip install beautifulsoup4`)

## Getting Started

1. Clone this repository or download the script file.

2. Register your application on the Spotify Developer Dashboard to obtain your `CLIENT_ID` and `CLIENT_SECRET`. Set the `REDIRECT_URI` to an appropriate URL (e.g., http://example.com).

3. Replace the `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI` values in the script with your own credentials.

4. Run the script using the command:

   ```bash
   python main.py
   ```

5. Enter the desired year and press the "Save" button.

6. The script will retrieve the Billboard Hot 100 chart for the specified year, search for each song on Spotify, and create a playlist with the top tracks from that date.

7. The playlist will be created on your Spotify account.

## Notes

- You need a Spotify account to use this script.
- Make sure to grant the necessary permissions to your Spotify application on the Spotify Developer Dashboard.


![spotify image](https://github.com/bahare-behzadi/100-HOT-Songs-Playlist-Creator/assets/53374314/b36faea4-3bdd-41c1-af4a-bebf537679f0)
![app image](https://github.com/bahare-behzadi/100-HOT-Songs-Playlist-Creator/assets/53374314/08e7aedc-5821-4f1d-87fc-0a38878b975f)
