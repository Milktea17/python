def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#직접 파일을 실행했을 때만 수행되게 한다.
if __name__ == "__main__" :
    print(add(1, 4))
    print(sub(4, 2))