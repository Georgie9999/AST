from bs4 import BeautifulSoup
import requests
import ast, dis
import astor
import re
from math import *

import networkx as nx


class MyOptimizer1(ast.NodeTransformer):
    def visit_If(self, node: ast.If):
        print(node)
        return node

class MyOptimizer2(ast.NodeTransformer):
    def visit_Constant(self, node: ast.Constant):
        if node.value==18:
            result = ast.Constant(n=20)
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        return node


class MyOptimizer3(ast.NodeTransformer):
    def visit_Call(self, node: ast.Call):
        if(node.func).id == 'range':
            result = ast.Call(func=ast.Name(id='range', ctx=ast.Load()), args=[ast.Constant(value=1)], keywords=[])
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        return node

class MyOptimizer4(ast.NodeTransformer):
    def visit_ListComp(self, node: ast.ListComp):
        result = ast.ListComp(
                                elt=ast.BinOp(
                                    left=ast.Constant(value=3),
                                    op=ast.Pow(),
                                    right=ast.Name(id='i', ctx=ast.Load())),
                                generators=[
                                    ast.comprehension(
                                        target=ast.Name(id='i', ctx=ast.Store()),
                                        iter=ast.Call(
                                            func=ast.Name(id='range', ctx=ast.Load()),
                                            args=[
                                                ast.Name(id='n', ctx=ast.Load())],
                                            keywords=[]),
                                        ifs=[],
                                        is_async=0)])
        result.lineno = node.lineno
        result.col_offset = node.col_offset
        return result

class Delete(ast.NodeTransformer):
    def visit_Assign(self, node: ast.Assign):
        return None


f = open('alg.txt', 'r')
T = f.read()
T = T.split("*****")
Osh = 0


def sravnenie(D, Grath):
    D1 = {"Module(body=[Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])], orelse=[])], type_ignores=[])": 0, "Assign(targets=[Name(id='t', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[]))": 1, "For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])], orelse=[])": 2, "Name(id='t', ctx=Store())": 3, "Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])": 4, "Name(id='i', ctx=Store())": 5, "Call(func=Name(id='range', ctx=Load()), args=[Name(id='t', ctx=Load())], keywords=[])": 6, "Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[]))": 7, "If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))], orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])])": 8, "Name(id='int', ctx=Load())": 9, "Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])": 10, "Name(id='range', ctx=Load())": 11, "Name(id='t', ctx=Load())": 12, "Name(id='n', ctx=Store())": 13, "Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Constant(value=20)])": 14, "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[]))": 15, "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[]))": 16, "For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))], orelse=[])": 17, "Name(id='input', ctx=Load())": 18, "Name(id='n', ctx=Load())": 19, 'GtE()': 20, 'Constant(value=20)': 21, "Call(func=Name(id='print', ctx=Load()), args=[Constant(value='NO')], keywords=[])": 22, "Call(func=Name(id='print', ctx=Load()), args=[Constant(value='YES')], keywords=[])": 23, "Call(func=Name(id='range', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[])": 24, "Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))]))": 25, "Name(id='print', ctx=Load())": 26, "Constant(value='NO')": 27, "Constant(value='YES')": 28, "Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))], keywords=[keyword(arg='end', value=Constant(value=' '))])": 29, "BinOp(left=Constant(value=3), op=Pow(), right=Name(id='i', ctx=Load()))": 30, "keyword(arg='end', value=Constant(value=' '))": 31, 'Constant(value=3)': 32, 'Pow()': 33, "Name(id='i', ctx=Load())": 34, "Constant(value=' ')": 35}

    Grath1 = {0: [1, 2], 1: [3, 4], 2: [5, 6, 7, 8], 3: [], 4: [9, 10], 5: [], 6: [11, 12], 7: [13, 4], 8: [14, 15, 16, 17], 9: [], 10: [18], 11: [], 12: [], 13: [], 14: [19, 20, 21], 15: [22], 16: [23], 17: [5, 24, 25], 18: [], 19: [], 20: [], 21: [], 22: [26, 27], 23: [26, 28], 24: [11, 19], 25: [29], 26: [], 27: [], 28: [], 29: [26, 30, 31], 30: [32, 33, 34], 31: [35], 32: [], 33: [], 34: [], 35: []}

    for i in range(min(len(Grath1), len(Grath))):
        pass



k=0
for s in T:
    vershin = 0
    Graph = {}
    D = {}
    try:
        print(s)
        codestr = ast.parse(s)
        optimizer1 = MyOptimizer1()
        t1 = optimizer1.visit(codestr)
        print(t1)
        optimizer2 = MyOptimizer2()
        codestr = optimizer2.visit(t1)
        optimizer3 = MyOptimizer3()
        codestr = optimizer3.visit(codestr)
        optimizer4 = MyOptimizer4()
        codestr = optimizer4.visit(codestr)
        print(ast.dump(codestr, indent=4))
        print()
        #exec(compile(codestr, "<string>", "exec"))
        new_codestr = astor.to_source(codestr, indent_with=' ' * 4, add_line_information=False,source_generator_class=astor.SourceGenerator)
        print(new_codestr)
        new_codestr = ast.parse(new_codestr)
        #exec(compile(new_codestr, "<string>", "exec"))
        #print("код")
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
        print()
        print('*************************************************************************************************************************')
        print()
        if k==1:
            break
    except:
        Osh+=1
        print(s)
        codestr = ast.parse(s)
        optimizer1 = MyOptimizer1()
        t1 = optimizer1.visit(codestr)
        optimizer2 = MyOptimizer2()
        codestr = optimizer2.visit(t1)
        print(ast.dump(codestr, indent=4))
        print()
        code = compile(codestr, "<string>", "exec")
        exec(code)
        print("код")
print(Osh)



