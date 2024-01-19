
import dotenv
from pydantic_settings import BaseSettings
from utils.utils import abs_path_from_project


class Config(BaseSettings):
    browser_version: str = "100"
    LOGIN: str = "Test"
    PASSWORD: str = "Test"
    LOGIN_READ: str = "Test"
    PASSWORD_READ: str = "Test"
    base_url: str = "https://graduationwork.testrail.io"
    api: str = "/index.php?/api/v2"
    login_selenoid: str = "test"
    password_selenoid: str = "test"


dotenv.load_dotenv(dotenv_path=abs_path_from_project('.env.'))
settings = Config(_env_file=abs_path_from_project('.env'))
