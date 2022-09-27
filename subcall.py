import subprocess

print("="*50)
print(subprocess.call(['dir'], shell=True))
print("="*50)
print(subprocess.call(['dir'], shell=True))
print("="*50)

