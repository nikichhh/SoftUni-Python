import pyqrcode
import png
from pyqrcode import QRcode
address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11666606901054856&slink=q4wy5x'
url = pyqrcode.create(address)
url.png('car.png', scale=8)