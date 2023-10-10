all_user=["sachin","dhoni","kohli","rohit","sanju","padikkal"]
sanju_followings=["padikkal","sachin"]
suggestions=list(set(all_user).difference(set(sanju_followings)))
sanju_pos=suggestions.index("sanju")
suggestions.pop(sanju_pos)
print(suggestions)