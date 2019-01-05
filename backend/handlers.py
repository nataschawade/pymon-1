import bottle
from bottle import (Bottle, get, post, put, redirect, request, response, jinja2_view)
import json
from backend import utils
from backend import controller
from backend import db
import os
bottle.TEMPLATE_PATH.insert(0, os.getcwd())

app = Bottle()

@app.get('/games/<game_id>/status')
def status(game_id):
    currentPlayerName = request.get_cookie("player")
    currentPlayerAvatar = db.getAvatar(currentPlayerName)
    print(currentPlayerAvatar['avatar'])
    gameStatus = controller.generateGameStatus(game_id, currentPlayerName, currentPlayerAvatar)
    return utils.jsonResponse(response, gameStatus)

@app.post('/games/<game_id>/players')
def joinGameHandler(game_id):
    playerName = request.get_cookie("player")
    avatar = db.getAvatar(playerName)
    print(avatar)
    result = controller.joinGame(game_id, playerName, avatar['avatar'])
    print(result)
    return utils.jsonResponse(response, {"result":result})

@app.put('/games/<game_id>/players')
def playerReadyHandler(game_id):
    playerName = request.get_cookie("player")
    result = controller.markPlayerReady(game_id, playerName)
    return utils.jsonResponse(response, {"result":result})

@app.post('/games/<game_id>/turn')
def turnHandler(game_id):
    playerName = request.get_cookie("player")
    color = utils.reqBody(request.body, "color")
    result = controller.playTurn(game_id, playerName, color)
    return utils.jsonResponse(response, {"result":result})

@app.post('/players')
def newPlayerHandler():
    playerName = request.forms.get("name")
    avatar = request.POST.dict['avatar'][0]
    print(avatar)
    controller.createPlayer(playerName, avatar)
    response.set_cookie("player", playerName, path='/')
    redirect("/games")

@app.post('/games')
def create():
    controller.createGame(request.forms.get("name"), request.get_cookie("player"))
    redirect("/games")

@app.error(404)
@jinja2_view('./backend/pages/404.html')
def error404(error):
    return {"version" : utils.getVersion()}