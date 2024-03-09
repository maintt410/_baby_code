def input_numbers(player):
    while True:
        numbers = input(f"Người chơi {player}: Nhập 4 số, nhớ thêm dấu cách giữa các số (A B C D): ").split()
        if len(numbers) == 4 and all(num.isdigit() and 1 <= int(num) <= 9 for num in numbers):
            numbers = [int(num) for num in numbers]
            if sum(numbers) == 20:
                return numbers
        print(f"Người chơi {player}, vui lòng nhập mỗi vị trí (A, B, C, D) từ 1 đến 9, sao cho tổng A B C D là 20.")


def compare_single(player1_num, player2_num):
    while True:
        player1_choose = input("Người chơi 1 chọn vị trí (A/B/C/D): ").upper()
        player2_choose = input("Người chơi 2 chọn vị trí (A/B/C/D): ").upper()
        if player1_choose in ['A', 'B', 'C', 'D'] and player2_choose in ['A', 'B', 'C', 'D']:
            index1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player1_choose]
            index2 = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player2_choose]
            if player1_num[index1] > player2_num[index2]:
                print(f"Số {player1_choose} của Người chơi 1 LỚN HƠN Số {player2_choose} của Người chơi 2")
            elif player1_num[index1] < player2_num[index2]:
                print(f"Số {player1_choose} của Người chơi 1 NHỎ HƠN Số {player2_choose} của Người chơi 2")
            else:
                print(f"Số {player1_choose} của người chơi 1 BẰNG Số {player2_choose} của Người chơi 2")
            choice = input("Chọn SINGLE để tiếp tục so sánh, chọn SUM để so sánh tổng, hoặc chọn EXIT để thoát: ").upper()
            if choice == 'SINGLE'.upper():
                continue
            elif choice == 'SUM'.upper():
                return False
            elif choice == 'EXIT'.upper():
                return True
            else:
                print("Lựa chọn không hợp lệ.")
        else:
            print("Vị trí không hợp lệ.")


def compare_sum(player1_num, player2_num):
    while True:
        player1_first_sum = input("Người chơi 1 chọn vị trí thứ nhất (A/B/C/D): ").upper()
        player1_second_sum = input("Người chơi 1 chọn vị trí thứ hai (A/B/C/D): ").upper()
        player2_first_sum = input("Người chơi 2 chọn vị trí thứ nhất (A/B/C/D): ").upper()
        player2_second_sum = input("Người chơi 2 chọn vị trí thứ hai (A/B/C/D): ").upper()
        
        if all(choice in ['A', 'B', 'C', 'D'] for choice in [player1_first_sum, player1_second_sum, player2_first_sum, player2_second_sum]):
            index1_first = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player1_first_sum]
            index1_second = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player1_second_sum]
            index2_first = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player2_first_sum]
            index2_second = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[player2_second_sum]
            
            player1_sum = player1_num[index1_first] + player1_num[index1_second]
            player2_sum = player2_num[index2_first] + player2_num[index2_second]
            
            comparison = "LỚN HƠN" if player1_sum > player2_sum else ("NHỎ HƠN" if player1_sum < player2_sum else "BẰNG")
            print(f"Tổng vị trí {player1_first_sum} + {player1_second_sum} của người chơi 1 {comparison} tổng vị trí {player2_first_sum} + {player2_second_sum} của người chơi 2")
            
            choice = input("Chọn SUM để tiếp tục so sánh tổng, chọn SINGLE để so sánh số đơn, hoặc chọn EXIT để thoát: ").upper()
            if choice == 'SUM'.upper():
                return False
            elif choice == 'SINGLE'.upper():
                return True
            elif choice == 'EXIT'.upper():
                return True
            else:
                print("Lựa chọn không hợp lệ.")
        else:
            print("Vị trí không hợp lệ.")


def main():
    print("Chương trình so sánh số của 2 người chơi!")
    player1_num = input_numbers(1)
    player2_num = input_numbers(2)
    exit_flag = False
    while not exit_flag:
        choice = input("Chọn SINGLE để so sánh số đơn, chọn SUM để so sánh tổng, hoặc chọn EXIT để thoát: ").upper()
        if choice == 'SINGLE'.upper():
            exit_flag = compare_single(player1_num, player2_num)
        elif choice == 'SUM'.upper():
            exit_flag = compare_sum(player1_num, player2_num)
        elif choice == 'EXIT'.upper():
            exit_flag = True
        else:
            print("Lựa chọn không hợp lệ.")
    print("Cảm ơn bạn đã sử dụng chương trình!")


if __name__ == "__main__":
    main()
