if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    input_list = list(arr)
    
    highestNum = input_list[0];
    for i in input_list:
        if i > highestNum:
            highestNum = i;
    secondHighest = 0;
    for i in input_list:
        if i < highestNum and i > secondHighest:
            secondHighest = i;
            
print(secondHighest)
