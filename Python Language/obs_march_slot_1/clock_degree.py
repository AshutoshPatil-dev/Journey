h, m = map(int, input().split())

hour_angle = 30*h + 0.5*m
minute_angle = 6*m

angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)

print(f"{angle:.2f}")