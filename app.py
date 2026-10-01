from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello, World!</h1><br/> <a href='/about'><button>About</button></a><br/> <a href='/home'><button>Home</button></a>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><br/> <a href='/'><button>Home</button></a>"

@app.route('/home')
def home():
    return "<h1>Home Page</h1><br/> <a href='/about'><button>About</button></a>"

if __name__ == '__main__':
    app.run()
