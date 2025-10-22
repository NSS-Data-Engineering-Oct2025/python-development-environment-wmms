import os

def read_file_from_folder(folder_path, filename):
    """
    Reads a text file from the specified folder and prints its content line by line.
    """
    file_path = os.path.join(folder_path, filename)
    
    # 💡 Set your breakpoint right here
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())

def main():
    print("Welcome to the Data Engineering Bootcamp!")

    folder = "C:\\Users\\Admin\\Downloads"
    filename = "requirements.txt"
    read_file_from_folder(folder, filename)

if __name__ == "__main__":
    main()
