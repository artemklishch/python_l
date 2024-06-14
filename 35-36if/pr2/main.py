def route_info(data):
    distance = data.get('distance')
    if distance and isinstance(distance, int):
        return F"Distance to your destination is {distance}"
    speed = data.get('speed')
    time = data.get('time')
    if speed and isinstance(speed, int) and time and isinstance(time, int):
        return f"Distance to your destination is {speed * time}"
    return "No distance info is available"
