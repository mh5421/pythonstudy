from __main__ import app
from flask import request, jsonify, render_template
from service.boardService import service as bService


@app.route('/bService', methods=["GET"])
def test():
    print("aaa")
    result = bService.selectBoard()
    return render_template('board.html',my_list=result)
