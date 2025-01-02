while True:
    word = input()
    
    if word == '0':
        break
    
    stop = False
    n = len(word)
    for i in range(n//2 + 1):
        if word[i] != word[n - i - 1]:
            print('no')
            stop = True
            break
    
    if stop:
        continue

    print('yes')