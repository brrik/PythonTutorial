
def calcList(objList): #objList = mainList＞変数として名前の書き換え：引数
    newList = []
    for n in objList:
        newList.append(n**5)
    return newList #戻り値：関数の実行結果

def printAll(objList):
    for i in objList:
        print(i)

mainList = [2,4,6,8,10]
nextList = calcList(mainList) #nextList = (関数の中の)newList
printAll(nextList)

mainList = [1,3,5,7,9]
nextList = calcList(mainList)
printAll(nextList)

mainList = [1,1,2,3,5,8]
nextList = calcList(mainList)
printAll(nextList)
