import math

def sin(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1 # insertt here one coordinate i.e point of pada release
    lat2, lon2 = coord2    # insertt here one coordinate i.e point of circle seen thro fpv system of pa/pada

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#radions of coordinates done conversion complete
c1 = 19.044783, 72.819797  #our college
c2= 19.044890, 72.819260# mount mary church bandra east
print(str(round(sin(c1, c2)))+ ' meters')