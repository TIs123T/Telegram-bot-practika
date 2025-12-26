class Settings:
    BOT_TOKEN: str = "8508612481:AAG0PDyOjapQqW4hQ10budFOXYeszv4sLZ4"
    
    # SQLite база — файл tools.db будет создан автоматически в папке проекта
    DB_URL: str = "sqlite+aiosqlite:///tools.db"

settings = Settings()