from typing import Literal
import dotenv
from pydantic_settings import BaseSettings
from utils import abs_path_from_project


class Config(BaseSettings):
    contex: Literal["bstack", "selenoid", "local"] = "local"
    LOGIN: str = "vishpolina796@gmail.com"
    PASSWORD: str = "Polina21@"
    LOGIN_READ: str = "test@test.ru"
    PASSWORD_READ: str = "Polina21@"
    base_url: str = "https://graduationwork.testrail.io"
    api: str = "/index.php?/api/v2"


dotenv.load_dotenv(dotenv_path=abs_path_from_project(f'.env.{Config().contex}'))
settings = Config(_env_file=abs_path_from_project(f'.env.{Config().contex}'))
