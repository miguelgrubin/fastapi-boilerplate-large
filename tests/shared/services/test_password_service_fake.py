from app.shared.services import factories


def test_should_hash():
    service = factories.create_password_service("fake")
    password = "lalala2"

    assert service.hash(password) == password


def test_should_check():
    service = factories.create_password_service("fake")
    password = "lalala2"
    hash = service.hash(password)

    assert service.check(hash, password) == True
