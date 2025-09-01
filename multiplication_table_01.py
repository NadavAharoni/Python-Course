def print_multiplication_table(rows, cols):
    # הדפסת שורת כותרת
    header = [" "] + [str(c) for c in cols]
    print(" | ".join(header))
    print("-" * (len(" | ".join(header))))

    # הדפסת כל שורה
    for r in rows:
        row_values = [str(r * c) for c in cols]
        print(str(r) + " | " + " | ".join(row_values))


# דוגמה לשימוש:
rows = [1, 2, 3, 4]
cols = [1, 2, 3, 4, 5]
print_multiplication_table(rows, cols)
