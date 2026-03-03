def q(a):
    def e():
        print("실행")
        a()
        print("종료")
    return e

@q        
def tq():
    print("출력함수")

tq()
    

