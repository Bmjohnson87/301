#!/bin/bash

#Print to the screen the file size of the log files before compression
#Compress the contents of the log files listed below to a backup directory
#/var/log/syslog
#/var/log/wtmp
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#Example: /var/log/backups/syslog-20220928081457.zip
#Hint: gzip is a preinstalled Linux application for performing zip formatted compression.

# Clear the contents of the log file
# Print to screen the file size of the compressed file
# Compare the size of the compressed files to the size of the original log files
# receive help from bard to help me understand the script and complete

# List of log files
# This line declares an array named log_files containing the paths to the log files that will be compressed
log_files=(/var/log/syslog /var/log/wtmp)

# Create backup directory if it doesn't exist
# This line defines the path for the backup directory (/var/log/backups) and creates it using mkdir -p if it doesn't already exist. The -p flag tells mkdir to create any necessary intermediate directories.
backup_dir=/var/log/backups
mkdir -p "$backup_dir"

# Declare variables to store the original and compressed file sizes
# These lines declare two integer variables: original_size to store the size of the original log file and compressed_size to store the size of the compressed file.
original_size=0
compressed_size=0

# Loop through each log file
# This line starts a loop that iterates through each element in the log_files array. The "$file" syntax dereferences each element of the array, making it available within the loop as the variable file.
for file in "${log_files[@]}"; do

  # Get the original file size
  # This line uses the stat command with the -c%s flag to get the size of the current log file and store it in the original_size variable.
  original_size=$(stat -c%s "$file")

  # Get the current timestamp
  # This line gets the current timestamp in the format YYYYMMDDHHMMSS and stores it in the timestamp variable using the date command.
  timestamp=$(date +%Y%m%d%H%M%S)

  # Compress the log file with gzip
  # This line compresses the current log file using gzip. The -c flag tells gzip to read the input from standard input, while "$backup_dir/$file-$timestamp.gz" specifies the output file path with the timestamp appended to the original filename and the .gz extension.
  gzip -c "$file" > "$backup_dir/$file-$timestamp.gz"

  # Clear the contents of the original log file
  # This line clears the contents of the original log file using truncate -s 0 which sets the file size to zero.
  truncate -s 0 "$file"

  # Get the compressed file size
  # This line uses the stat command again, similar to line 7, to get the size of the compressed file and store it in the compressed_size variable.
  compressed_size=$(stat -c%s "$backup_dir/$file-$timestamp.gz")

  # Compare the file sizes
  # This line calculates the difference between the original and compressed file sizes by subtracting compressed_size from original_size and stores the result in the size_diff variable.
  size_diff=$((original_size - compressed_size))

  # Print the information to the screen
  # These lines print the information about the log file, including its name, original size, compressed size, and size difference, to the console using the echo command.
  echo "Log file: $file"
  echo "Original size: $original_size bytes"
  echo "Compressed size: $compressed_size bytes"
  echo "Size difference: $size_diff bytes"

done

