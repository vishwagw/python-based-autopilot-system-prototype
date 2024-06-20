import serial

def read_gps():
    gps_serial = serial.Serial('/dev/ttyusBO', baudrate=9000, Timeout=1)
    while True:
        line = gps_serial.readline().decode('ascii', errors='replace')
        if '$GPAA' in line:
            data = line.split(',')
            latitude = float(data[2])
            longitude = float(data[4])

            return latitude, longitude
        