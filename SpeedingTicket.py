# Write a program that is given two integers representing a speed limit and
# driving speed in miles per hour (mph) and outputs the traffic ticket amount.
# Driving 10 mph under the speed limit (or slower) receives a $50 ticket.
# Driving 6 - 20 mph over the speed limit receives a $75 ticket.
# Driving 21 - 40 mph over the speed limit receives a $150 ticket.
# Driving faster than 40 mph over the speed limit receives a $300 ticket.
# Otherwise, no ticket is received.
speed_limit = int(input())
driving_speed = int(input())

speed_calc = driving_speed - speed_limit
ticket_cost = 0

if speed_calc <= -10:
    ticket_cost = 50
elif 6 <= speed_calc <= 20:
    ticket_cost = 75
elif 20 < speed_calc <= 40:
    ticket_cost = 150
elif speed_calc > 40:
    ticket_cost = 300
else:
    ticket_cost = 0

print(ticket_cost)