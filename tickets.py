import random
lst=[]
lottery_tickets_list = []
print("creating 100 random lottery tickets")

for i in range(100):
    b=random.randrange(1000000000, 9999999999)
    lottery_tickets_list.append(b)




winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)

#a=input("to see previous lottery")
#if a==("YES" or "yes"):
#   print(lottery_tickets_list)
