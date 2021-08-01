def cal4(tp, a, *args):
    if tp == 'add':
        result = a
        for i in args:
            result +=i    

    elif tp == 'minus':
        result = a
        for i in args:
            result -= i
            
    elif tp == 'multiple':
        result = a 
        for i in args:
            result *= i
            
    elif tp == 'division':
        try :
            result = a
            for i in args:
                result /= i
                
        except ZeroDivisionError:
            print('0은 입력할 수 없습니다. 다시 입력해주세요')
            
    else :
        print('잘못 입력하셨습니다.')    
    print(result)
