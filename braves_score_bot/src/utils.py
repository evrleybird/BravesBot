def format_score_message(team_name, score, status):
    return f"{team_name} - Score: {score} | Status: {status}"

def format_error_message(error):
    return f"Error: {error}"

def format_game_update_message(game_info):
    teams = " vs. ".join(game_info['teams'])
    score = " - ".join(map(str, game_info['scores']))
    return f"Update: {teams} | Score: {score} | Status: {game_info['status']}"