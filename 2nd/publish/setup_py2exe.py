from distutils.core import setup
import py2exe

#setup(console=["stepMotionDrawing.py"])

includes = ["encodings", "encodings.*"]

options = {"py2exe":
            {"compressed": 1,
             "optimize": 2,
             "ascii": 1,
             "includes":includes,
             "bundle_files": 1
            }}
setup(
    options=options,
    zipfile=None,
    console=[{"script": "test.py", "icon_resources": [(1, "16.ico")]}],
    windows=[{"script": "test.py", "icon_resources": [(1, "16.ico")]}],
    #windows=['test.py'],
    version = "2016.5.5",
    description = "this is a py2exe test",
    name = "stepMotionDrawing",
)
