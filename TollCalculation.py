def calc_toll(hour, is_morning, is_weekend):
    toll = 0
    # Convert 12 hour format to 24 hour format
    if is_morning:
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:
        if hour == 12: # 12 pm
            hour_24 = 12
        else:
            hour_24 = hour + 12
    if not is_weekend:
        if hour_24 < 7:
            toll = 1.15
        elif 7 <= hour_24 < 10:
            toll = 2.95
        elif 10 <= hour_24 < 15:
            toll = 1.90
        elif 15 <= hour_24 < 20:
            toll = 3.95
        else:
            toll = 1.40
    else:
        if hour_24 < 7:
            toll = 1.05
        elif 7 <= hour_24 < 20:
            toll = 2.15
        else:
            toll = 1.10

    return toll

# Type your code here.

if __name__ == '__main__':
    print(calc_toll(10, False, True))