import time

def pomodoro(work_minutes=25, break_minutes=5, cycles=4):
    """
    Pomodoro 타이머
    - work_minutes: 집중 시간 (기본 25분)
    - break_minutes: 휴식 시간 (기본 5분)
    - cycles: 반복 횟수 (기본 4회)
    """
    for cycle in range(1, cycles + 1):
        print(f"{cycle}번째 집중 시작! {work_minutes}분 동안 집중하세요.")
        time.sleep(work_minutes * 60)

        print(f"휴식 시간! {break_minutes}분 동안 쉬세요.")
        time.sleep(break_minutes * 60)

    print("모든 Pomodoro 세션이 끝났습니다! 수고하셨습니다.")

if __name__ == "__main__":
    print("Pomodoro 타이머를 시작합니다.")
    work = int(input("집중 시간(분): ") or 25)
    rest = int(input("휴식 시간(분): ") or 5)
    cycles = int(input("반복 횟수: ") or 4)

    pomodoro(work, rest, cycles)
