Type the following commands:
 
cd /home
 
sudo apt-get install python-dev
 
sudo wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.5.5.tar.gz
 
sudo gunzip RPi.GPIO-0.5.5.tar.gz

sudo tar -xvf RPi.GPIO-0.5.5.tar
 
cd RPi.GPIO-0.5.5

sudo python setup.py install
