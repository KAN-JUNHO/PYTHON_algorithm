box = [int(input()) for i in range(9)]

hap = sum(box)

for i in range(len(box)):
    for j in range(i+1,len(box)):
        if 100==hap-box[i]-box[j]:
            box.remove(box[i])
            box.remove(box[j-1])
            box.sort()

            for i in box:
                print(i)
            break