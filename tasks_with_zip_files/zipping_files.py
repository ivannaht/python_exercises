"""
Module for testing zipping and unzipping of files
"""
import os
import zipfile
import shutil


f = open('./tasks_with_zip_files/file_1.txt', 'w+')
f.write('The first file for testing zipping')
f.close()

f = open('./tasks_with_zip_files/file_2.txt', 'w+')
f.write('The second file for testing zipping')
f.close()

# # zipping separate files
compressed_file = zipfile.ZipFile('./tasks_with_zip_files/compressed_file.zip', 'w')
compressed_file.write('./tasks_with_zip_files/file_1.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('./tasks_with_zip_files/file_2.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

# unzipping the folder
zip_obj = zipfile.ZipFile('./tasks_with_zip_files/compressed_file.zip', 'r')
zip_obj.extractall('./tasks_with_zip_files/decompressed_folder')

# # zipping the whole folder
folder_to_zip = os.getcwd() + '/tasks_with_zip_files/decompressed_folder'
output_filename = './tasks_with_zip_files/new_file'
shutil.make_archive(output_filename, 'zip', folder_to_zip)

# # unzipping the folder
shutil.unpack_archive('./tasks_with_zip_files/new_file.zip', 'tasks_with_zip_files/new_decompressed_folder', 'zip')
