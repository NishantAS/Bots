from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def index():
  return "Hello Bot Online"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def main():
    print('Not A Runable Module')

if __name__ == '__main__':
    main()