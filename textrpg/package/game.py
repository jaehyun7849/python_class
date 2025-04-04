from package.constants import shop_items


def shop(player):
    print("\n[상점]")
    print(f"\n보유 골드: {player.gold}")
    for idx, item in enumerate(shop_items):
        print(f"{idx + 1}. {item["name"]}(추가 공격력 : {item["attack"]},추가 HP :{item["hp"]},추가 치명타 확률: {item["cri_luk"]})")
    choice = int(input("구매할 아이템 번호를 입력 해주세요(취소: 0):"))-1
    if 0<= choice <len(shop_items):
        item = shop_items[choice]
        if player.gold >= item["price"]:
            player.gold -= item["price"]
            player.items.append(item)
            player.apply_item(item)
            print(f"{item["name"]}을/를 구매 했습니다!")
        else:
            print("골드가 부족 합니다.")
    elif choice == -1:
        print("구매를 취소 했습니다.")
    else:
        print("잘못된 입력입니다..")

