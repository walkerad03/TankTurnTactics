#!/usr/bin/python

import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, \
    session, jsonify
from gamemanager import GameManager as GM

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


@app.route('/')
def load_login():
    return redirect(url_for('login'))


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        session['uname'] = request.form['username']
        _load_player_data()
        return redirect(url_for('play'))
    return render_template('login.html')


@app.route('/play')
def play():
    return render_template('index.html', player_data=session['data_json'])


@app.route('/play', methods=['POST', 'GET'])
def handle_move():
    if (request.method == 'POST'):
        move = request.form['move']
        print(move)

        _load_player_data()
        print(session['data_json'])
        gm = GM(session['data_json'])
        session['data_json'] = gm.handle_move(move)
        _save_player_data()

        return jsonify({'player_data': session['data_json']})
    return render_template('index.html', player_data=session['data_json'])


if __name__ == '__main__':
    app.secret_key = 'key:)'
    app.run(debug=True)
