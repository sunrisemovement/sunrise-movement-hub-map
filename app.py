from flask import Flask, send_file
app = Flask(__name__)

with open("index.html", "r") as f:
  template_html = f.read()

@app.route("/")
def index():
  with open("hub_map.html", "r") as f:
    hubmap_html = f.read()
  return template_html.replace("INSERT_HUB_MAP_HTML", hubmap_html)

@app.route('/<path:filename>')
def show_file(filename=''):
  return send_file(filename)
