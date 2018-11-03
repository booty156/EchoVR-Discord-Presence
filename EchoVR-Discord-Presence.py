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
    bluecount = 0
    orangecount = 0
    try:
        response = requests.get('http://127.0.0.1/session')
        response_text = response.text.rstrip('\0')
        response_object = json.loads(response_text)

        clock = response_object['game_clock_display']
        print(clock)

        game_state = response_object['game_status']
        print(game_state)

        game_status_description = GAME_STATUS_DESCRIPTIONS.get(game_state, '')
        if game_state in ['pre_match', 'post_match']:
            clock = '00:00.00'

        try:
            for team in response_object['teams']:
                if (team['team']) == ('BLUE TEAM'):
                    for n in team['players']:
                        bluecount = bluecount + 1
                    p = team['stats']
                    bPoints = (str((p['points'])))
                else:
                    for n in team['players']:
                        orangecount = orangecount + 1
                    p = team['stats']
                    oPoints = (str(p['points']))
        except KeyError:
            bluecount = '0'
            orangecount = '0'
            oPoints = '0'
            bPoints = '0'

        state = ('Playing Pubs | ') + str(orangecount) + ('v') + str(bluecount) + (' | ') + (game_status_description)
        detail = ('In Arena | ') + (oPoints) + '-' + (bPoints) + ' | ' + (clock)

        RPC.update(state = state, details = detail, large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')

    except NameError:
        print ('Lobby')
        RPC.update(state = 'In Lobby', large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')

    time.sleep(10)
