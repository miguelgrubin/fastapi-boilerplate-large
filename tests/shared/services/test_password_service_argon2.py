from app.shared import factory


def test_should_hash():
    service = factory.create_password_service("argon2")
    password = "lalala2"

    assert service.hash(password) != password


def test_should_check():
    service = factory.create_password_service("argon2")
    password = "lalala2"
    hash = service.hash(password)

    assert service.check(password, hash) == True
