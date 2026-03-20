import os
import settings
import datetime

def load_highscore():
    if os.path.exists(settings.SCORE_FILE):
        with open(settings.SCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0

def save_highscore(seconds):
    with open(settings.SCORE_FILE, "w") as file:
        file.write(str(seconds))

def format_time(seconds):
    return str(datetime.timedelta(seconds=seconds))

current_score = settings.HIGHSCORE
highscore = load_highscore()

if highscore == 0 or current_score > highscore:
    save_highscore(current_score)