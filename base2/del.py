import sys
import shutil
path = sys.argv[1]
shutil.rmtree(path)
print("删除:",path)