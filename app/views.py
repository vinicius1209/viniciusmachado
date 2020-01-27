from flask import render_template, flash, url_for, request, abort, redirect, jsonify, session
from urllib.parse import urljoin, urlparse
from app import app

# Check if url is safe http://flask.pocoo.org/snippets/63/
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

# Dashboard
@app.route('/')
def index():
    return render_template('index.html') 