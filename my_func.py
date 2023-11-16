def my_func(toponym):
    size = toponym['boundedBy']['Envelope']
    lower_corner = ",".join(size['lowerCorner'].split())
    upper_corner = ",".join(size['upperCorner'].split())
    return lower_corner, upper_corner