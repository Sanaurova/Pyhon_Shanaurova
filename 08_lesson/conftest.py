import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def api_key():
    key = os.getenv("YOUGILE_API_KEY")
    if not key:
        pytest.fail("YOUGILE_API_KEY не задан в .env файле")
    return key


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")
