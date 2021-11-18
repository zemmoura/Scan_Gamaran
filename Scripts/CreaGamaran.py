import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import shutil
import subprocess
import os
import sys
import logging


logging.basicConfig(filename='Log_Gamaran.log',
      format='%(asctime)s %(levelname)-8s %(message)s',
      level=logging.DEBUG,
      datefmt='%Y-%m-%d %H:%M:%S')


def img_dl(path):

	## S	et up the image URL and filename
	image_url = path
	filename = image_url.split("/")[-1]

	# Open the url image, set stream to True, this will return the stream content.
	r = requests.get(image_url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
	    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	    r.raw.decode_content = True
	    
	    # Open a local file with wb ( write binary ) permission.
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	        
	    print('Image sucessfully Downloaded: ',filename)
	    subprocess.call(["mv",filename,dir])
	else:
	    print('Image Couldn\'t be retreived')




#Recuperer le numero de chapitre a telecharger
chapitre = sys.argv[1]

dir="/home/abdelhakim/Bureau/Gamaran/chapitre/" + chapitre
subprocess.call(["mkdir", dir])

"""
print("Combien de page ?")
nbr = input()
"""
nbr = sys.argv[2]

#Recuperer l'url de la page 1 du chapitre
url = "https://www.frscan.cc/manga/gamaran/" + chapitre


#Recuperer le code source de la page
page = requests.get(url)
status = page.status_code

for i in range (0,int(nbr)):
	soup = BeautifulSoup(page.text, 'html.parser') #On démarre le parser html
	img= soup.find('img')
	print(img.length())
	for image in img:
		#pass
		print(image['src'])
		#classe = image['class']
		#source = image['alt']
		#print(classe)
		#print (image('class'))
	#src=img.get("src")
	#print(src)
	