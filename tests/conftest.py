import pytest
from django.core.management import call_command
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.transaction import atomic, DatabaseError


User = get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def partner():
    user = User.objects.create(
        email="partner@jafton.com",
        username="partner",
        password="TestPa@ssword",
    )
    user.set_password(user.password)
    user.save()
    return user


def partner_profile(partner):
    profile = UserProfile.objects.create(
        user=partner,
        bio='bio',
        birth_date="2012-12-12",
        gender="female"
    )
    return profile


@pytest.fixture
def user(db):
    user = User.objects.create(
        email="user@jafton.com",
        username="Jafton",
        password="TestPa@ssword",
        auth_type='via_email',
        is_active=True
    )
    return user


@pytest.fixture
def user_profile(user):
    profile = UserProfile.objects.create(
        user=user,
        bio='bio',
        birth_date="2012-12-12",
        gender="female"
    )
    return profile


@pytest.fixture
def auth_client(user, client):
    client = APIClient()
    client.force_authenticate(user)
    return client

    
@pytest.fixture(scope="class")
def init_db(request, django_db_setup, django_db_blocker):
    fixtures = getattr(request.cls, "fixtures", [])
    with django_db_blocker.unblock():
        if fixtures:
            call_command("loaddata", *fixtures)
        yield
        call_command("flush", "--no-input")


def transactional(func):
    def wrapper(*args, **kwargs):
        try:
            with atomic():
                func(*args, **kwargs)
                raise DatabaseError
        except DatabaseError:
            pass

    return wrapper
