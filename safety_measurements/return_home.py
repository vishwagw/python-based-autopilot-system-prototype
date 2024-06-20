import navigation/waypointnav.py

def return_to_home(home_location):
    navigate_to_waypoints([home_location], read_gps())

