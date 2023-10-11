import time

#sentence = 출력할 문자, timesl = 글자가 출력되는 시간간격(단위:초)
def hgj (sentence, timesl):
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)

hgj('글자를 0.08 간격으로 하나씩 출력하기',0.08)