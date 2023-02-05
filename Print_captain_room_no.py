room_size=int(input())
players=list(map(int, input().strip().split()))[:room_size*6+1]
player=sorted(players)
for i in range(0,len(players)):
  if player.count(player[i])==1:
    print(player[i])
  else:
    continue
