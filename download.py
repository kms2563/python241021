import os
import shutil #move 함수

# 다운로드 폴더 경로
DOWNLOADS_FOLDER = r"c:\Users\student\Downloads"

# 이동할 폴더 설정
TARGET_FOLDERS = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "data": [".csv", ".xlsx", ".xls"],
    "docs": [".txt", ".doc", ".pdf"],
    "archive": [".zip", ".rar", ".tar", ".gz", ".bz2"]
}

# 각 폴더의 경로 설정
def get_target_folder(base_folder, sub_folder):
    return os.path.join(base_folder, sub_folder)

# 폴더 생성 함수
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동 함수
def move_files():
    for folder, extensions in TARGET_FOLDERS.items():
        target_folder = get_target_folder(DOWNLOADS_FOLDER, folder)
        create_folder_if_not_exists(target_folder)
        
        for file_name in os.listdir(DOWNLOADS_FOLDER):
            file_path = os.path.join(DOWNLOADS_FOLDER, file_name)
            if os.path.isfile(file_path) and file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, target_folder)
                print(f"Moved {file_name} to {target_folder}")

if __name__ == "__main__":
    move_files()