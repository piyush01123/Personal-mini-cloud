
from flask import Flask, request, render_template, send_from_directory
from urllib.request import pathname2url, url2pathname
import os, glob, sys
from urllib.parse import urlparse

app = Flask("Personal mini cloud")

@app.route('/', methods=["GET", "POST"])
def home():
    app.config.host_url = urlparse(request.base_url).geturl()
    if request.method=="GET":
        return docu()
    file = request.files["file"]
    file.save(os.path.join("cdn", file.filename))
    return "wget {}/cdn/{}\n\n".format(app.config.host_url, pathname2url(file.filename))

@app.route('/cdn/<path:codeword>')
def download_file(codeword):
    file = url2pathname(codeword)
    return send_from_directory("cdn", file, as_attachment=True)

@app.route('/all')
def get_list():
    text = ["<b><u>All uploads</u></b>"]
    for file in os.listdir("cdn"):
        url = "{}cdn/{}".format(app.config.host_url, pathname2url(file))
        text.append("<a href='{0}'</a>{0}".format(url))
    return "<br>".join(text)


def docu():
    return """<span style="white-space: pre-line" id="myspan">
<h1>Welcome to Personal Mini Cloud.</h1>
Usage:
curl -i -X POST -F file=@FILE_PATH  %s \n
Replace FILE_PATH with absolute path of the file to be uploaded to the cloud. \n
<a id="allfileslink">List all uploads</a> \n
Star/fork/improve my source code:
<a href='https://github.com/piyush-kgp/Personal-mini-cloud'>https://github.com/piyush-kgp/Personal-mini-cloud</a> \n
NEW: You can also upload from browser now. \n
<input type="file" id="uploader"></input>
</span>
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
<script>
 $("document").ready(function(){
      $("#allfileslink").attr("href", window.location.href+'all');
      $("#uploader").change(function() {
        var form = new FormData();
        var fileInputElement = document.getElementById('uploader');
        form.append("file", fileInputElement.files[0]);
        $.ajax({
                  type: 'POST',
                  url: `/`,
                  processData: false,
                  contentType: false,
                  async: true,
                  cache: false,
                  data: form,
                  success: function (data) {
                    console.log(data);
                    window.location.href += 'all';
                  }
              })
      });
});
</script>
    """ % app.config.host_url


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
