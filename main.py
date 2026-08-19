from BuildTheLeaderboard import func1
from ExploreTheKingdom import func4
from FindTheFastestRoute import func3
from MonsterBattle import func5
from TreasureScanner import func2


def show_banner():
    print("=" * 40)
    print("BridgeLabz Python Missions")
    print("=" * 40)


def show_menu():
    print("\nChoose a mission:")
    print("1. Build The Leaderboard")
    print("2. Treasure Scanner")
    print("3. Find The Fastest Route")
    print("4. Explore The Kingdom")
    print("5. Monster Battle")
    print("6. Run All Missions")
    print("0. Exit")


def run_all_missions():
    print("\nMission 1: Build The Leaderboard")
    func1("3")

    print("\nMission 2: Treasure Scanner")
    func2()

    print("\nMission 3: Find The Fastest Route")
    func3()

    print("\nMission 4: Explore The Kingdom")
    func4()

    print("\nMission 5: Monster Battle")
    func5()


def main():
    show_banner()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "0":
            print("\nNice Play, Bye Bye!")
            break
        elif choice == "1":
            func1()
        elif choice == "2":
            func2()
        elif choice == "3":
            func3()
        elif choice == "4":
            func4()
        elif choice == "5":
            func5()
        elif choice == "6":
            run_all_missions()
        else:
            print("Wrong Choice! Choose Again.")


if __name__ == "__main__":
    main()
