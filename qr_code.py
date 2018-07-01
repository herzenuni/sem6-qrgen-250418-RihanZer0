import pyqrcode
qr_code = pyqrcode.create('https://vk.com/rihan_zer0')
qr_code.svg('qr_code.svg', scale=7, module_color='red',  background='black')
qr_code.eps('qr_code.eps', scale=3)

print(qr_code.terminal(quiet_zone=1))
