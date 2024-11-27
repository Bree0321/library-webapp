from database import create_app
from routes import api

app = create_app()
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Library API!"

if __name__ == '__main__':
    app.run(debug=True)