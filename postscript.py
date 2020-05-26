opstack = []  #assuming top of the stack is the end of the list

def opPop():
    if opstack==[]:
        return None
    return opstack.pop()
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    if dictstack==[]:
        return None
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    begin()
    d = dictPop()
    d[name] = value
    dictPush(d)
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    dictstack_copy = dictstack.copy()
    dictstack_copy.reverse()
    for d in dictstack_copy:
        for key, value in d.items():
            if not isinstance(key,str):
                raise TypeError('Error: key not valid')
            elif name == key[1:]:
                return value          
    print(name + str(TypeError))
    return None
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            raise TypeError("Error: add - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: add expects 2 operands")

def sub():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1-op2)
        else:
            raise TypeError("Error: sub - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: sub expects 2 operands")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1*op2)
        else:
            raise TypeError("Error: mul - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: mul expects 2 operands")
        
def div():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            if op2 != 0:
                opPush(op1/op2)
            else:
                raise TypeError('Error: non-zero denominator please!')
        else:
            raise TypeError("Error: div - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: div expects 2 operands")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(type(op1)==type(op2)):
            opPush(op1==op2)
        else:
            raise TypeError("Error: not same type")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: mul expects 2 operands")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1<op2)
        else:
            raise TypeError("Error: lt - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: lt expects 2 operands")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1>op2)
        else:
            raise TypeError("Error: gt - one of the operands is not a numerical value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: gt expects 2 operands")

def psAnd():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1&op2)
        else:
            raise TypeError("Error: psAnd - one of the operands is not a boolean value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: psAnd expects 2 operands")

def psOr():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1|op2)
        else:
            raise TypeError("Error: psOr - one of the operands is not a boolean value")
            opPush(op1)
            opPush(op2)
    else:
        raise TypeError("Error: psOr expects 2 operands")

def psNot():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op,bool):
            opPush(not op)
        else:
            raise TypeError("Error: psNot - it is not a boolean value")
            opPush(op)
    else:
        raise TypeError("Error: psNot expects 1 operands")

#--------------------------- 25% -------------------------------------
# Array operators: define the string operators length, get, getinterval, put, putinterval
def length():
    target = opPop()
    mark()
    if not isinstance(target,list):
        raise TypeError('Error: not an array')
        cleartomark()
        opPush(target)
    else:
        count = 0
        # remove possible mark in target
        for op in target:
            if op == '-mark-':
                target.remove(op)
                count += 1 
        target.reverse()
        while target:
            op = target.pop()
            if op in ['add','sub','mul','div','eq','lt','gt','psAnd','psOr','psNot']:
                eval(op)()
            else:
                opPush(op)
        
        counttomark()
        count += opPop()
        cleartomark()
        opPush(count)
        return None
        
def get():
    index = opPop()
    if not isinstance(index,int):
        raise TypeError('Error: not an index')
        opPush(index)
    else:
        target = opPop()
        if not isinstance(target,list):
            raise TypeError('Error: not an array')
            opPush(target)
            opPush(index)
        else:
            target_copy = target.copy()
            mark()
            target.reverse()
            while target:
                op = target.pop()
                if op in ['add','sub','mul','div','eq','lt','gt','psAnd','psOr','psNot']:
                    eval(op)()
                else:
                    opPush(op)
            counttomark()
            total_index = opPop()
            if(index>=total_index):
                raise TypeError('Error: index out of range')
                cleartomark()
                opPush(target_copy)
                opPush(index)
            else:
                get_op = opstack[index-total_index]
                cleartomark()
                opPush(get_op)
            return None

def getinterval():
    count = opPop()
    start_index = opPop()
    end_index = start_index + count
    if ((not isinstance(start_index,int)) | (not isinstance(end_index,int))):
        raise TypeError('Error: index not valid')
        opPush(start_index)
        opPush(count)
    else:
        target = opPop()
        if not isinstance(target,list):
            raise TypeError('Error: not an array')
            opPush(target)
            opPush(start_index)
            opPush(count)
        else:
            target_copy = target.copy()
            mark()
            target.reverse()
            while target:
                op = target.pop()
                if op in ['add','sub','mul','div','eq','lt','gt','psAnd','psOr','psNot']:
                    eval(op)()
                else:
                    opPush(op)
            counttomark()
            total_index = opPop()
            if (start_index>=total_index) | (end_index>=total_index) | (start_index>=end_index):
                raise TypeError('Error: index out of range')
                cleartomark()
                opPush(target_copy)
                opPush(start_index)
                opPush(count)
            else:
                get_op = opstack[(start_index-total_index):(end_index-total_index)]
                cleartomark()
                opPush(get_op)
            return None

def put():
    value = opPop()
    index = opPop()
    if (not isinstance(index,int)) | (not isinstance(value,int)):
        raise TypeError('Error: not an index')
        opPush(index)
        opPush(value)
    else:
        target = opPop()
        if not isinstance(target,list):
            raise TypeError('Error: not an array')
            opPush(target)
            opPush(index)
            opPush(value)
        else:
            target[index] = value
            

def putinterval():
    value = opPop()
    index = opPop()
    if (not isinstance(index,int)) | (not isinstance(value,list)):
        raise TypeError('Error: not valid')
        opPush(index)
        opPush(value)
    else:
        target = opPop()
        if not isinstance(target,list):
            raise TypeError('Error: not an array')
            opPush(target)
            opPush(index)
            opPush(value)
        else:
            target[index:(index+len(value))]=value

#--------------------------- 15% -------------------------------------
# Define the stack manipulation and raise TypeError operators: dup, copy, count, pop, clear, exch, mark, cleartomark, counttotmark
def dup():
    op = opPop()
    opPush(op)
    opPush(op)

def copy():
    num = opPop()
    for op in opstack[-num:]:
        opPush(op)
    
def count():
    opPush(len(opstack))

def pop():
    opPop()
    
def clear():
    opstack.clear()

def exch():
    op2 = opPop()
    op1 = opPop()
    opPush(op2)
    opPush(op1)

def mark():
    opPush('-mark-')
    return None

def cleartomark():
    op = opPop()
    while True:
        if op == '-mark-':
            return None
        else:
            op = opPop()

def counttomark():
    opstack_copy = opstack.copy()
    opstack_copy.reverse()
    count = 0
    for op in opstack_copy:
        if op != '-mark-':
            count += 1
        else:
            opPush(count)
            return None

def stack():
    print(opstack)


def psDict():
    size = opPop()
    for idx in range(size):
        opPush({})

def begin():
    d = opPop()
    if (not isinstance(d,dict)) and d!=None:
        opPush(d)
    elif d != None:
        dictPush(d)
    elif d==None and dictstack==[]:
        dictPush({})

def end():
    dictPop()
    return None

def psDef():
    if dictstack==[]:
        dictstack.append({})
    value = opPop()
    key = opPop()
    if not isinstance(key,str):
        raise TypeError('Error: key not valid')
        opPush(key)
        opPush(value)
    elif key[0]!='/':
        raise TypeError('Error: key not valid')
        opPush(key)
        opPush(value)
    define(key,value)