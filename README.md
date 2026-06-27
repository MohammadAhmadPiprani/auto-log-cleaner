# Auto-log-cleaner
Python script for automatically delete the files from the folder.

# automated-log-cleaner

A lightweight, automated Python utility designed to manage disk space by continuously scanning a target log directory and purging files that exceed a specified age threshold. 

This type of utility is a critical operational tool in production environments, preventing server disk space exhaustion caused by runaway application logs.

## 🚀 How It Works

The script runs an infinite loop that acts as a lightweight background daemon:
1. **Scans** the designated log directory (`log/`) at a configurable interval.
2. **Calculates** the age of each file by comparing the current system time against the file's last modified time (`os.path.getmtime`).
3. **Purges** any file that has exceeded the maximum retention age limit.
4. **Sleeps** for a defined interval before initiating the next maintenance cycle.

## ⚙️ Configuration

You can easily customize the behavior of the script by modifying the variables at the top of the file:

```python
log_folder = "log"      # The directory to monitor
check_min = 1           # File retention threshold (in minutes)
check_int_sec = 2       # Loop sleep interval (frequency of checks in seconds)
