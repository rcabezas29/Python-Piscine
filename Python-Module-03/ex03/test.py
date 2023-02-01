from ColorFilter import ColorFilter
import sys
sys.path.append('../ex01')
from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")

cf = ColorFilter()
cf.invert(arr)
cf.to_green(arr)
cf.to_red(arr)
cf.to_blue(arr)
cf.to_celluloid(arr)
cf.to_grayscale(arr, 'm')
cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5])
