# https://pythonspot.com/python-subprocess/

import subprocess


subprocess.call(["ls", "-l"])

print("=============================")

process = subprocess.Popen(['cat', 'teste.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout)

print("=============================")

s = subprocess.check_output(["echo", "Hello World!"])
print("s = ", s)