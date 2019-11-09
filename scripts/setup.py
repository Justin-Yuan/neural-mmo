from pdb import set_trace as T
import os

#Install python requirements
print('Installing requirements')
os.system('pip install -r scripts/requirements.txt')

# my fixes
os.system('pip install imageio')
os.system('pip install pygame')
os.system('pip install psutil')
# if it's mac, link to another file, run with `open client`
import sys 
if "darwin" in sys.platform:    
    os.system('ln -fs $(pwd)/forge/embyr/UnityClient/neural-mmo-mac.app client')


#Download the Unity client
print('Downloading Embyr client')
os.chdir('forge')
os.system('git clone https://github.com/jsuarez5341/neural-mmo-client')
os.system('mv -n neural-mmo-client embyr')
os.chdir('..')

#Build game maps
print('Building game maps')
import terrain
