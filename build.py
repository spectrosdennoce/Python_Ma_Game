import PyInstaller.__main__
import os
import shutil
#compile en exe
PyInstaller.__main__.run([
	'.\main.py',
	'--onefile',
	'--icon=image/icon.ico',
	'--name=tempo of psycho',
	'--noconsole',
	'--clean'
])

#copie ressource to dist

dest = './dist/'
Repe = ["Image","sfx","Music"]
for x in Repe:
	if(os.path.exists(dest+x)):
		shutil.rmtree( dest + x)
	shutil.copytree("./"+x+"/", dest + x)
#zip to send
shutil.make_archive('Tempo_of_Psycho', 'zip', './dist')