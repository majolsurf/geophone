import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as numps

# Max Nyquist Frequency is about 800Hz

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

samples = 256 
channel = 0
det_thresh = 2500

sig_v = [0 for i in range(samples)]


while True:
  for i in range(len(sig_v)):
      sig_v[i] = mcp.read_adc(channel)
      time.sleep(0.005)
  dft_sig_v = numps.fft.fft(sig_v)
  abs_dft = abs(dft_sig_v[2:])

  max_index = 0
  max_value = det_thresh-1 
  for i in range(len(abs_dft)):
      if abs_dft[i] > det_thresh:
	if abs_dft[i] > max_value:
		max_index = i
		max_value = abs_dft[i]
  if max_index > 0:
	ts = time.ctime()
	print('Event detected', ts, max_index, max_value)
	file = open("geograph.txt", "a+")
	file.write(str(ts)+", "+str(sig_v)+"\n")
	file.close()


