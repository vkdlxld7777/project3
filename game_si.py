import flask_app.lib.twitch_data as tw
import flask_app.lib.db_controll as db
import json
import time



# CLIENT_ID = '1jjn6ii4ipolph9xwyba2ufja2h4gu'
# CLIENT_SECRET = 'zr82n93qz4x9y2vsdjdlhrp7vzj7io'
# token, type = tw.create_token(CLIENT_ID,CLIENT_SECRET)
# list_data = tw.twitch_rank_list(token,CLIENT_ID,3)
# start = time.time()
# for i in list_data:
#     game_data = tw.game_rank_data(i)
#     db.db_insert(game_data)
# end = time.time()
# breakpoint()
# print(end)
data = db.game_list()
breakpoint()       
print()