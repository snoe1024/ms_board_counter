import random

def prob_LMb_1(n):
    
    width = 16 # 盤面のサイズを指定
    height = 14 # 
    posx = posy = 0 # 座標保管用
    count = 0 # ループ回数カウント
    mescnt = 0 # 途中経過出力回数
    over73 = 0 # 地雷非隣接マスが74を超えたサンプル数
    recboxes = [0] * 144 # 地雷非隣接マスカウント
    bombmax = 33 # 最大地雷設置数
    i = j = 0 # その他
    isAir = False

    while count < n:
        board = [[0 for i in range(width + 2)] for j in range(height + 2)] # 盤面初期化
        bombs = 0 # 爆弾数初期化
        clearcnt = 0 #地雷非隣接マス数初期化
        for i in range(1, width + 1):
            board[1][i] -= 1 # -1は地雷
        for i in range(1, 9): # 盤面固有
            board[2][i] -= 1
            board[3][i] -= 1
        
        while bombs < bombmax:# ランダム設置開始
            isAir = False
            while (not isAir): # 地雷設置可能？
                posx = random.randrange(width) + 1
                posy = random.randrange(height) + 1
                isAir = (board[posy][posx] == 0)
            board[posy][posx] = -1 # 地雷設置
            bombs += 1
        
        for i in range(1, width + 1): # 地雷カウント
            for j in range(1, height + 1):
                if (board[j][i] < 0):
                    continue
                board[j][i] -= min([board[j - 1][i - 1], 0])
                board[j][i] -= min([board[j - 1][i], 0])
                board[j][i] -= min([board[j - 1][i + 1], 0])
                board[j][i] -= min([board[j][i - 1], 0])
                board[j][i] -= min([board[j][i + 1], 0])
                board[j][i] -= min([board[j + 1][i - 1], 0])
                board[j][i] -= min([board[j + 1][i], 0])
                board[j][i] -= min([board[j + 1][i + 1], 0])
                if (board[j][i] == 0):
                    clearcnt += 1
        
        recboxes[clearcnt] += 1 # 統計
        if (clearcnt > 73): # これだけ別で取る
            over73 += 1

        count += 1

        if (count >= 2 ** mescnt): # 2のべき乗数回目のループで中間報告
            print("")
            print(f"[info] clearcnt: {clearcnt}")
            print(f"[info] over73: {over73} / {count}")
            mescnt += 1
        
    return over73, recboxes

result, data = prob_LMb_1(100000000)
print(f"[Final Data] over73: {result} / 10 - from prob_LMb_1") # データ

# その他のデータ出力
text = ""
for i in range(0, 10):
    text = ""
    for j in range(0, 10):
        text += "["+str(i * 10 + j)+"]: "+str(data[i * 10 + j])+", "
    print("[data] "+text)

i = input()