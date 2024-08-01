import math
def video_part(part, total):
    prt = part.split(":")
    ttl = total.split(":")
    hour_p = int(prt[0])*3600
    hour_t = int(ttl[0])*3600
    minute_p = int(prt[1])*60
    minute_t = int(ttl[1])*60
    second_p = int(prt[2])
    second_t = int(ttl[2])
    t = (hour_t+minute_t+second_t)
    p = (hour_p+minute_p+second_p)
    gcd = math.gcd(p, t)
    return [p/gcd, t/gcd]