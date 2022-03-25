import sys
import os

src_dir = sys.argv[1]
output_name = sys.argv[2]

#get files in src_dir
file_names = os.listdir(src_dir)

#Open output file
with open(output_name, 'w') as outfile: 

  #open each file in the directory
  for file_name in file_names:
    with open(src_dir + file_name, 'r') as infile:
      outfile.write(infile.read())
    outfile.write("\n")

