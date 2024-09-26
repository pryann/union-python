from os import mkdir, path, rename, rmdir

dir_path = path.join(path.dirname(__file__), "new_dir")
# mkdir(dir_path)

# rename and move too
# rename(dir_path, path.join(path.dirname(__file__), "files", "new_dir2"))
rmdir(path.join(path.dirname(__file__), "files", "new_dir2"))
# shutils: copytree, rmtree, move
