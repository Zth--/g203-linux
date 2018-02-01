import usb.core
import usb.util

# find the device
dev = usb.core.find(idVendor=0x046d, idProduct=0xc084)

# detach the kernel driver
dev.detach_kernel_driver(1)
usb.util.claim_interface(dev,1)
dev.set_interface_altsetting(interface=1,alternate_setting=0)

# set a hardcoded colour
colors = [0x00, 0x00, 0x00]

# concatenate the colours into the expected 8 bytes
data = [0x11, 0xff, 0x0e, 0x3c, 0x00, 0x01] + colors + [0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# send the data to the mouse
dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09, wValue=0x0211, wIndex=0x0001, data_or_wLength=data,timeout=1000)

# reclaim the device
usb.util.release_interface(dev,1)
dev.attach_kernel_driver(1)
