import requests
from bs4 import BeautifulSoup
import spotipy
import tkinter
import datetime

# -------------------------------APPEARANCE-------------------------

LINK = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"
REDIRECT_URI = "http://example.com"
PLAY_LIST_NAME = "Billboard 100"
YELLOW = "#F3E99F"
BROWN = "#C8AE7D"
DARK_BROWN = "#65451F"

window = tkinter.Tk()
window.title("Save Your Favorite Songs From Spotify")
window.config(padx=50, pady=50, bg=YELLOW)
window.iconbitmap("icon.ico")
header_frame = tkinter.Frame(window)
entry_frame = tkinter.Frame(window, bg=BROWN, highlightthickness=0)
image_frame = tkinter.Frame(window, bg=BROWN, highlightthickness=0)
button_frame = tkinter.Frame(window, bg=BROWN, highlightthickness=0)

header_frame.pack(expand=True, fill="both")
image_frame.pack(expand=True, fill="both")
entry_frame.pack(expand=True, fill="both")
button_frame.pack(expand=True, fill="both")
window.resizable(None, None)

header_label1 = tkinter.Label(header_frame, text='When you chose your date,\n press "Save" button to save'
                                                 '\n your list of songs', font=('arial', '15', 'bold'),
                              fg=DARK_BROWN, bg=YELLOW, highlightthickness=0)
header_label2 = tkinter.Label(header_frame, text='CALENDAR', font=('arial', '45', 'bold'), fg=BROWN,
                              bg=YELLOW, highlightthickness=0)
header_label1.pack(expand=True, fill="both")
header_label2.pack(expand=True, fill="both")

image_frame.picture = tkinter.PhotoImage(file="calender.png")
image_frame.label = tkinter.Label(image_frame, image=image_frame.picture, bg=BROWN)
image_frame.label.pack()

date_label = tkinter.Label(entry_frame, text="Day:", font=("arial", "20", "bold"), fg="#000000", bg=BROWN)

month_label = tkinter.Label(entry_frame, text="Month:", font=("arial", "20", "bold"), fg="#000000", bg=BROWN)

year_label = tkinter.Label(entry_frame, text="Year:", font=("arial", "20", "bold"), fg="#000000", bg=BROWN)

month_var = tkinter.IntVar(entry_frame)
year_var = tkinter.IntVar(entry_frame)
date_var = tkinter.IntVar(entry_frame)

current_month = datetime.date.today().month
current_year = datetime.date.today().year
current_date = datetime.date.today().day

month_var.set(current_month)
year_var.set(current_year)
date_var.set(current_date)

date_box = tkinter.Spinbox(entry_frame, from_=1, to=31, width=10, textvariable=date_var, font=('arial', '15'))

month_box = tkinter.Spinbox(entry_frame, from_=1, to=12, width=10, textvariable=month_var, font=('arial', '15'))

year_box = tkinter.Spinbox(entry_frame, from_=0000, to=3000, width=10, textvariable=year_var, font=('arial', '15'))

date_label.pack()
date_box.pack()
month_label.pack()
month_box.pack()
year_label.pack()
year_box.pack()


def close():
    window.destroy()


close_button = tkinter.Button(button_frame, text="Save", bg=DARK_BROWN, fg="#E0FFFF", command=close,
                              font=('arial', '15'))
close_button.pack()
window.mainloop()
if int(date_var.get()) < 10:
    chosen_day = f"0{date_var.get()}"
else:
    chosen_day = str(date_var.get())

if int(month_var.get()) < 10:
    chosen_month = f"0{month_var.get()}"
else:
    chosen_month = str(month_var.get())

chosen_year = year_var.get()
chosen_date = f"{chosen_year}-{chosen_month}-{chosen_day}"

# --------------------------SPOTIFY AUTHENTICATION AND GETTING SONGS LIST--------------------------------

response = requests.get(LINK + chosen_date)
soup = BeautifulSoup(response.text, "html.parser")
song_names = soup.find_all(name="h3", class_="a-no-trucate")
title_list = [' '.join((song.text.split())) for song in song_names]
answer = spotipy.Spotify(
    auth_manager=spotipy.SpotifyOAuth(
        client_id=CLIENT_ID,
        scope="playlist-modify-public",  # Use the correct scope for playlist modification
        redirect_uri="http://example.com",
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Your Username",
    )
)
user_id = answer.current_user()["id"]

uri_list = []
for name in title_list:
    result = answer.search(q=f"track:{name} year:{chosen_year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{name} doesn't exist in Spotify. Skipped.")
play_list = answer.user_playlist_create(user=user_id, name=str(chosen_year) + " " + PLAY_LIST_NAME)
answer.playlist_add_items(playlist_id=play_list['id'], items=uri_list)
