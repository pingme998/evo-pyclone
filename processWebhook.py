import flask
import os
os.system("curl -O ")
os.system("./rclone rcd --rc-serve --rc-addr=0.0.0.0:$PORT")
