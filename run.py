from app import create_app

app = create_app('DevelopmentConfig')

if __name__ == "__main__":
    app.run(debug=True, port=5002)