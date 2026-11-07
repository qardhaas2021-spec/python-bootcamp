# Mini Shop / Bill Calculator
# Style: small functions + chain steps (subtotal -> discount -> tax)

def subtotal(price, quantity):
    """Return price * quantity."""
    return price * quantity


def apply_discount(amount, percentage):
    """Return amount after discount."""
    return amount - (amount * percentage / 100)


def add_tax(amount, tax_percent):
    """Return amount after adding tax."""
    return amount + (amount * tax_percent / 100)


if __name__ == "__main__":
    # Full bill example: 2 items at 50, 10% off, 21% tax
    step1 = subtotal(50, 2)              # 100
    step2 = apply_discount(step1, 10)    # 90
    step3 = add_tax(step2, 21)           # 108.9

    print("Subtotal:", step1)
    print("After discount:", step2)
    print("Final bill:", step3)
