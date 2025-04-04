import os.path

from package.game import shop
from package.models import Player
from package.utils import load_game, save_game


def main():
    print("턴제 RPG 게임")
    if os.path.exists("save.json"):
        choice = input("1. 기존 캐릭터 불러오기 \n2. 새로 시작하기 \n 선택:")
        if choice == "1":
            player = load_game()# 1번 세이브 파일 불러옴
            if not player:
                print("저장된 캐릭터가 없습니다.") #1번 세이브 데이터 없음
                return
            # pass # 저장 파일 불러 오기
        else:
            nickname = input("닉네임을  입력해 주세요 :")
            player = Player(nickname)# 2번
    else:
        nickname = input("닉네임을  입력해 주세요 :")
        player = Player(nickname)

    while True:
        print("\n[메뉴]")
        print("1. 배틀")
        print("2. 상점")
        print("3. 내 아이템 확인")
        print("4. 내 정보 확인")
        print("5. 게임 종료")
        choice = input("선택 : ")

        if choice == "1":
            print("\n[배틀]")
        elif choice == "2":
            print("\n[상점]")
            shop(player)
        elif choice == "3":
            print("\n[내 아이템 확인]")
        elif choice == "4":
            print("\n[내 정보 확인]")
            print(f"닉네임 : {player.nickname}\n 레벨: {player.level} ({player.exp}/{player.max_exp})\n공격력 : {player.attack}\n치명타 확률: "
                  f"{player.cri_luk}\nhp: {player.hp}\nmp:{player.mp}\n골드:{player.gold}")
        elif choice == "5":
            print("\n[게임 종료]")
            save_game(player)
            break
        else:
            print("잘못된 입력입니다.")
            
            

if __name__ == "__main__": # 다른 파일 실행 방지
    main()
