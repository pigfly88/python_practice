import subprocess


r = subprocess.call(['php', '-r echo 666;'])
r = subprocess.call(['cd'])
print('Exit code:', r)