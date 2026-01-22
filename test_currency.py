from unittest.mock import patch, Mock
from currency_api import convert_rubles_to_usd, get_currency_rate

@patch("currency_api.get_exchange_rate")
def test_convert_with_mock(mock_rate):
    mock_rate.return_value = 100

    result = convert_rubles_to_usd(500)

    assert result == 5

def test_get_rate_with_mock_argument():
    fake_api = Mock()
    fake_api.json.return_value = {"rate": 75}

    result = get_currency_rate(fake_api)
 
    assert result == 75