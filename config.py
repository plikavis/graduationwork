
import dotenv
from pydantic_settings import BaseSettings
from utils.utils import abs_path_from_project


class Config(BaseSettings):
    BROWSER_VERSION: str = "100"
    LOGIN: str = "Test"
    PASSWORD: str = "Test"
    LOGIN_READ: str = "Test"
    PASSWORD_READ: str = "Test"
    BASE_URL: str = "https://graduationwork.testrail.io"
    ENDPOINT: str = "/index.php?/api/v2"
    LOGIN_SELENOID: str = "test"
    PASSWORD_SELENOID: str = "test"



dotenv.load_dotenv(dotenv_path=abs_path_from_project('.env.'))
settings = Config(_env_file=abs_path_from_project('.env'))
