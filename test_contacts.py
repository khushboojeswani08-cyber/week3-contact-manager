# Basic tests for Week 3 Contact Management System

from contacts_manager import valid_phone, valid_email


def test_valid_phone():
    assert valid_phone("1234567890")
    assert valid_phone("+91 9876543210")
    assert not valid_phone("12345")


def test_valid_email():
    assert valid_email("test@example.com")
    assert not valid_email("invalid-email")


if __name__ == "__main__":
    test_valid_phone()
    test_valid_email()
    print("All tests passed!")
