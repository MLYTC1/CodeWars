def get_grade(s1, s2, s3):
    a = (s1+s2+s3)/3
    if 90 <= a <= 100:
        return 'A'
    if 80 <= a < 90:
        return 'B'
    if 70 <= a < 80:
        return 'C'
    if 60 <= a < 70:
        return 'D'
    if 0 <= a < 60:
        return 'F'
