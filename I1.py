from bs4 import BeautifulSoup
import requests
import ast, dis
import re

cookies = {
    'RCPC': 'd2c5ce02c40abd45c44f112ecc58e037',
}


def sravnenie(D, Grath):
    D1 = {
        "Module(body=[Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])], orelse=[])], type_ignores=[])": 0,
        "Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[]))": 1,
        "For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])], orelse=[])": 2,
        "Name(id='t', ctx=Store())": 3,
        "Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])": 4,
        "Name(id='i', ctx=Store())": 5,
        "Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[])": 6,
        "Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[]))": 7,
        "If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])": 8,
        "Name(id='int', ctx=Load())": 9, "Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])": 10,
        "Name(id='range', ctx=Load())": 11, "Name(id='t', ctx=Load())": 12, "Name(id='n', ctx=Store())": 13,
        "Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)])": 14,
        "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))": 15,
        "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[]))": 16,
        "For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])": 17,
        "Name(id='input', ctx=Load())": 18, "Name(id='n', ctx=Load())": 19, 'GtE()': 20, 'Constant(value=20)': 21,
        "Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[])": 22,
        "Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])": 23,
        "Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[])": 24,
        "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))": 25,
        "Name(id='print', ctx=Load())": 26, "Constant(value='NO')": 27, "Constant(value='YES')": 28,
        "Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))])": 29,
        "BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))": 30,
        "keyword(arg='end', value=Constant(value=' '))": 31, 'Constant(value=3)': 32, 'Pow()': 33,
        "Name(id='i', ctx=Load())": 34, "Constant(value=' ')": 35}

    Grath1 = {0: [1, 2], 1: [3, 4], 2: [5, 6, 7, 8], 3: [], 4: [9, 10], 5: [], 6: [11, 12], 7: [13, 4],
              8: [14, 15, 16, 17], 9: [], 10: [18], 11: [], 12: [], 13: [], 14: [19, 20, 21], 15: [22], 16: [23],
              17: [5, 24, 25], 18: [], 19: [], 20: [], 21: [], 22: [26, 27], 23: [26, 28], 24: [11, 19], 25: [29],
              26: [], 27: [], 28: [], 29: [26, 30, 31], 30: [32, 33, 34], 31: [35], 32: [], 33: [], 34: [], 35: []}

    for i in range(min(len(Grath1), len(Grath))):
        pass
    return 0

Osh = 0

for i in range(1, 10):

    url_number = "https://codeforces.com/contest/1651/status/B/page/"+str(i)+"?order=BY_PROGRAM_LENGTH_ASC"
    page_number = requests.get(url_number, cookies=cookies)

    soup = BeautifulSoup(page_number.text, "lxml")
    all_numbers = soup.findAll('a',class_="view-source")
    r = requests.get(url_number)
    all_results = soup.findAll('span', class_="verdict-accepted")
    results = [str(str(res.text)) for res in all_results]
    numbers = [str(str(num.text)) for num in all_numbers]
    print(results)
    #print(numbers)

    k=0
    for s in numbers:
        vershin = 0
        Graph = {}
        D = {}
        url_code = "https://codeforces.com/contest/1651/submission/"+s
        page_code = requests.get(url_code, cookies=cookies)
        soup = BeautifulSoup(page_code.text, "html.parser")
        all_code = soup.findAll('pre', class_='prettyprint')
        for code in all_code:
            codestr = str(code.text)
        try:
            #print(codestr)
            codestr = ast.parse(codestr)
            #print(ast.dump(codestr, indent=4))
            print()
            print('*************************************************************************************************************************')
            print()
            for node in ast.walk(codestr):
                t = []
                nd = ast.dump(node)
                if nd not in D and (str(nd)!='Load()' and str(nd)!='Store()'):
                    D[str(nd)] = vershin

                    vershin += 1
                #print(ast.dump(node, indent=4))
                for ch in ast.iter_child_nodes(node):
                    ch = ast.dump(ch)
                    t.append(ch)
                    if ch not in D and (str(ch)!='Load()' and str(ch)!='Store()'):
                        D[str(ch)] = vershin
                        vershin+=1
            for node in ast.walk(codestr):
                nd = ast.dump(node)
                t1 = []
                for ch in ast.iter_child_nodes(node):
                    ch = ast.dump(ch)
                    if (str(ch)!='Load()' and str(ch)!='Store()'):
                        t1.append(D[str(ch)])
                if (str(nd) != 'Load()' and str(nd) != 'Store()'):
                    Graph[D[str(nd)]] = t1
            print(D)
            print(Graph)
            if k==1:
                break
        except:
            Osh+=1
print("Количество алгоритмов с ошибкой компиляции или ошибкой парсинга:", Osh)









