
from flask import Flask, request, render_template, send_from_directory
from urllib.request import pathname2url, url2pathname
import os, glob, sys

app = Flask("Flask Upload Server")

@app.route('/', methods=["GET", "POST"])
def home():
    print(app.config)
    if request.method=="GET":
        return docu()
    file = request.files["file"]
    file.save(os.path.join("cdn", file.filename))
    return "http://localhost:5000/cdn/{}".format(pathname2url(file.filename))

@app.route('/cdn/<path:codeword>')
def download_file(codeword):
    file = url2pathname(codeword)
    return send_from_directory("cdn", file, as_attachment=True)

def docu():
    return """
    Welcome to My Personal File Server
    ==================================
    Usage
    curl -i -X POST -F file=@$FILE_PATH  http://$HOST:PORT 
    """

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
