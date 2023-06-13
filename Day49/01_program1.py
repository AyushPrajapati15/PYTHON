students={
    101:{'name':'alice','email':'alice@gmail.com','address':'bbsr'},

    102:{'name':'bob','email':'bob@gmail.com','address':'ctc'},

    103:{'name':'jack','email':'jack@gmail.com','address':'bbsr'},

    104:{'name':'mary','email':'mary@gmail.com','address':'rkl'}
}

for k,v in students.items():
    print('student id is : ',k)

    for i in v:
        print(f'{i} is : {v[i]}')
    print('-'*20)