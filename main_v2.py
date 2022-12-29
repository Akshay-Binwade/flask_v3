from flask import Flask
from crud_ops.starwars import crud_app

app = Flask(__name__)

app.register_blueprint(crud_app)


if __name__ == '__main__':
    app.run(port = 2000)