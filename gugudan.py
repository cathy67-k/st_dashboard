def print_gugudan():
    """2단부터 9단까지 구구단을 출력하는 함수"""
    for i in range(2, 10):
        print(f"--- {i}단 ---")
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()

if __name__ == "__main__":
    # 구구단 출력 시작
    print_gugudan()
