text="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
word=text.split(" ")
for w in word:
    if w.startswith("@"):
        print(w)