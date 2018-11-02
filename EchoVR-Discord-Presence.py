from pypresence import Presence
import time
import requests
import json

client_id = "500359009375748117"

RPC = Presence(client_id)
RPC.connect()

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
        print (game_state)

        if game_state == 'pre_match':
            game_state = 'Pre Match'
            clock = '00:00.00'
        elif game_state == 'round_start':
            game_state = 'Round Starting'
        elif game_state == 'playing':
            game_state = 'Playing'
        elif game_state == 'score':
            game_state = 'Team Scored'
        elif game_state == 'round_over':
            game_state = 'Round Over'
        elif game_state == 'pre_sudden_death':
            game_state = 'Pre Sudden Death'
        elif game_state == 'sudden_death':
            game_state = 'Playing Sudden Death'
        elif game_state == 'post_sudden_death':
            game_state = 'Post Sudden Death'
        elif game_state == 'post_match':
            clock = '00:00.00'
            game_state = 'Game Over'
        else:
            clock = clock
            game_state = ''

        try:
            for team in response_object['teams']:
                if (team['team']) == ('BLUE TEAM'):
                    for n in team['players']:
                        bluecount = bluecount + 1
                else:
                    for n in team['players']:
                        orangecount = orangecount + 1
            for stats in response_object['teams']:
                if (stats['team']) == ('BLUE TEAM'):
                    p = stats['stats']
                    bPoints = (str((p['points'])))
                else:
                    p = stats['stats']
                    oPoints = (str(p['points']))
        except KeyError:
            bluecount = '0'
            orangecount = '0'
            oPoints = '0'
            bPoints = '0'

        GameState = (game_state)

        state = ('Playing Pubs | ') + str(orangecount) + ('v') + str(bluecount) + (' | ') + (GameState)
        detail = ('In Arena | ') + (oPoints) + '-' + (bPoints) + ' | ' + (clock)

        RPC.update(state = state, details = detail, large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')

    except NameError:
        print ('Lobby')
        RPC.update(state = 'In Lobby', large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')

    time.sleep(10)
