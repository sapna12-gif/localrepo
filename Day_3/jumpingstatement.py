# break continue, before completing the series immediately i want to exist from block.

for i in range(1,10):
    if i ==5:
     break
    print(i) # 1......9
print("program exited!!!")

for i in range(1,10):
    if i ==5:
     continue
    print(i) # 1......9
print("program exited!!!")