
def parse_purchase(text):
    try:
        if not isinstance(text, str):
            return None

        parts = text.split(':')
        if len(parts) != 2:
            return None

        grade, litres = parts
        grade = grade.strip()
        litres = float(litres)

        if not grade or litres < 0:
            return None

        return grade.title(), litres

    except (ValueError, TypeError):
        return None


def volume_average(volumes_csv):
    try:
        if not isinstance(volumes_csv, str):
            return None

        values = [int(r.strip()) for r in volumes_csv.split(',')]

        if not values or any(value < 0 for value in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError, ZeroDivisionError):
        return None


def payable_bill(text):
    try:
        if not isinstance(text, str):
            return None

        parts = text.split('|')
        if len(parts) != 2:
            return None

        bill, discount = parts
        bill = float(bill)
        discount = float(discount)

        if bill < 0 or discount < 0:
            return None

        total = bill * 1.18 - discount
        return max(total, 0)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_purchase ====")
    user_input = input("Enter grade:litres (e.g. diesel:25): ")
    result = parse_purchase(user_input)
    print("Grade and Litres:", result)

    print("\n==== Running volume_average ====")
    user_input = input("Enter pump volumes in litres as CSV (e.g. 10,25,40): ")
    result = volume_average(user_input)
    print("Average Volume:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 2500|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()
