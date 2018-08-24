Type the following commands:
cd /home
sudo apt-get install python-dev git && sudo wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.5.tar.gz && sudo gunzip RPi.GPIO-0.5.5.tar.gz && sudo tar -xvf RPi.GPIO-0.5.5.tar && cd RPi.GPIO-0.5.5 && sudo python setup.py install
======
cd /home
sudo wget https://github.com/mrboog12/Python-Nonsense/blob/master/addcredit.py && sudo wget https://github.com/mrboog12/Python-Nonsense/blob/master/buttontrigger.py
======
cd /home
sudo apt-get update && sudo apt-get install python-mosquitto mosquitto python-pip -y && sudo pip install paho-mqtt && sudo apt-get install build-essential python quilt devscripts python-setuptools python3 libssl-dev cmake libc-ares-dev uuid-dev daemon libwebsockets-dev apache2 -y 
======
cd /home/pi
wget http://mosquitto.org/files/source/mosquitto-1.4.2.tar.gz && tar zxvf mosquitto-1.4.2.tar.gz && cd mosquitto-1.4.2 && sudo nano config.mk
======
Change the line to say: "WITH_WEBSOCKETS:=yes"
======
sudo make && sudo make install && sudo cp mosquitto.conf /etc/mosquitto && sudo nano /etc/mosquitto/mosquitto.conf
======
Add in under "General Configuration"
port 1883
listener 9001
protocol websockets
======
./src/mosquitto -c /etc/mosquitto/mosquitto.conf -d
======
ps ax

========
Installing web server

Earlier you stalled the Apache web server as part of all the software you loaded at the beginning of this tutorial. Now you will copy the HTML files into the web server home directory.

Download the software from our website as follows:

cd /home/pi
mkdir onoff
cd onoff
sudo wget www.privateeyepi.com/downloads/onoff.zip
sudo unzip onoff.zip -d /var/www/html
sudo mv /var/www/html/onoff.py ./

Now configure the website to point towards your Raspberry Pi IP Address. If you do not know the IP Address of your Raspberry PI type:

ifconfig

Near the bottom you will see the ip address as shown below (192.168.2.19 in my case):

wlan0     Link encap:Ethernet  HWaddr b8:27:eb:d7:82:72

inet addr:192.168.2.19  Bcast:192.168.2.255  Mask:255.255.255.0

Now edit the website config file with this address:

sudo nano /var/www/html/config.js

Change the host ip address to your address (I've configured my address of 192.168.2.19):

 host = '192.168.2.19'; // hostname or IP address

Then press ctrl-x followed by "y" and ENTER to save.

Edit onoff.py to configure the GPIO pin you are using. It is set to pin number 7 by default, but if you are pin number 12 then change the 7's to 12 as shown here:

sudo nano onoff.py

....
def on():
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, 1)

def off():
        GPIO.setup(12, GPIO.IN)
....

Press ctrl-X followed by y to save and exit.

Now run the Python application that will switch the GPIO on/Off:

sudo nohup python /home/pi/onoff/onoff.py &


The application will run in the background on your Raspberry Pi so you can log off and it continues to run.
