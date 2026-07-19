from unittest import mock

from app.main import can_access_google_page


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_valid_and_has_internet(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://google.com")
    assert result is True


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_url_invalid(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = False
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://youtube.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_connection_is_lost(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = False
    result = can_access_google_page("https://youtube.com")
    assert result == "Not accessible"


@mock.patch("app.main.has_internet_connection")
@mock.patch("app.main.valid_google_url")
def test_can_access_google_page_when_all_data_is_valid(
    mock_valid_google_url: mock.MagicMock,
    mock_has_internet_connection: mock.MagicMock,
) -> None:
    mock_valid_google_url.return_value = True
    mock_has_internet_connection.return_value = True
    result = can_access_google_page("https://youtube.com")
    assert result == "Accessible"
