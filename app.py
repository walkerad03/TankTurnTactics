'''
This module handles the server side of the tank turn tactics website.
'''

import os
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, \
    session, jsonify, send_from_directory
from flask_socketio import SocketIO
from gamemanager import GameManager

app = Flask(__name__)


# helper function to store updated data into the database
def _save_player_data():
    print(session['data_json'])
    # df = pd.read_json(data)
    # df.to_csv('playerData.csv')


# helper function to load player data from the database to the server
def _load_player_data():
    df_data = pd.read_csv('playerData.csv')
    df_data['isClient'] = (df_data['username'] == session['uname'])
    session['data_json'] = df_data.to_json(orient='records')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/')
def load_login():
    '''Redirects clients who travel to the root URL.'''
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Confirms logging in for client and forwards game data to the client'''
    if request.method == 'POST':
        session['uname'] = request.form['username']
        _load_player_data()
        return redirect(url_for('play'))
    return render_template('login.html')


@app.route('/play')
def play():
    '''Sends base webpage to players after logging in'''
    return render_template('index.html', player_data=session['data_json'])


@app.route('/play', methods=['POST', 'GET'])
def handle_move():
    '''Handles client game move data'''
    if request.method == 'POST':
        move = request.form['move']

        _load_player_data()
        manager = GameManager(session['data_json'])
        session['data_json'] = manager.handle_move(move)
        _save_player_data()

        return jsonify({'player_data': session['data_json']})
    return render_template('index.html', player_data=session['data_json'])


if __name__ == '__main__':
    app.secret_key = 'key:)'
    socket = SocketIO(app)
    socket.run(app)
