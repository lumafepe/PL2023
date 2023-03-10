import re
import json
media = lambda x: sum(x)/len(x)
headerSeparatorRe=re.compile(r"(\w+)(?:\{(\d+)(?:,(\d+))?\}(?:::(\w+))?)?")
bodySeparatorRe=re.compile(r",")

with open("alunos.csv","r") as fp:
    header= fp.readline()
    bodyLines = map(lambda x :bodySeparatorRe.split(x[:-1]),fp.readlines())
headerArgs=headerSeparatorRe.findall((header))
normalizedHeaderArgs=[]

for arg in headerArgs:
    op=arg[3]
    maximumArgs= int(arg[2]) if arg[2]!='' else ( int(arg[1]) if arg[1]!='' else -1 )
    nome=arg[0]
    normalizedHeaderArgs.append((nome,maximumArgs,op))

l=[]
for p,bline in enumerate(bodyLines):
    l.append({})
    n=0
    for arg in normalizedHeaderArgs:
        if arg[1]==-1:
            l[p][arg[0]]=bline[n]
            n+=1
        else:
            t=n
            tlist=[]
            while n<t+arg[1] and len(bline)>n:
                if (bline[n]==''):
                    break
                else:
                    tlist.append(int(bline[n]))
                    n+=1
            n=t+arg[1]
            l[p][arg[0]]=tlist
            if arg[2]=='media':
                l[p][arg[0]+"_media"]=media(l[p][arg[0]])
                del l[p][arg[0]]
            if arg[2]=='sum':
                l[p][arg[0]+"_sum"]=sum(l[p][arg[0]])
                del l[p][arg[0]]

with open("alunos.json","w") as fp:
    json.dump(l, fp)
       
        

        