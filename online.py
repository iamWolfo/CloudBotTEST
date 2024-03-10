from threading import Thread

from flask import Flask

app = Flask('')


@app.route('/')
def home():
  with open('index.html', 'r') as f:
    prossessing = f.read()
    return prossessing


def run():
  app.run(host='0.0.0.0', port=2404)


def keep_alive():
  t = Thread(target=run)
  t.start()