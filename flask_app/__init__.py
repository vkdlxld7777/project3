from flask import Flask, render_template
import flask_app.lib.db_controll as db
import json


def create_app():
    
    app = Flask(__name__)
    
    @app.route('/')
    def main():
        return render_template('index.html'),200

    @app.route('/data_list',methods=["GET"])
    def data_list():
        data = db.db_select()
        json_data = []
        for i in data:
            json_data += [{
                "ranking" : i[0],
                "game" : i[1],
                "month" : i[2],
                "year" : i[3],
                "hours_watched" : i[4],
                "hours_streamed" : i[5],
                "peak_viewers" : i[6],
                "peak_channels" : i[7],
                "streamers" : i[8],
                "avg_viewers" : i[9],
                "avg_channels" : i[10],
                "avg_viewer_ratio" : i[11]
            }]
        json_dump = json.dumps({'data':json_data})
        json_data = json.loads(json_dump)
        return json_data, 200
    
    @app.route('/game_list')
    def game_list():
        data = db.game_list()
        json_data = {'game' : data}
        return json_data
    return app


