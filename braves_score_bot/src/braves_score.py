import requests
import pytz
from datetime import datetime

TEAM_ABBR = "ATL"
SCOREBOARD_URL = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

def fetch_scoreboard():
    response = requests.get(SCOREBOARD_URL)
    response.raise_for_status()
    return response.json()

def get_braves_game_info():
    data = fetch_scoreboard()
    braves_game = None
    for event in data.get("events", []):
        for comp in event.get("competitions", []):
            competitors = comp.get("competitors", [])
            braves_team = next((team for team in competitors if team['team']['abbreviation'] == TEAM_ABBR), None)
            opponent_team = next((team for team in competitors if team['team']['abbreviation'] != TEAM_ABBR), None)
            if braves_team and opponent_team:
                braves_game = {
                    "status": comp.get("status", {}).get("type", {}).get("description", ""),
                    "braves_score": int(braves_team['score']),
                    "opponent": opponent_team['team']['displayName'],
                    "opponent_score": int(opponent_team['score']),
                    "event_time_utc": event.get("date"),
                    "opponent_abbr": opponent_team['team']['abbreviation'],
                }
                break
        if braves_game:
            break
    return braves_game

def format_score_message(game_info):
    if not game_info:
        return "No current game information available."
    
    status = game_info["status"]
    braves_score = game_info["braves_score"]
    opponent = game_info["opponent"]
    opponent_score = game_info["opponent_score"]
    event_time_utc = game_info.get("event_time_utc")
    opponent_abbr = game_info.get("opponent_abbr", opponent[:3].upper())

    if status.lower() == "final":
        if braves_score > opponent_score:
            winner = "Braves"
        elif opponent_score > braves_score:
            winner = opponent
        else:
            winner = "No one"  # Tie game (rare in MLB)
        return f"Final: {braves_score}-{opponent_score}\n{winner} Win"
    elif status.lower() in ["in progress", "in-progress", "live"]:
        return f"In Progress: {braves_score}-{opponent_score}"
    elif status.lower() == "scheduled":
        # Format the time to local (Eastern) time
        if event_time_utc:
            dt_utc = datetime.fromisoformat(event_time_utc.replace("Z", "+00:00"))
            eastern = pytz.timezone("US/Eastern")
            dt_local = dt_utc.astimezone(eastern)
            time_str = dt_local.strftime("%I:%M %p %Z")
        else:
            time_str = "Unknown time"
        # Determine home/away and format accordingly
        # If Braves are home, show: OPP @ ATL; if away, show: ATL @ OPP
        if braves_score == 0:
            matchup = f"{opponent_abbr} @ ATL"
        else:
            matchup = f"ATL @ {opponent_abbr}"
        return f"Scheduled: First pitch at {time_str} ({matchup})"
    else:
        return f"Status: {status} | {braves_score}-{opponent_score}."

def check_for_score_change(previous_score, current_score):
    return previous_score != current_score

def get_current_score():
    game_info = get_braves_game_info()
    if game_info:
        return game_info["score"]
    return None

def fetch_braves_score():
    game_info = get_braves_game_info()
    return format_score_message(game_info)