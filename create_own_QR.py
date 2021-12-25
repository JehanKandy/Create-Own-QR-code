import pyqrcode
from pyqrcode import QRCode

link="https://www.youtube.com/channel/UC675lo49LTHGi9SCX8XbM5g"
urls=pyqrcode.create(link)
urls.svg("jk.svg", scale=8)