import sys
import tempfile
import zipfile
import shutil
import subprocess
import os
import argparse
import uuid

def createInitFileIfDoesntExist(directory):
    initFilePath = os.path.join(directory, "__init__.py")
    if not os.path.isfile(initFilePath):
        open(initFilePath, 'a').close()

def pylintZipFile(path, verifyPath, globalPath=[]):
    tempDir = tempfile.mkdtemp(dir="/tmp", prefix="pylinttempdir")
    pythonPath = ":".join(["."] + globalPath + sys.path)
    try:
        createInitFileIfDoesntExist(tempDir)
        with zipfile.ZipFile(path, "r") as z:
            z.extractall(tempDir)
        rcFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pylint.rc")
        shutil.copyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "ignorestuffplugin.py"),
                        os.path.join(tempDir, "ignorestuffplugin.py"))
        subprocess.Popen(["pylint", "--rcfile", rcFilePath, verifyPath], env={"PYTHONPATH": pythonPath}, cwd=tempDir).wait()
    finally:
        shutil.rmtree(tempDir)

def pylintFile(path, globalPath=[]):
    assert os.path.isfile(path)
    tempDir = tempfile.mkdtemp(dir="/tmp", prefix="pylinttempegg")
    try:
        eggPath = os.path.join(tempDir, str(uuid.uuid4()))
        os.system( "STRATO_CONF_DIRECTORY=/etc/stratoscale UPSETO_JOIN_PYTHON_NAMESPACES=yes PYTHONPATH=py python -m upseto.packegg --entryPoint=%(path)s --output=%(eggPath)s --createDeps=%(eggPath)s.deps --compile_pyc --joinPythonNamespaces" % dict(path=path, eggPath=eggPath))
        if path.startswith("py/"):
            path = path[3:]
        pylintZipFile(eggPath, path, globalPath)
    finally:
        shutil.rmtree(tempDir)

def pylintDirectory(directory, globalPath=[]):
    assert os.path.isdir(directory)
    allFilesInDir = [ os.path.splitext(f)[0] for root, dirs, files in os.walk(directory) for f in files if os.path.splitext(f)[1] == ".py" ]
    tempDir = tempfile.mkdtemp(dir="/tmp", prefix="pylinttempegg")
    try:
        eggPath = os.path.join(tempDir, str(uuid.uuid4())) + '.egg'
        os.system( "STRATO_CONF_DIRECTORY=/etc/stratoscale UPSETO_JOIN_PYTHON_NAMESPACES=yes PYTHONPATH=py python -m upseto.packegg --directory=%(directory)s --output=%(eggPath)s --createDeps=%(eggPath)s.deps --compile_pyc --joinPythonNamespaces" % dict(directory=directory, eggPath=eggPath))
        initFilePath = '%(directory)s/__init__.py' % dict( directory = directory )
        if not os.path.isfile( initFilePath ):
            try:
                with open( initFilePath, 'w' ) as fd:
                    fd.write('')
                os.system( "zip %(eggPath)s %(initFilePath)s" % dict( eggPath = eggPath, initFilePath = initFilePath ) )
            finally:
                try:
                    os.remove( initFilePath )
                except:
                    pass
        pylintZipFile(eggPath, directory, globalPath)
    finally:
        shutil.rmtree(tempDir)

parser = argparse.ArgumentParser(description='pylint zipped files or single python files')
parser.add_argument('--zip', dest="zipfiles", default=[], action='append', help='zip file with source:relative package path to verify inside zip file (e.g. strato)')
parser.add_argument('--file', dest="files", default=[], action='append', help='file to pylint')
parser.add_argument('--dir', dest="dirs", default=[], action='append', help='directory to pylint python files in dir (recursive)')
parser.add_argument('--globalpath', default=[], action='append', help='path to add to PYTHONPATH to simulate site packages.')
args = parser.parse_args()


for directory in args.dirs:
    pylintDirectory(directory, globalPath=args.globalpath)

for filePath in args.files:
    pylintFile(filePath, globalPath=args.globalpath)

for zipFileAndPackagePath in args.zipfiles:
    filePath, packagePath = zipFileAndPackagePath.split(':')
    pylintZipFile(filePath, packagePath, globalPath=args.globalpath)
