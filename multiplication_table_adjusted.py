def print_multiplication_table(rows, cols):
    # מחשבים את רוחב השדה הדרוש לכל עמודה
    max_val = max([max(rows) * max(cols)] + rows + cols)
    width = len(str(max_val))

    # שורת כותרת
    header = ["".rjust(width)] + [str(c).rjust(width) for c in cols]
    print(" | ".join(header))
    print("-" * (len(" | ".join(header))))

    # השורות עצמן
    for r in rows:
        row_values = [str(r * c).rjust(width) for c in cols]
        print(str(r).rjust(width) + " | " + " | ".join(row_values))


# דוגמה לשימוש
rows = [2, 4, 6, 8, 10, 0.001]
cols = [3, 6, 9, 12, 0.002]
print_multiplication_table(rows, cols)