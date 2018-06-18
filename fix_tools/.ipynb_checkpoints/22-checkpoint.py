from notebook.auth import passwd
a = passwd()
import os
os.popen("echo \"c.NotebookApp.ip='*'\" >> /root/.jupyter/jupyter_notebook_config.py")
os.popen("echo \"c.NotebookApp.password = "+"u"+"'"+a+"'"+"\" >> /root/.jupyter/jupyter_notebook_config.py")
os.popen("echo \"c.NotebookApp.open_browser = False\" >> /root/.jupyter/jupyter_notebook_config.py")
os.popen("echo \"c.NotebookApp.port =81\" >> /root/.jupyter/jupyter_notebook_config.py")
os.popen("echo \"c.NotebookApp.notebook_dir ='/opt/jupyter/'\" >> /root/.jupyter/jupyter_notebook_config.py")
os.popen("echo \"c.NotebookApp.allow_root = True\" >> /root/.jupyter/jupyter_notebook_config.py")


