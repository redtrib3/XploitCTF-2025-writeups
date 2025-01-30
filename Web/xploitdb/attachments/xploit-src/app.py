from flask import Flask, render_template, request, redirect, send_file
from database.utils import query_exploits
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/source', methods=['GET'])
def source_code():
    return send_file('archive/xploit_src.zip', as_attachment=True)

@app.route('/search', methods=['GET'])
def search_route():
    keyword = request.args.get('x', None)
    by_col = request.args.get('by', None)

    if not keyword or not by_col:
        return redirect('/')

    exploits = query_exploits(keyword, by=by_col)

    if not exploits:
        return render_template('index.html', error="No exploits found :(")

    return render_template('index.html', exploits=exploits)

