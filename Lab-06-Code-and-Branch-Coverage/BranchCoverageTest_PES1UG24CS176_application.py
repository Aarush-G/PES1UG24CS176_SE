
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# ---------------- FUEL BILL ----------------

def test_invalid_grade():
    with pytest.raises(ValueError):
        fuel_bill("electric", 20, "silver")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_silver_regular_covered():
    assert fuel_bill("regular", 10, "silver") == 0


def test_gold_regular_covered():
    assert fuel_bill("regular", 15, "gold") == 0


def test_gold_premium_covered():
    assert fuel_bill("premium", 20, "gold") == 0


def test_gold_diesel_covered():
    assert fuel_bill("diesel", 20, "gold") == 0


def test_regular_extra_small_purchase():
    assert fuel_bill("regular", 15, "silver") == 525


def test_diesel_extra_small_purchase():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_regular_extra_large_silver():
    assert fuel_bill("regular", 45, "silver") == 3465


def test_regular_extra_large_gold():
    assert fuel_bill("regular", 50, "gold") == 3325


def test_diesel_extra_large_gold():
    assert fuel_bill("diesel", 55, "gold") == 2800


# ---------------- PUMP PERMISSION ----------------

def test_fleet_within_limit():
    assert pump_allowed(200, 5, True) is True


def test_fleet_over_limit():
    assert pump_allowed(201, 5, True) is False


def test_non_fleet_within_limit_one_container():
    assert pump_allowed(60, 1, False) is True


def test_non_fleet_over_litre_limit():
    assert pump_allowed(61, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(30, 2, False) is False


# ---------------- SESSION STATUS ----------------

def test_card_day_active():
    assert session_status(60, True, False) == "active"


def test_cash_day_active():
    assert session_status(30, False, False) == "active"


def test_card_night_active():
    assert session_status(90, True, True) == "active"


def test_cash_night_active():
    assert session_status(60, False, True) == "active"


def test_card_day_warning():
    assert session_status(50, True, False) == "warning"


def test_cash_day_warning():
    assert session_status(20, False, False) == "warning"


def test_card_night_warning():
    assert session_status(80, True, True) == "warning"


def test_cash_night_warning():
    assert session_status(50, False, True) == "warning"


def test_card_day_timed_out():
    assert session_status(40, True, False) == "timed_out"


def test_cash_day_timed_out():
    assert session_status(10, False, False) == "timed_out"


def test_card_night_timed_out():
    assert session_status(60, True, True) == "timed_out"


def test_cash_night_timed_out():
    assert session_status(30, False, True) == "timed_out"
