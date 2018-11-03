from pypresence import Presence
import time
import requests
import json

client_id = "500359009375748117"

RPC = Presence(client_id)
RPC.connect()

GAME_STATUS_DESCRIPTIONS = {
  'pre_match': 'Pre Match',
  'round_start': 'Round Starting',
  'playing': 'Playing',
  'score': 'Team Scored',
  'round_over': 'Round Over',
  'pre_sudden_death': 'Pre Sudden Death',
  'sudden_death': 'Playing Sudden Death',
  'post_sudden_death': 'Post Sudden Death',
  'post_match': 'Game Over',
}

while True:
    blue_team_size = 0
    orange_team_size = 0
    try:
        response = requests.get('http://127.0.0.1/session')
        response_text = response.text.rstrip('\0')
        response_object = json.loads(response_text)

        clock = response_object['game_clock_display']
        print(clock)

        game_status = response_object['game_status']
        print(game_status)

        game_status_description = GAME_STATUS_DESCRIPTIONS.get(game_status, '')
        if game_status in ['pre_match', 'post_match']:
            clock = '00:00.00'

        try:
            for team in response_object['teams']:
                if team['team'] == 'BLUE TEAM':
                    for _player in team['players']:
                        blue_team_size = blue_team_size + 1
                    stats = team['stats']
                    blue_points = stats['points']
                else:
                    for _player in team['players']:
                        orange_team_size = orange_team_size + 1
                    stats = team['stats']
                    orange_points = stats['points']
        except KeyError:
            blue_team_size = 0
            orange_team_size = 0
            orange_points = 0
            blue_points = 0

        RPC.update(
            details = f"In Arena | {orange_points} - {blue_points} | {clock}",
            state = f"Playing Pubs | {orange_team_size}v{blue_team_size} | {game_status_description}",
            large_image = 'echobig',
            large_text = 'Echo Arena',
            small_image = 'echosmall',
            small_text = 'Echo VR')

    except NameError:
        print('Lobby')
        RPC.update(
            state = 'In Lobby',
            large_image = 'echobig',
            large_text = 'Echo Arena',
            small_image = 'echosmall',
            small_text = 'Echo VR')

    time.sleep(10)
