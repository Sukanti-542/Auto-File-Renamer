import csv
import shutil
# Update the path of the current directory(where the files are present) and
# the new directory(where the reordered files should be placed)
current_directory = "PATH OF EXISTING FILES"
new_directory = "PATH OF NEW DIRECTORY"

# metadata.csv is the csv file which has the order of the new files. Files are fetched by the name of
# mentioned in the rows of the first column and files are renamed according to the position of the row
# This particular metadata has various other columns that are not used by this script and have been kept
# as an example that the csv may have multiple columns
with open('metadata.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Exclude the headers row
            line_count += 1
        else:
            # Here we use the following format to generate the new names for the audio. The names have
            # a format 001,002....010,011.....099,100 etc. The file format here is wav, feel free to add
            # your own extension
            if line_count < 10:
                shutil.copy(current_directory + '/' + row[0], new_directory + '/00' + str(line_count) + '.wav')
            elif line_count < 100:
                shutil.copy(current_directory + '/' + row[0], new_directory + '/0' + str(line_count) + '.wav')
            else:
                shutil.copy(current_directory + '/' + row[0], new_directory + '/' + str(line_count) + '.wav')
                line_count += 1