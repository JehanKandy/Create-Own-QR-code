#import pyqrcode module


import pyqrcode
from pyqrcode import QRCode

#create a link for add to the you arcode  
link="https://www.youtube.com/channel/UC675lo49LTHGi9SCX8XbM5g"
urls=pyqrcode.create(link)
urls.svg("jk.svg", scale=8)
