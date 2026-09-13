marks = int(input("Apne marks likho (0-100): "))

if marks >= 80:
    print("Grade: A+ (Outstanding!)")
elif marks >= 60:
    print("Grade: B (Good job!)")
elif marks >= 40:
    print("Grade: C (Pass)")
else:
    print("Grade: Fail (Mehnat ki zaroorat hai)")