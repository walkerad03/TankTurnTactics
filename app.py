#!/usr/bin/python

from ctypes import util
from imp import lock_held
import json
from re import I, T, U
from socketserver import UnixDatagramServer
from termios import IUCLC
from xml.etree.ElementInclude import LimitedRecursiveIncludeError
from numpy import ubyte
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, \
    session, jsonify
from gamemanager import GameManager as GM

app = Flask(__name__)

def save_player_data(data):
    df = pd.read_json(data)
    df.to_csv('playerData.csv')

def load_player_data(uname):
    data = pd.read_csv('playerData.csv')
    data['isClient'] = (data['username'] == uname)
    session['player_data'] = data
    session['player_json'] = data.to_json(orient='records')


@app.route('/')
def load_login():
    return redirect(url_for('login'))


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        session['uname'] = request.form['username']
        load_player_data(session['uname'])
        return redirect(url_for('play'))
    return render_template('login.html')


@app.route('/play')
def play():
    return render_template('index.html', player_data=session['player_json'])


@app.route('/play', methods=['POST', 'GET'])
def handle_move():
    if (request.method == 'POST'):
        move = request.form['move']

        load_player_data(session['uname'])
        gm = GM(session['player_data'])
        player_data = gm.handle_move(move)
        save_player_data(player_data)


        return jsonify({'player_data': player_data})
    return render_template('index.html', player_data=session['player_json'])


if __name__ == '__main__':
    app.secret_key = 'key:)'
    # app.session_cookie_samesite = "lax"
    app.run(debug=True)
