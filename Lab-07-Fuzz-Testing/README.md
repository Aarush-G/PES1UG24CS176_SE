# L6_L7_47 — Fuel Station

## Lab 7: Fuzz Testing

## About

This lab focuses on testing a Fuel Station application using fuzz testing with Python's Hypothesis library and Pytest.

The application contains three functions to process fuel purchases, calculate average pump volumes and calculate payable bills after discounts. Hypothesis is used to generate different inputs, including unexpected and invalid values, to identify cases that cause errors.

The application was then modified to handle invalid inputs without crashing. Additional checks were also added to reject non-finite numeric values such as `NaN` and infinity.

## Files

| File | Description |
|------|-------------|
| `fuel_station.py` | Fixed Fuel Station application |
| `test_fuel_station.py` | Hypothesis fuzz tests for all three functions |
| `Screenshots_Lab7.pdf` | PDF containing the lab screenshots |
| `screenshots/` | Individual screenshots captured during the lab |

## Functions Tested

1. `parse_purchase()` – Parses fuel grade and litres.
2. `volume_average()` – Calculates the average of pump volumes.
3. `payable_bill()` – Calculates the final bill after applying a discount and tax.

## Testing

The tests use Hypothesis to generate random strings and `None` values to check whether the functions handle unexpected inputs without crashing.

Additional tests verify that `parse_purchase()` and `payable_bill()` reject non-finite numeric values such as `NaN`, `inf` and `-inf`.

Run the tests using:

```bash
python3 -m pytest test_fuel_station.py -v
```

## Screenshots

The `screenshots/` directory contains:

- `Original_Output.png` – Output of the original application.
- `Fuzz_Test_Failures.png` – Test failures with the original application.
- `Fixed_Output.png` – Output of the corrected application.
- `Fuzz_Test_Passing.png` – Successful test execution after fixing the application.

The screenshots are also compiled into `Screenshots_Lab7.pdf`.

## Tools Used

- Python
- Hypothesis
- Pytest

## Result

The original application was tested using automatically generated inputs, and input-handling issues were identified. The application was modified to handle invalid inputs safely, and the updated tests passed.
