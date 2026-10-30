def get_grade(score):
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
        
    if score >= 70:
        return "A"

    elif score >= 60:
        return "B"

    elif score >= 50:
        return "C"

    elif score >= 45:
        return "D"

    else:
        return "F"