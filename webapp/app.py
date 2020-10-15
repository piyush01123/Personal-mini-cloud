
from flask import Flask, request, render_template, send_from_directory
from urllib.request import pathname2url, url2pathname
import os, glob, sys

app = Flask("Flask Upload Server")

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return docu()
    file = request.files["file"]
    file.save(os.path.join("cdn", file.filename))
    return "wget https://personal-mini-cloud.herokuapp.com/cdn/{}\n\n".format(pathname2url(file.filename))

@app.route('/cdn/<path:codeword>')
def download_file(codeword):
    file = url2pathname(codeword)
    return send_from_directory("cdn", file, as_attachment=True)

@app.route('/all')
def get_list():
    return "<br>".join([
    "<b><u>All uploads</u></b>",
    *["wget <a href='https://personal-mini-cloud.herokuapp.com/cdn/{0}'>https://personal-mini-cloud.herokuapp.com/cdn/{0}</a>\n\n".format(pathname2url(file)) for file in os.listdir("cdn")]
    ])

def docu():
    return "<br>".join([
    "Welcome to Personal Mini Cloud.",
    "========================================================================================",
    "Usage:",
    "curl -i -X POST -F file=@FILE_PATH  https://personal-mini-cloud.herokuapp.com",
    "",
    "Replace FILE_PATH with absolute path of the file to be uploaded to the cloud."
    "","",
    "<a href='https://personal-mini-cloud.herokuapp.com/all'>List all uploads</a>",
    "",
    "Star/fork/improve my source code: <a href='https://github.com/piyush-kgp/File-upload-server'>https://github.com/piyush-kgp/File-upload-server</a>"
    ])

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
