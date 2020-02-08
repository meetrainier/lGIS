from laspy.file import File
#import numpy as np

inFile = File('simple.las', mode='r')
print("inFile type",type(inFile))
I = inFile.Classification == 2
##
pts = inFile.get_points()
print("points type",type(pts))
print("points shape",pts.shape)

intensity = inFile.get_intensity()
print("intensity points shape",intensity.shape)

flag_byte = inFile.get_flag_byte()
print("flag_byte shape",flag_byte.shape)

ret_num = inFile.get_return_num()
print("ret_num shape",ret_num.shape)
print(ret_num[0])

num_returns = inFile.get_num_returns()
print("num_returns shape",num_returns.shape)
print(num_returns[0])

get_scan_dir_flag()

get_edge_flight_line()

get_raw_classification()

get_classification()

get_scanner_channel()

get_synthetic()

get_key_point()

get_withheld()

get_overlap()

get_scan_angle_rank()

get_scan_angle()
get_user_data()
get_pt_src_id()
get_red()
get_green()
get_blue()
get_wave_packet_desc_index()
get_nir()

outFile = File('output.las', mode='w', header=inFile.header)
print("outFile type",type(outFile))
outFile.points = inFile.points[I]
outFile.close()