from app import create_app

app = create_app()

if __name__ == "__main__":
    print("🚀 Starting Grazioso Salvare Enhanced Dashboard...")
    app.run(debug=True, port=5000)