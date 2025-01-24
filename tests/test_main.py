import pytest
from scrape_articles.main import app, is_unwanted_text

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_is_unwanted_text():
    assert is_unwanted_text("") == True
    assert is_unwanted_text("Click here to sign up") == True
    assert is_unwanted_text("Normal article text") == False
    assert is_unwanted_text("SMALL CAPS") == False
    assert is_unwanted_text("THIS IS A VERY LONG ALL CAPS LINE THAT SHOULD BE FILTERED") == True

def test_process_urls_empty(client):
    rv = client.post('/process', data={'urls': ''})
    assert rv.status_code == 200 