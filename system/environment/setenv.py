import os

print('setenv...', end='')
print(os.environ['USER'])

os.environ['USER'] = 'Brian'

os.chdir('system/environment')
os.system('python echoenv.py')

os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USER'] = input('?')
print(os.popen('python echoenv.py').read())
