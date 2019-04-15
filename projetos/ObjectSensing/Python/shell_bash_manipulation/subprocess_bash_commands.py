import subprocess

return_code = subprocess.check_output('ls', shell=True)
print("comandos:", return_code)
