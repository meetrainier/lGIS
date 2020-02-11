import numpy as np
import laspy
from laspy.file import File
#import numpy as np
#file_name='simple.las'
file_name='points.las'
inFile = File(file_name, mode='r')
print("inFile type",type(inFile))
I = inFile.Classification == 2
##
h = inFile.header
print("Version=",h.major_version,".",h.minor_version)
##
pts = inFile.get_points()
print("points type",type(pts))
print("points shape",pts.shape)

intensity = inFile.get_intensity()
print("intensity points shape",intensity.shape)

flag_byte = inFile.get_flag_byte()
print("flag_byte shape",flag_byte.shape)

pt_ret_count = inFile.point_return_count()
print("type of point return count", type(pt_ret_count))

ret_num = inFile.get_return_num()
print("ret_num shape",ret_num.shape)
print("ret_num shape 100",ret_num[100].shape)
print("First returned number",ret_num[0],"\n")
print("First returned number",ret_num[0],"\n")
unique_elements, counts_elements = np.unique(ret_num, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)),"\n")

num_returns = inFile.get_num_returns()
print("num_returns shape",num_returns.shape)

print("First number of returns:",num_returns[0])
unique_elements, counts_elements = np.unique(num_returns, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))

src_ids = inFile.get_pt_src_id()
print("First number of returns:",num_returns[0])
unique_elements, counts_elements = np.unique(src_ids, return_counts=True)
print("Frequency of", "source ids", "of the said array:")
print(np.asarray((unique_elements, counts_elements)))

#get_scan_dir_flag()

flight_lines = inFile.get_edge_flight_line()

raw_classes = inFile.get_raw_classification()

classes = inFile.get_classification()

#scanner_channel = inFile.get_scanner_channel()

synthetics = inFile.get_synthetic()

key_points = inFile.get_key_point()

withehelds_points = inFile.get_withheld()

try:
	overlap = inFile.get_overlap()
except laspy.util.LaspyException as err:
	print("Overlap error: {0}".format(err))
	#print(format(err))

angle_rank = inFile.get_scan_angle_rank()

try:
	scan_angle = inFile.get_scan_angle()
except laspy.util.LaspyException as err:
	print("\nScan angle error: {0}".format(err))
	
user_data = inFile.get_user_data()

try:
	reds = inFile.get_red()
	greens = inFile.get_green()
	blues = inFile.get_blue()
except laspy.util.LaspyException as err:
	print("\nColor: {0}".format(err))
#wv_desc_indices = inFile.get_wave_packet_desc_index()
#inFile.get_nir()

outFile = File('output.las', mode='w', header=inFile.header)
print("outFile type",type(outFile))
outFile.points = inFile.points[I]
outFile.close()