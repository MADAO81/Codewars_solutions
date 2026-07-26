# https://www.codewars.com/kata/58e61f3d8ff24f774400002c/train/python

def assembler_interpreter(program):
    lines=[l.split(';')[0].strip() for l in program.split('\n')if l.split(';')[0].strip()]
    r,l,s,o,c={},{},[],[],0
    for i,ln in enumerate(lines):
        if ':'in ln and not any(x in ln for x in['mov','inc','dec','add','sub','mul','div','cmp','jmp','jne','je','jge','jg','jle','jl','call','ret','msg','end']):
            l[ln[:-1].strip()]=i
    def v(x):return r[x]if x in r else int(x)
    i=0
    while i<len(lines):
        p=lines[i].replace(',',' ').split();a=p[0]
        if a=='mov':r[p[1]]=v(p[2])
        elif a=='inc':r[p[1]]=r.get(p[1],0)+1
        elif a=='dec':r[p[1]]=r.get(p[1],0)-1
        elif a=='add':r[p[1]]=r.get(p[1],0)+v(p[2])
        elif a=='sub':r[p[1]]=r.get(p[1],0)-v(p[2])
        elif a=='mul':r[p[1]]=r.get(p[1],0)*v(p[2])
        elif a=='div':r[p[1]]=r.get(p[1],0)//v(p[2])
        elif a=='cmp':c=v(p[1])-v(p[2])
        elif a=='jmp':i=l[p[1]];continue
        elif a=='jne'and c!=0:i=l[p[1]];continue
        elif a=='je'and c==0:i=l[p[1]];continue
        elif a=='jge'and c>=0:i=l[p[1]];continue
        elif a=='jg'and c>0:i=l[p[1]];continue
        elif a=='jle'and c<=0:i=l[p[1]];continue
        elif a=='jl'and c<0:i=l[p[1]];continue
        elif a=='call':s.append(i+1);i=l[p[1]];continue
        elif a=='ret':i=s.pop();continue
        elif a=='msg':
            parts=[]
            current=''
            in_quotes=False
            rest=lines[i][3:].strip()
            for ch in rest:
                if ch=="'":
                    if in_quotes:
                        parts.append(current)
                        current=''
                    in_quotes=not in_quotes
                    continue
                if in_quotes:
                    current+=ch
                else:
                    if ch==',':
                        if current.strip():
                            if current.strip() in r:
                                parts.append(str(r[current.strip()]))
                            else:
                                parts.append(current.strip())
                        current=''
                    elif ch not in ' \t':
                        current+=ch
                    elif current:
                        # Проверяем, является ли current регистром (только буквы)
                        if current in r:
                            parts.append(str(r[current]))
                            current=''
                        elif current.isalpha():
                            # Это может быть регистр, но его пока нет
                            parts.append(current)
                            current=''
                        else:
                            current+=ch
            if current:
                if current in r:
                    parts.append(str(r[current]))
                else:
                    parts.append(current.strip())
            o.append(''.join(parts))
        elif a=='end':return''.join(o)
        i+=1
    return -1
