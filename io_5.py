str = input("enter a string:")
try:
    i = float(str)
    print("\nNumeric")
except (ValueError, TypeError):
    print('\nNot numeric')