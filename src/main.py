from app.main import main

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Errore inatteso: {e}")
