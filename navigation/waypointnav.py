def navigate_to_waypoints(waypoints, current_location):
    for waypoint in waypoints:
        while not at_waypoint(current_location, waypoint):
            control_signals = compute_control_signals(current_location, waypoint)
            send_control_signals(control_signals)
            current_location = read_gps()  # Update location
            time.sleep(0.1)
        
def at_waypoint(current, target, tolerance=0.0001):
    return abs(current[0] - target[0]) < tolerance and abs(current[1] - target[1]) < tolerance
