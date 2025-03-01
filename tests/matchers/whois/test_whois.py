import pytest

from abuse_whois.matchers.whois import get_contact_from_whois


@pytest.mark.parametrize(
    "hostname",
    [
        "1.1.1.1",
        "github.com",
    ],
)
def test_get_contact_from_whois(hostname: str):
    assert get_contact_from_whois(hostname) is not None
