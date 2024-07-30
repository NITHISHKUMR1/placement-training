def calculate_bonus(salary, rating):
    if rating <= 2:
        return 0
    elif rating <= 4:
        return 0.05 * salary
    else:
        return 0.10 * salary
