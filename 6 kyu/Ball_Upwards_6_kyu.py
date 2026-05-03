# https://www.codewars.com/kata/566be96bb3174e155300001b/train/python

# g = 9.81

# def height(v,t):
#     return v*t - (g*(t**2))/2
# def max_ball(v0):
#     velocity_ms = v0 *1000/3600
#     time = [x*0.1 for x in range(0,100)]
#     result = [height(velocity_ms, t) for t in time]
#     return result.index(max(result))
    


# def max_ball(v0):
#     return round(v0 / 3.5316)


def max_ball(v0):
    return round(10*v0/9.81/3.6)
