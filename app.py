#!/usr/bin/python

import json
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, \
    session
from gamemanager import GameManager as GM

app = Flask(__name__)


def load_player_data(uname):
    data = pd.read_csv('playerData.csv')
    data['isClient'] = (data['username'] == uname)
    session['player_data'] = data.to_dict('records')
    session['player_json'] = data.to_json(orient='records')


@app.route('/')
def load_login():
    return redirect(url_for('login'))


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        uname = request.form['username']
        load_player_data(uname)
        return redirect(url_for('play'))
    return render_template('login.html')


@app.route('/play')
def play():
    return render_template('index.html', player_data=session['player_json'])


@app.route('/play', methods=['POST', 'GET'])
def handle_move():
    manager = GM(session['player_data'])
    if (request.method == 'POST'):
        session['player_data'] = manager.handle_move(request.form.get('movelist'))
    request.cookies.get('player_json', False)
    session['player_json'] = json.dumps(session['player_data'])
    return render_template('index.html', player_json=session['player_json'])


if __name__ == '__main__':
    app.secret_key = 'key:)'
    app.session_cookie_samesite = "lax"
    app.run()
