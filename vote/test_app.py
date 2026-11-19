import pytest

import app as vote


class FakeRedis:
    def __init__(self):
        self.votes = {}

    def get(self, key):
        return self.votes.get(key)

    def incr(self, key):
        self.votes[key] = self.votes.get(key, 0) + 1
        return self.votes[key]


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(vote, "redis", FakeRedis())
    return vote.app.test_client()


def test_options(client):
    option_a, option_b = vote.getOptions()

    response = client.get("/")

    assert response.status_code == 200
    assert f"{option_a} vs {option_b}" in response.get_data(as_text=True)


def test_vote(client):
    response = client.post("/", data={"vote": "a"})

    assert response.status_code == 200
    assert "1 vs 0" in response.get_data(as_text=True)
