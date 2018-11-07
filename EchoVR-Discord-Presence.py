from pypresence import Presence
import time
import echovr_api

epoch  = round(time.time())

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
    try:
        game_state = echovr_api.fetch_state()

        clock = game_state.game_clock_display

        print(clock)
        print(game_state.game_status)

        game_status_description = GAME_STATUS_DESCRIPTIONS.get(game_state.game_status, '')
        if game_state.game_status in ['round_over', 'post_match']:
            clock = '00:00.00'

        blue_team_size = len(game_state.blue_team.players)
        orange_team_size = len(game_state.orange_team.players)
        blue_points = game_state.blue_team.score
        orange_points = game_state.orange_team.score

        RPC.update(
            details = f"In Arena | {orange_points} - {blue_points} | {clock}",
            state = f"Playing Pubs | {orange_team_size}v{blue_team_size} | {game_status_description}",
            large_image = 'echobig',
            large_text = 'Echo Arena',
            small_image = 'echosmall',
            small_text = 'Echo VR')

    except:
        print('Lobby')
        RPC.update(
            state = 'In Lobby | Matchmaking',
            large_image = 'echobig',
            large_text = 'Echo Arena',
            small_image = 'echosmall',
            small_text = 'Echo VR',
            start = epoch)
    time.sleep(10)
