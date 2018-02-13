# open file
# open(name[.mode[.buffering]])

# 'r' - read
# 'w' - write
# 'a' - add
# 'b' - binary could be added to another modes
# '+' - read/write could be added to another modes

# buffer - > 1 -- buffering size
#          < 0 -- default size

# -------------------------- Files and Paths -------------------------- #
# |   os.getcwd()    | Current path
# | os.listdir(path) | Return all files and folders under path
# | os.remove(path)  | Remove file
# | os.removedirs(path) | Remove a vacant folder
# | os.path.isfile(path) | Check is a file or not
# | os.path.isdir(path) | Check is a dir or not
# | os.path.isabs(path) | Check is an absolute directory or not
# | os.path.exists(path)| Check if dir exists
# | os.path.split(path) | Split a path, return a tuple
# | os.path.splitext(path) | Split expanded name
# | os.path.dirname(path) | Get dir name
# | os.path.basename(path) | Get file name
# | os.getenv() os.putenv() | Get and set environmental variable
# | os.linesep | Return line separator, Windows - '\r\n', Linux/Unix -
#              | '\n', Mac - '\r'
# | os.name | Current platform, Windows - 'nt', Linux/Unix - 'posix'
# | os.rename(old, new) | Rename a file or dir
# | os.makedirs(path) | Create multi-level path
# | os.makedir(name) | Create single level path
# | os.stat(file) | Status of file
# | os.chmod(file) | Change permission and time stamp
# | os.path.getsize(filename) | Get file size
# | shutil.copytree("olddir", "newdir") | Copy folder, newdir must do not exist
# | shutil.copyfile("oldfile", "newfile") | Copy file, newfile and oldfile must be file
# | shutil.copy("oldfile", "newfile") | Copy file, oldfile must be file, newfile could be a path
# | shutil.move("oldpos", "newpos") | Move file
# | os.rmdir("dir") | Delete vacant path
# | os.rmtree("dir") | Delete dir, could have content
# --------------------------------- END ------------------------------- #


import pickle

d = dict(url="index.html", title="First Page", content="First page")
f = open(r"/Users/robinxyuan/Documents/dump.txt", "wb")
pickle.dump(d, f)
f.close()

f = open(r"/Users/robinxyuan/Documents/dump.txt", "rb")
d = pickle.load(f)
f.close()
print(d)



