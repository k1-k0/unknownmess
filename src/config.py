import os


database_name = os.getenv("UNKM_DATABASE_NAME", "unknownmess")
database_host = os.getenv("UNKM_DATABASE_HOST", "localhost")
database_port = os.getenv("UNKM_DATABASE_PORT", "5432")
database_user = os.getenv("UNKM_DATABASE_USER", "postgres")
database_pass = os.getenv("UNKM_DATABASE_PASS", "postgres")
