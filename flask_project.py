from flask import Flask

# backend basic
app = Flask(__name__)
@app.route('/')

def hello():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run(debug=True)