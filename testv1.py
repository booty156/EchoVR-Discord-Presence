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
    except requests.exceptions.ConnectionError as e:
        print('Error')
        
    try:
        response_text = response.text.rstrip('\0')
    except NameError:
        print ('Lobby')
        RPC.update(state = 'In Lobby', large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')
        
    try:
        response_object = json.loads(response_text)
    except NameError:
        print('Error')
    except json.decoder.JSONDecodeError as e:
            print('Error')
        
    for clock in [response_object['game_clock_display']]:
        print (clock)
        
    for team in response_object['teams']:
        if (team['team']) == ('BLUE TEAM'):
            for n in team['players']:
                bluecount = bluecount + 1
        else:
            for n in team['players']:
                orangecount = orangecount + 1               

    for stats in response_object['teams']:               
        if (stats['team']) == ('BLUE TEAM'):
            for p in [stats['stats']]:
                bPoints = (str((p['points'])))
        else:
            for p in [stats['stats']]:
                oPoints = (str(p['points']))

    state = ('Playing Pubs | ') + str((orangecount)) + ('v') + str((bluecount))
    detail = ('In Arena | ') + (oPoints) + '-' + (bPoints) + ' | ' + (clock)

    RPC.update(state = state, details = detail, large_image = 'echobig', large_text = 'Echo Arena', small_image = 'echosmall', small_text = 'Echo VR')

    time.sleep(15)
