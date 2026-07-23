from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    openai_api_key: str = ""
    model_name: str = "llama3.2"
    ollama_key: str = ""
    ollama_url: str = "" 

    log_level: str = "DEBUG"
    environment: str = ""

    class Config():
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()