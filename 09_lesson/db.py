DB_USER = "postgres"
DB_PASSWORD = "2410"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Holm"


DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
