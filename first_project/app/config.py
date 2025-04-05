from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    """Датакласс с конфигурацией БД."""

    database_url: str


@dataclass
class Config:
    """Датакласс с конфигурационными переменными."""

    db: DatabaseConfig
    secret_key: str
    debug: bool


def load_config(path: str = None) -> Config:
    """Загрузка конфигурации проекта из env файла."""
    env = Env()
    env.read_env(path)  # Загружаем переменные окружения из файла .env

    return Config(
        db=DatabaseConfig(database_url=env('DATABASE_URL')),
        secret_key=env('SECRET_KEY'),
        debug=env.bool('DEBUG', default=False),
    )


CONFIG = load_config()
