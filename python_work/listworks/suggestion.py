all_user=["mohanlal","fahad","unni","mamooty","nivin"]
nivin_friends=["mohanlal","unni","fahad"]
fahad_friend=["mohanlal","mamooty","unni"]
suggestion_list=[]
for u in all_user:
    if u not in nivin_friends:
        suggestion_list.append(u)
suggestion_list.pop(suggestion_list.index("nivin"))
print(suggestion_list) 