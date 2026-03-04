import os 

folder=""

def main():
    scan_folder(1024 * 1024)  # 1 MB
    print("Scan complete.")
    print(f"The 10 biggest files in the folder are: {scan_folder.__doc__}")

def set_folder_to_scan(folder_path):
    """Sets the folder to scan for large files."""
    if os.path.isdir(folder_path):
        os.chdir(folder_path)
        print("Folder set to: {}".format(folder_path))
    else:
        print("Invalid folder: {}".format(folder_path))

def scan_folder(max_size):
    print("Scanning folder for files larger than {} bytes...".format(max_size))
    set_folder_to_scan()
    
        
if __name__ == "__main__":
    main()
    