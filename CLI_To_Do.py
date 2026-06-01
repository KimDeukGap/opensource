import sys

tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 종료")

def add_task():
    task = input("추가할 할 일을 입력하세요: ")
    tasks.append(task)
    print(f"'{task}' 추가 완료!")

def list_tasks():
    if not tasks:
        print("할 일이 없습니다.")
    else:
        print("\n현재 할 일 목록:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    list_tasks()
    try:
        idx = int(input("삭제할 번호를 입력하세요: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"'{removed}' 삭제 완료!")
        else:
            print("잘못된 번호입니다.")
    except ValueError:
        print("숫자를 입력하세요.")

def main():
    while True:
        show_menu()
        choice = input("선택: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("프로그램을 종료합니다.")
            sys.exit()
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
