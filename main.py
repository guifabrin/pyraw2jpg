import rawpy
import imageio
from os import listdir, mkdir
from os.path import isfile, join
from pathlib import Path
from tkinter import filedialog
from tkinter import *


def raw_to_jpg(origin_path, destination_path):
    print("Converting", origin_path, "to", destination_path + ".jpg")
    raw = rawpy.imread(origin_path)
    rgb = raw.postprocess()
    imageio.imsave(destination_path + ".jpg", rgb)


root = Tk()
root.withdraw()

selected_path = filedialog.askdirectory()
sub_path_result = "/resolved/"
print("Init at", selected_path)
files = [f for f in listdir(selected_path) if isfile(join(selected_path, f))]

try:
    print("Creating path", selected_path + sub_path_result)
    mkdir(selected_path + sub_path_result)
except:
    pass

for filename in files:
    try:
        complete_path = selected_path + "/" + filename
        my_path = Path(complete_path)
        if my_path.suffix in (
                '.cr2', '.nef', '.raw', '.dng', '.arw', '.dcr', '.orf', '.rw2', '.pef',
                '.CR2', '.NEF', '.RAW', '.DNG', '.ARW', '.DCR', '.ORF', '.RW2', '.PEF'
        ):
            raw_to_jpg(complete_path, selected_path + sub_path_result + my_path.stem)
    except:
        pass
