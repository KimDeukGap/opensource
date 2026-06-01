import os
import shutil
from datetime import datetime

def organize_files(folder_path, mode="extension"):
    """
    mode = "extension" → 확장자별 정리
    mode = "date" → 생성 날짜별 정리 (YYYY-MM-DD)
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            if mode == "extension":
                # 확장자 기준
                ext = filename.split('.')[-1].lower()
                target_folder = os.path.join(folder_path, ext)
            elif mode == "date":
                # 파일 생성 날짜 기준
                timestamp = os.path.getctime(file_path)
                date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
                target_folder = os.path.join(folder_path, date_str)
            else:
                print("지원하지 않는 모드입니다.")
                return

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"{filename} → {target_folder} 로 이동 완료")

if __name__ == "__main__":
    folder = input("정리할 폴더 경로를 입력하세요: ")
    mode = input("정리 모드 선택 (extension/date): ").strip().lower()
    organize_files(folder, mode)
