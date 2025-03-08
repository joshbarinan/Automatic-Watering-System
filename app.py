from flask import Flask
from dotenv import load_dotenv
from routes import bp
from config import Config

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
