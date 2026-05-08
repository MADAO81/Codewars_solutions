# [BUG] XCOM-409: Flight distance of Interceptor planes is miscalculated
# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*

def travel_distance(avg_speed, travel_time):
    KM_PER_KNOT = 1.852
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles * KM_PER_KNOT
    return travel_kms
