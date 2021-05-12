bagcolor = 'shiny gold'
cnt = 0
cnt2 = 0
parentlist = []
def TSA(bagcolor,rulelist):
    global cnt
    global parentlist
    tempparent = []
    for rule in rulelist:
        nextbag = rule
        for child in rulelist[rule]:
            if child[0] == bagcolor:
                tempparent.append(nextbag)
                parentlist.append(nextbag)
    parentlist = list(set(parentlist))
    cnt = len(parentlist)
    for item in tempparent:
       TSA(item,rulelist)
    return cnt

def airlinefuckery(bagcolor,rulelist,numbags):
    global cnt2
    tempparent = []
    colorcnt = 0
    for rule in rulelist:
        if rule == bagcolor:
            nextbag = rule
            for child in rulelist[rule]:
                if child[1] != 'no':
                    parentlist.append(nextbag)
                    colorcnt = int(child[1])*int(numbags)
                    newrule = (child[0],colorcnt)
                    tempparent.append(newrule)
                    cnt2 += (colorcnt)
    for item in tempparent:
        airlinefuckery(item[0],rulelist,item[1])

with open(r"input","r") as file:
    inp = file.readlines()
    rulelist = {}
    for rule in inp:
        bag , contents = rule.split(' bags contain ')
        contents = contents.split(',')
        kid=[]
        for content in contents:
            content = content.split()
            temp = content[1] +' '+ content[2]
            kid.append((temp, content[0]))
        rulelist[bag] = kid
TSA(bagcolor,rulelist)
airlinefuckery(bagcolor,rulelist,1)
print (cnt)
print (cnt2)
