#import pyqrcode module


import pyqrcode
from pyqrcode import QRCode

#create a link for add to the you arcode  
link="https://www.youtube.com/channel/UC675lo49LTHGi9SCX8XbM5g"

#now create the QRcode
urls=pyqrcode.create(link)

#QRcode save in image image extentions should be .svg
urls.svg("jk.svg", scale=8)
