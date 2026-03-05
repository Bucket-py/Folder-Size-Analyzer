import os

def main():
    # .strip() removes accidental leading/trailing spaces that cause WinError 123
    folder = input("Enter the folder you want to scan: ").strip()
    
    if not os.path.exists(folder):
        print("Error: The specified folder does not exist.")
        return

    # 1 MB threshold (1024 * 1024)
    max_size = 1024 * 1024
    large_files = scan_folder(folder, max_size)
    
    print("\nScan complete.")
    print(f"The top 10 biggest files larger than 1MB are:")
    
    # Sort files by size (descending) and take the top 10
    large_files.sort(key=lambda x: x[1], reverse=True)
    for name, size in large_files[:10]:
        print(f"{name}: {size / (1024*1024)} MB")

def scan_folder(folder_path, max_size):
    found_files = []
    print(f"Scanning {folder_path} for files larger than {max_size} bytes...")
    
    try:
        for filename in os.listdir(folder_path):
            # Create the full path to the file
            full_path = os.path.join(folder_path, filename)
            
            # Skip if it's a directory; process if it's a file
            if os.path.isfile(full_path):
                file_size = os.path.getsize(full_path)
                if file_size > max_size:
                    found_files.append((filename, file_size))
    except PermissionError:
        print("Permission denied to access some files in this folder.")
        
    return found_files

if __name__ == "__main__":
    main()
