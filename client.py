# __author__ = "taher fattahi"


# USAGE
# python client.py --server-ip SERVER_IP


# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:8888".format(args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
# vs = VideoStream(usePiCamera=True).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)
cnt=0
while True:
    # read the frame from the camera and send it to the server
    print(f'prepare image {cnt}th to {args["server_ip"]}')
    frame = vs.read()
    cnt += 1
    print(frame.shape)
    sender.send_image(rpiName, frame)
    print(f'sent image to {args["server_ip"]}')
