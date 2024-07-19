import os
from os.path import splitext, exists, join
import shutil


source_dir = "/Users/amr/Downloads"
dest_dir_media = '/Users/amr/Downloads/DownloadedMedia'
dest_dir_docs = '/Users/amr/Downloads/DownloadedDocuments'
dest_dir_apps = '/Users/amr/Downloads/DownloadedApps'
dest_dir_others = '/Users/amr/Downloads/others'
dest_dir_code = '/Users/amr/Downloads/DownloadedCode'

# We create the directories to prevent any possible error
def createDirectories():
	dir1 = "DownloadedMedia"
	dir2 = "DownloadedDocuments"
	dir3 = "DownloadedApps"
	dir4 = "others"
	dir5 = "DownloadedCode"
	dirs = [dir1, dir2, dir3, dir4, dir5]

	for d in dirs:
		path = os.path.join(source_dir, d) 
		# If the directory does not exist we create it. Otherwise we just continue
		try:
			os.mkdir(path) 
			print(f'{d} has been created')
		except FileExistsError:
			pass

def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # If the file exists, we add a number to make it unique
    dest_path = os.path.join(dest, name) 
    while exists(dest_path):
        name = f"{filename}({str(counter)}){extension}"
        dest_path = os.path.join(dest, name) 
        counter += 1
    return name


# With this function we move the files to the new location and get a new name for files with the same name
def moveFile(dest, entry, name):
	dest_path = os.path.join(dest, name)
	if exists(dest_path):
		unique_name = makeUnique(dest, name)
		old_name = join(dest, name)
		new_name = join(dest, unique_name)
		os.rename(old_name, new_name)
	shutil.move(entry, dest)


# We verify if the file is a media file
def mediaExtension(name):
	media = ['.wav', '.mp3', '.acc', '.wma', '.flac', '.m4a', '.webm', '.mpg', '.mp2', '.mpeg', 
		'.mpv', '.ogg', '.m4v', '.avi', '.wmv', '.mp4v', '.mp4', '.mov', '.jpg', '.jpeg', '.png', 
		'.webp', '.heic', '.qt', '.flv', '.swf', '.avchd', 'jpe', '.jif', ".jfif", ".jfi", ".png", 
		".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", 
		".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", 
		".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
	for ext in media:
		if name.lower().endswith(ext):
			return True
	return False

# We verify if the file is a code file
def codeExtension(name):
	code = ['.py', '.c', '.cpp', '.java', '.js', '.go', '.nb']
	for ext in code:
		if name.lower().endswith(ext):
			return True
	return False

# We verify if the file is a document
def docsExtension(name):
	docs = ['.txt', '.tex', '.pdf', '.css', '.sql', '.xlsx', '.xls', '.ppt', '.pptx', '.doc', '.docx', '.odt']
	for ext in docs:
		if name.lower().endswith(ext):
			return True
	return False

# We verify if the file is an app
def AppsExtension(name):
	apps = ['.iso', '.app', '.dmg', '.pkg']
	for ext in apps:
		if name.lower().endswith(ext):
			return True
	return False	

# We organize the files
def organizeFiles():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			name = entry.name
			dest = source_dir
			# Depending on the extension we move the file to the desired location
			if mediaExtension(name):
				dest = dest_dir_media
				moveFile(dest, entry, name)
			elif codeExtension(name):
				dest = dest_dir_code
				moveFile(dest, entry, name)
			elif docsExtension(name):
				dest = dest_dir_docs
				moveFile(dest, entry, name)
			elif AppsExtension(name):
				dest = dest_dir_apps
				moveFile(dest, entry, name)
			# else:
			# 	dest = dest_dir_others
			# 	moveFile(dest, entry, name)

if __name__ == "__main__":
	createDirectories()
	organizeFiles()

