import json, os

FILE = "passwords.json"
vault = json.load(open(FILE, "r", encoding="utf-8")) if os.path.exists(FILE) else {}

while True:
    print("\n--- [1] 목록 조회 [2] 계정 추가 [3] 계정 삭제 [4] 종료 ---")
    cmd = input("선택: ")
    
    if cmd == "1":
        print("\n".join(f"- 사이트: {k} | 아이디/비번: {v}" for k, v in vault.items()) or "저장된 계정이 없습니다.")
    elif cmd == "2":
        site = input("사이트/서비스 이름: ")
        info = input("아이디/비밀번호 정보: ")
        vault[site] = info
        json.dump(vault, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("저장되었습니다.")
    elif cmd == "3":
        site = input("삭제할 사이트 이름: ")
        if vault.pop(site, None):
            json.dump(vault, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            print("삭제되었습니다.")
        else:
            print("해당 사이트가 존재하지 않습니다.")
    elif cmd == "4":
        break
