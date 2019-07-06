class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]  # カードの種類
    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]    # カードの数字
    
    def __init__(self, v, s):
        """スート（マーク）も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):  # 比較の仕方を定義
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):  # 比較の仕方を定義
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):   # カードオブジェクトが print 文に渡された時の挙動を定義
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v


from random import shuffle


class Deck:
    def __init__(self): #  Deckのインスタンスが生成される時点で、52枚のカードがシャッフルされた状態でリストに格納される
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
        
    def rm_card(self):  # このメソッドが実際に山からカードを引っ張ってくる行為になる。
        if len(self.cards) == 0:
            return
        return self.cards.pop() # cardsリストから１枚引いてきたカードが返り値になる。


    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
        


class Game:
    def __init__(self):
        name1 = input("プレーヤー１の名前：　")
        name2 = input("プレーヤー２の名前：　")
        self.deck = Deck()  # deckオブジェクト作成
        self.p1 = Player(name1) # Playerオブジェクトp1作成
        self.p2 = Player(name2) # Playerオブジェクトp2作成
        
    def wins(self, winner):
        w = "このラウンドは、{}が勝ちました。\n"
        w = w.format(winner)
        print(w)
        
    def draw(self, p1n, p1c, p2n, p2c):   # このメソッドは表示をするだけで、実際のカードの操作は行っていない
        d = "{}は{}を、{}は{}を引きました。"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)


    def play_game(self):  # このメソッドを呼ぶことによって、ゲームが開始される
        cards = self.deck.cards
        print("戦争を始めます！！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay：　"
            response = input(m)  # この変数response の値は'q'の時しか使われません
            if response == 'q':
                break
            p1c = self.deck.rm_card() # rm_cardの返り値が、デッキから引いてきた１枚のカードインスタンスである。
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            print("Debug: p1.card= {}, p2.card={}".format(self.p1.card, self.p2.card)) # Playerオブジェクトが持っているカードオブジェクトに何が入っているか？
            
            self.draw(p1n, p1c, p2n, p2c) # 誰が何のカードを引いたかを表示するだけのメソッド
            if p1c > p2c:
                self.p1.wins += 1 # 勝ち数の累積
                self.wins(self.p1.name) # 勝者名を表示するメソッド
            else:
                self.p2.wins += 1 # 勝ち数の累積
                self.wins(self.p2.name) # 勝者名を表示するメソッド


        win = self.winner(self.p1, self.p2) # 累積勝利数の多い方を判定して win に返すメソッド
        print("ゲーム終了、{}の勝利です。".format(win))


    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！！"




game = Game() # カード（デッキ）、プレーヤーなどのインスタンスを生成する。
game.play_game() # 作成したGameオブジェクトの play_game メソッドを呼ぶことにより、ゲームが開始される。
