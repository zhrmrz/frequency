def frequency():
    inp = input()
    if inp=='':
        return
    list_of_input=[int(s) for s in inp.split(',')]
    list_of_set_of_input=list(set(list_of_input))
    print('**********')
    for i in range(len(list_of_set_of_input)):
        print('*',list_of_set_of_input[i],':',list_of_input.count(list_of_set_of_input[i]))
        print('**********')

if __name__ == '__main__':
    frequency()
