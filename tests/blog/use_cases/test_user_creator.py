from unittest.mock import patch

import pytest
from app.blog.domain.errors.username_aready_exits import UserAlreadyExits
from app.blog.infrastructure.storage.user_repository_memory import UserRepositoryMemory
from app.blog.use_cases.user_creator import UserCreator
from app.shared.services.infrastructure.password_service_fake import PasswordServiceFake


def _create_new_use_case():
    repository = UserRepositoryMemory()
    repository.clear()
    password_service = PasswordServiceFake()
    return UserCreator(repository, password_service)


def test_should_create_user_when_email_and_username_is_not_used():
    use_case = _create_new_use_case()
    user = use_case.execute("someone", "S3CUR€ PA$$", "someone@example.com")
    assert user.id != "" and user.crated_at


def test_should_raise_error_when_email_already_exists():
    use_case = _create_new_use_case()
    use_case.execute("someone", "S3CUR€ PA$$", "someone@example.com")
    with pytest.raises(UserAlreadyExits):
        use_case.execute("second_one", "S3CUR€ PA$$", "someone@example.com")


def test_should_raise_error_when_username_already_exists():
    use_case = _create_new_use_case()
    use_case.execute("someone", "S3CUR€ PA$$", "someone@example.com")
    with pytest.raises(UserAlreadyExits):
        use_case.execute("someone", "S3CUR€ PA$$", "aaaa@example.com")


@patch.object(UserRepositoryMemory, "save")
def test_should_save_on_repository(mock_save):
    use_case = _create_new_use_case()
    use_case.execute("someone", "S3CUR€ PA$$", "someone@example.com")
    mock_save.assert_called()


@patch.object(PasswordServiceFake, "hash")
def test_should_hash_password(mock_hash):
    use_case = _create_new_use_case()
    use_case.execute("someone", "S3CUR€ PA$$", "someone@example.com")
    mock_hash.assert_called()
