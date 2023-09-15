wget https://www.python.org/ftp/python/3.11.5/Python-3.11.5.tgz

tar -zxvf Python-3.11.5.tgz
cd Python-3.11.5
./configure --enable-optimizations

sudo make altinstall