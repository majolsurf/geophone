import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import matplotlib.pyplot as plt
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

sig_v = [0 for i in range(samples)]

plt.ion()

while True:
  for i in range(len(sig_v)):
      sig_v[i] = mcp.read_adc(channel)
  dft_sig_v = numps.fft.fft(sig_v)

  plt.plot(abs(dft_sig_v[2:]))
  #plt.plot(sig_v)
  plt.show()
  plt.pause(0.01)
  plt.clf()




#print(sig_v)

#plt.plot(sig_v)
#plt.show()

#plt.plot(abs(dft_sig_v))
#plt.show()


