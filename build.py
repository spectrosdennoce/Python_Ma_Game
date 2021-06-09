import PyInstaller.__main__
import os
import shutil
#compile en exe
pyinstaller.__main__.run([
	'.\main.py',
	'--onefile',
	'--icon=image/icon.ico',
	'--name=tempo of psycho',
	'--noconsole',
	'--clean'
])

#copie ressource to dist
srcImage = './Image'
srcsfx = './sfx'
srcMusic = './Music'
dest = './dist/'
shutil.copytree(srcImage, dest + "Image") 
shutil.copytree(srcsfx, dest + "sfx")
shutil.copytree(srcMusic, dest + "Music")
#zip to send
shutil.make_archive('Tempo_of_Psycho', 'zip', './dist')