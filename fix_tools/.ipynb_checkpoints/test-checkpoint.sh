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
echo "success"