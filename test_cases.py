"""Unit tests for case management"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db.session import get_db
from app.models.base import Base
from app.models.case import Case, CaseStatus, CustodyStatus
from app.models.user import User, UserRole
from app.core.security import get_password_hash

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(scope="function")
def setup_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    user = User(
        email="judge@test.com",
        hashed_password=get_password_hash("password"),
        full_name="Test Judge",
        role=UserRole.JUDGE,
    )
    db.add(user)
    db.commit()

    from datetime import date, timedelta
    case = Case(
        cnr_number="TEST123456",
        filing_number="123/2024",
        filing_date=date.today() - timedelta(days=200),
        case_type="criminal",
        status=CaseStatus.PENDING,
        petitioner="State",
        respondent="Accused A",
        court_id=1,
        custody_status=CustodyStatus.UNDERTRIAL,
        detention_start_date=date.today() - timedelta(days=100),
        adjournment_count=12,
    )
    db.add(case)
    db.commit()

    yield db
    Base.metadata.drop_all(bind=engine)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_login(setup_db):
    response = client.post("/api/v1/auth/login", data={
        "username": "judge@test.com",
        "password": "password"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_list_cases(setup_db):
    login = client.post("/api/v1/auth/login", data={
        "username": "judge@test.com",
        "password": "password"
    })
    token = login.json()["access_token"]

    response = client.get("/api/v1/cases/", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_analyze_case(setup_db):
    login = client.post("/api/v1/auth/login", data={
        "username": "judge@test.com",
        "password": "password"
    })
    token = login.json()["access_token"]

    response = client.post("/api/v1/cases/1/analyze", headers={
        "Authorization": f"Bearer {token}"
    })
    assert response.status_code == 200
    data = response.json()
    assert "analysis" in data
    assert data["analysis"]["priority_score"] > 0
