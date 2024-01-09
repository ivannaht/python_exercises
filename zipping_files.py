"""
Module for testing zipping and unzipping of files
"""
import zipfile
import shutil


f = open('file_1.txt', 'w+')
f.write('The first file for testing zipping')
f.close()

f = open('file_2.txt', 'w+')
f.write('The second file for testing zipping')
f.close()

# zipping separate files
compressed_file = zipfile.ZipFile('compressed_file.zip', 'w')
compressed_file.write('file_1.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('file_2.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

# unzipping files
zip_obj = zipfile.ZipFile('compressed_file.zip', 'r')
zip_obj.extractall('decompressed_folder')

# zipping the whole folder
