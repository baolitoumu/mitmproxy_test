sudo apt-get -y update
apt install -y python3-setuptools
apt install -y python-setuptools
easy_install pip
sudo apt-get -y install unzip
sudo apt-get -y upgrade
sudo apt-get -y install python3-pip
pip install --upgrade pip==9.0.3
pip3 install pip3 install selenium


sudo apt-get install -y build-essential libncursesw5-dev libreadline6-dev libssl-dev libgdbm-dev libc6-dev libsqlite3-dev tk-dev bzip2 libbz2-dev
sudo apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get -y install python-dev
y
sudo apt-get -y install python3-dev 
sudo apt-get -y install autoconf automake libtool
sudo apt-get -y install autoconf-archive
sudo apt-get -y install libpng12-dev
sudo apt-get -y install libicu-dev

sudo apt-get -y install libpango1.0-dev
sudo apt-get -y install libcairo2-dev
sudo apt-get -y install libjpeg8-dev
sudo apt-get -y install libtiff5-dev
sudo apt-get -y install zlib1g-dev
sudo apt-get -y install python-numpy
sudo apt-get -y install python3-numpy
sudo pip3 install matplotlib
sudo pip3 install pandas
pip3 install scrapy
sudo pip3 install pyocr
apt-get -y install   git libssl-dev libffi-dev 
pip3 install --upgrade pwntools
sudo apt-get -y install libtbb2 
sudo apt-get -y install libtbb-dev 

sudo apt-get -y install libpng-dev 
sudo apt-get -y install libtiff-devlibjasper-dev 
sudo apt-get -y install libdc1394-22-dev
sudo apt-get -y install libssl-dev libevent-dev libjpeg-dev libxml2-dev libxslt-dev
pip3 install netron
sudo apt-get -y update
pip install netron
sudo pip3 install virtualenv
sudo apt-get -y install install aptitude
sudo apt-get -y install libreadline-dev  

sudo apt-get -y install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
sudo pip3 install pytorch
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install libpython3-dev libpython3.5-dev python3-dev python3-setuptools python3-wheel python3.5-dev
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libatlas-base-dev gfortran
pip3 install netron
pip3 install http://download.pytorch.org/whl/cpu/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl 
pip3 install torchvision
sudo apt-get -y install python2.7-dev python3.5-dev python3.5-dev
pip3 install robobrowser
pip3 install beautifulsoup4
pip3 install lxml
pip3 install html5lib
pip3 install MechanicalSoup
sudo apt-get -y install protobuf-compiler libprotoc-dev
pip3 install onnx
wget https://github.com/git-lfs/git-lfs/releases/download/v2.3.4/git-lfs-linux-386-2.3.4.tar.gz
tar -zxvf git-lfs-linux-386-2.3.4.tar.gz
cd git-lfs-2.3.4
./install.sh
git lfs install
cd /
cd opt
git clone https://github.com/baolitoumu/jupyter.git
pip3 install jupyter
pip3 install jupyterlab
sudo apt-get -y -f install
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo -y dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -y install libxss1 libappindicator1 libindicator7
pip3 install pyvirtualdisplay
sudo apt-get -y install xvfb
jupyter notebook --generate-config

echo "[Unit]" >> /etc/systemd/system/jupyter.service
echo "Description=Jupyter Workplace" >> /etc/systemd/system/jupyter.service
echo "[Service]" >> /etc/systemd/system/jupyter.service
echo "Type=simple" >> /etc/systemd/system/jupyter.service
echo "PIDFile=/run/jupyter.pid" >> /etc/systemd/system/jupyter.service
echo "#ExecStart=/usr/local/bin/jupyter-notebook" >> /etc/systemd/system/jupyter.service
echo "#如果需要lab注释掉上面的改成" >> /etc/systemd/system/jupyter.service
path_lab=`find / -name jupyter-lab`
echo "当前lab目录位置为 $path_lab"
echo "ExecStart=$path_lab" >> /etc/systemd/system/jupyter.service
echo "WorkingDirectory=/opt/jupyter" >> /etc/systemd/system/jupyter.service
echo "Restart=always" >> /etc/systemd/system/jupyter.service
echo "RestartSec=10" >> /etc/systemd/system/jupyter.service
echo "[Install]" >> /etc/systemd/system/jupyter.service
echo "WantedBy=multi-user.target" >> /etc/systemd/system/jupyter.service



echo "from notebook.auth import passwd" >> passwd.py
echo "a = passwd()" >> passwd.py
echo "import os" >> passwd.py
echo "os.popen(\"echo \\\"c.NotebookApp.ip='*'\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py

echo "os.popen(\"echo \\\"c.NotebookApp.password = \"+\"u\"+\"'\"+a+\"'\"+\"\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py
echo "os.popen(\"echo \\\"c.NotebookApp.open_browser = False\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py
echo "os.popen(\"echo \\\"c.NotebookApp.port =81\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py
echo "os.popen(\"echo \\\"c.NotebookApp.notebook_dir ='/opt/jupyter/'\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py
echo "os.popen(\"echo \\\"c.NotebookApp.allow_root = True\\\" >> /root/.jupyter/jupyter_notebook_config.py\")" >> passwd.py

python3 passwd.py
cd /
echo "success config"

sudo systemctl enable jupyter.service
sudo systemctl daemon-reload
sudo systemctl restart jupyter.service
systemctl -a | grep jupyter

echo "当前已安装chrome版本为："
google-chrome --version
echo "正在安装chromedirver 2.38版本，与chrome v66对应："
cd /usr/bin/
wget -N https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -rf chromedriver_linux64.zip