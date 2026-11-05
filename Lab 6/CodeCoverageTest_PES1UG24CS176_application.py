
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# ---------------- FUEL BILL TESTS ----------------

def test_invalid_fuel_grade():
    with pytest.raises(ValueError):
        fuel_bill("electric", 20, "silver")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_litres_within_coverage():
    assert fuel_bill("regular", 8, "silver") == 0


def test_gold_regular_fuel_coverage():
    assert fuel_bill("regular", 15, "gold") == 0


def test_gold_premium_fuel_coverage():
    assert fuel_bill("premium", 20, "gold") == 0


def test_diesel_gold_no_additional_coverage():
    assert fuel_bill("diesel", 20, "gold") == 0


def test_regular_fuel_extra_litres():
    assert fuel_bill("regular", 15, "silver") == 525


def test_diesel_extra_litres():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_large_regular_purchase():
    assert fuel_bill("regular", 45, "silver") == 3465


def test_large_gold_purchase():
    assert fuel_bill("regular", 50, "gold") == 3325


def test_large_gold_diesel_purchase():
    assert fuel_bill("diesel", 55, "gold") == 2800


# ---------------- PUMP PERMISSION TESTS ----------------

def test_fleet_request_allowed():
    assert pump_allowed(200, 5, True) is True


def test_fleet_request_exceeds_limit():
    assert pump_allowed(201, 5, True) is False


def test_non_fleet_request_allowed():
    assert pump_allowed(60, 1, False) is True


def test_non_fleet_request_exceeds_limit():
    assert pump_allowed(61, 1, False) is False


def test_multiple_containers_not_allowed():
    assert pump_allowed(30, 2, False) is False


# ---------------- SESSION STATUS TESTS ----------------

def test_card_payment_active():
    assert session_status(60, True, False) == "active"


def test_cash_payment_active():
    assert session_status(30, False, False) == "active"


def test_night_session_active():
    assert session_status(90, True, True) == "active"


def test_session_warning():
    assert session_status(50, True, False) == "warning"


def test_session_timed_out():
    assert session_status(40, True, False) == "timed_out"


def test_night_session_warning():
    assert session_status(80, True, True) == "warning"


def test_night_session_timed_out():
    assert session_status(60, True, True) == "timed_out"
