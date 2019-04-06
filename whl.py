import pip
from pip._internal import main as pipmain

def install_whl(path):
    pipmain(['install', path])

install_whl('C:\prog\Pillow_SIMD-5.3.0.post0-cp37-cp37m-win32.whl')