import asyncio
import os
from datetime import datetime
import exifread
import dronekit
import time

from picamera2 import Picamera2

# Define the target folder for geotagged images
TARGET_FOLDER = "/home/pi/Desktop/images/"

#1 Initialize PiCamera
picam2 = Picamera2()
#Create a new object, camera_config and use it to set the still image resolution (main) to 1920 x 1080. and a “lowres” image with a size of 640 x 480. This lowres image is used as the preview image when framing a shot.
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
#Load the configuration.
picam2.configure(camera_config)

#2 Connect to the drone and wait for GPS fix
print("Connecting to vehicle...")
vehicle = dronekit.connect('/dev/ttyAMA0', baud=57600)
print("Waiting for GPS fix...")
while not vehicle.gps_0.fix_type:
    pass
print("GPS fix obtained.")

# Define the capture_photo function
async def capture_photo():
    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
    temp_file = "/run/shm/{}".format(filename) # Use the ramdisk for faster I/O
    picam2.start()
    #Pause the code for two seconds.
    time.sleep(1)
    #Capture an image and save it as test.jpg.
    picam2.capture_file(temp_file)
    return temp_file

# Define the get_gps_data function
async def get_gps_data():
    #return (vehicle.location.global_frame.lat,
     #       vehicle.location.global_frame.lon,
     #       vehicle.location.global_frame.alt)
     return(39.668756, -127.334674, 10)

# Define the geotag function
async def geotag(temp_file, gps_data):
    # gps_data should be a tuple containing latitude, longitude, and altitude
    latitude, longitude, altitude = gps_data
    
    # Construct the ExifTool command
    exiftool_cmd = ['exiftool', '-GPSLatitude={}'.format(latitude), '-GPSLongitude={}'.format(longitude), '-GPSAltitude={}'.format(altitude), temp_file]
    
    # Run the ExifTool command using subprocess
    try:
        subprocess.run(exiftool_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("Error geotagging photo: ", e)
        return False
    
    return True

# Define the main function
async def main():
    while True:
        # Wait for 5 seconds
        # Capture photo and get GPS data asynchronously
        temp_file_task = asyncio.create_task(capture_photo())
        gps_data_task = asyncio.create_task(get_gps_data())
        # Wait for both tasks to complete
        temp_file = await temp_file_task
        gps_data = await gps_data_task
        # Geotag the image asynchronously
        await geotag(temp_file, gps_data)

# Run the main function
asyncio.run(main())
