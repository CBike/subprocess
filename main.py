import subprocess


out = subprocess.check_output(['dir'], shell=True, universal_newlines=True)






print(out)