# ========== STACK IMPLEMENTATION ======== #
list_stack = []
while True:
    oprInput = int(input(
        '''
        Choose your operator
        1. Push element
        2. Pop element
        3. Peek element
        4. Display stack
        5. Exit
        
        '''
    ))
    if oprInput == 1:
        data1 = int(input('Masukkan angka: '))
        if data1 == 0:
            print('Empty value')
        else:
            print(data1)
            list_stack.append(data1)
            print(list_stack)
    elif oprInput == 2:
        if len(list_stack) == 0:
            print('Empty value')
        else:
            list_stack.pop()
            print(list_stack)
    elif oprInput == 3:
        if len(list_stack) == 0:
            print('Empty value')
        else:
            print(list_stack[-1])
    elif oprInput == 4:
        if len(list_stack) == 0:
            print('Empty value')
        else:
            print(list_stack)
    elif oprInput == 5:
        break
    else:
        print('Wrong Operator') 
        

# ========== QUEUE IMPLEMENTATION ======== #
list_queue = []
while True:
    oprInput = int(input(
        '''
        Choose your operator
        1. Push element
        2. Pop first element
        3. front element
        4. Last element
        5. Display queue
        6. Exit
        '''
    ))
    if oprInput == 1:
        data1 = int(input('Masukkan angka: '))
        if data1 == 0:
            print('Empty value')
        else:
            print(data1)
            list_queue.append(data1)
            print(list_queue)
    elif oprInput == 2:
        if len(list_queue) == 0:
            print('Empty value')
        else:
            del list_queue[0]
            print('Pop First: ', list_queue)
    elif oprInput == 3:
        if len(list_queue) == 0:
            print('Empty value')
        else:
            print('First element', list_queue[0])
    elif oprInput == 4:
        if len(list_queue) == 0:
            print('Empty value')
        else:
            print('First element', list_queue[-1])
    elif oprInput == 5:
        if len(list_queue) == 0:
            print('Empty value')
        else:
            print(list_queue)
    elif oprInput == 6:
        break
    else:
        print('Wrong Operator') 