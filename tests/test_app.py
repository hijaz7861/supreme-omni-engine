import os

from app_web import app


def test_home_page_is_available():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Supreme Omni Engine" in response.data
    assert b"not yet implemented" in response.data


def test_health_endpoint():
    response = app.test_client().get("/healthz")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_status_does_not_expose_api_key(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-secret-value")
    response = app.test_client().get("/api/status")
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["engine_implemented"] is False
    assert payload["integrations"]["gemini_api_configured"] is True
    assert "test-secret-value" not in response.get_data(as_text=True)


def test_status_reports_missing_api_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    response = app.test_client().get("/api/status")
    assert response.get_json()["integrations"]["gemini_api_configured"] is False
