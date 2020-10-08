import random
#random.seed(0)#need to get deleted
statementstorage=list()
############
class people:
    peoplelist=[]
    record=[]
    statementdict=dict()
    @staticmethod
    def decide_role(number):
        if number ==1:
            return 'knight'
        elif number==0:
            return 'knave'
        #else:
            #return 'normal'




    def __init__(self,name,role):
        self.value=None
        self.role=role
        self.name=name
        self.statement=[]
        self.peoplelist.append(self)


    @classmethod
    def updatelist(cls):
        cls.record=[]
        for peeps in cls.peoplelist:
            cls.record.append({(peeps.name,peeps.role):peeps.value})

    @classmethod
    def assignstatements(cls):
        cls.statementdict=dict()
        tem=list(statementstorage)
        for p in cls.peoplelist:
            cls.statementdict.update({p:tem.pop(random.randint(0,len(tem)-1))})
        for i in people.statementdict.items():
            sayer, saying=i
            k=saying.check_statement(sayer.value)
            while not k:
                saying=tem.pop(random.randint(0,len(tem)-1))
                k=saying.check_statement(sayer.value)
            cls.statementdict[sayer]=saying
        return tem#this returns the list of statements that is still available after giving all the people a legit statement
    
    @classmethod
    def generatepuzzle(cls):
        people.assignstatements()
        for i in people.statementdict.items():
            sayer, saying=i
            saying=saying.statement.replace(str(sayer),'himself')
            print(f'{sayer} told you that {saying}')





    def setvalue(self):
        if self.role=='knave':
            self.value=False
        elif self.role=='knight':
            self.value=True
        else:
            self.value=True or False
    def __repr__(self):
        return self.name

#################
class statements:
    def __init__(self,name,statement,code,value=None,sayer_value=None):
        self.name=name
        self.statement=statement
        self.code=code
        self.value=value
        self.cred_value=sayer_value
    def __repr__(self):
            return self.name
    def check_statement_role(self):
        tem=[]
        for key in self.code.keys():
            if key.role == self.code[key]:
                tem.append(True)
            else:
                tem.append(False)
        if all(tem):
            self.value=True
        else:
            self.value=False 
    def cred_updater(self,value):
        self.cred_value=value

    def check_statement(self,sayer_value):
        self.check_statement_role()
        self.cred_updater(sayer_value)
        if self.cred_value==self.value:
            return True
        else:
            return False
####################
def permuteBool(n):
    l=list()
    if n==0:
        return l
    elif n==1:
        return [[True],[False]]
    else:
        for a in (permuteBool(n-1)):
            tem=list(a)
            tem.append(True)
            l.append(tem)
            tem=list(a)
            tem.append(False)
            l.append(tem)
        return l

##########
def check_solution(a_state_dict):
    l=list()
    checklist=permuteBool(len(a_state_dict.keys()))
    for i in checklist:
        counter=0
        for person in people.statementdict.keys():
            person.role=(people.decide_role(i[counter]))
            counter+=1
        counter=0
        tem=list()
        for j in a_state_dict.items():
            sayer, saying=j
            if saying.check_statement(i[counter]):
                tem.append(True)
            else:
                 tem.append(False)
                 break
            counter+=1
        if all(tem):
            l.append(i)     
    return l
##############


def create_people(): 
    people('A',people.decide_role(random.randint(0,1)))
    people('B',people.decide_role(random.randint(0,1)))
    people('C',people.decide_role(random.randint(0,1)))
    people('D',people.decide_role(random.randint(0,1)))
    people('E',people.decide_role(random.randint(0,1)))
    people('F',people.decide_role(random.randint(0,1)))
    people('G',people.decide_role(random.randint(0,1)))
    for person in people.peoplelist:
        person.setvalue()   
    people.updatelist()


def create_statement():
    for person in people.peoplelist:
        temp=statements(str(person)+'.knight',str(person)+' is a knight',{person:'knight'})
        statementstorage.append(temp)
    for person in people.peoplelist:
        temp=statements(str(person)+'.knave',str(person)+' is a knave',{person:'knave'})
        statementstorage.append(temp)
    #for person in people.peoplelist:
        #temp=statements(str(person)+'.normal',str(person)+' is normal',{person:'normal'})
        #statementstorage.append(temp)   
    klist=list(people.peoplelist)
    i=0
    for person in people.peoplelist:
        klist.pop(i)
        for p in klist:  
            temp=statements(str(person)+'.'+str(p)+'.same',str(person)+' is the same as '+str(p),{person:p.role})
            statementstorage.append(temp)
#this method creates statements but do not assign statements to sayer


######################
def puzzle():
    create_people()
    #print(people.record)#this need to get deleted in actual code
    create_statement()
    people.generatepuzzle()
def check_answer(answer,possible_solutions):
    answer=answer[1:-1].split(',')
    temp=[]
    for i in answer:
        if i =='1':
            temp.append(True)
        elif i=='0':
            temp.append(False)
        else:
            print('Bad input')
    if temp in possible_solutions:
        return (True,temp)
    else:
        return (False,temp)



def main():
    a='''A very special island is inhabited only by knights and knaves. Knights always tell the truth, and knaves always lie.
One day, you met seven inhabitants: A, B, C, D, E, F, and G, and had conversation with them.
Here is the information you got:'''
    print(a)
    puzzle()
    b=list(check_solution(people.statementdict))
    print('Can you determine what are A, B, C, D, E, F, and G? ')
    print(f'There are {len(b)} possible combinations in total')
    if len(b)>5:
        print('you only have to input 5 solutions')
    else:
        print(f'you will have to input all {len(b)} possible combinations')
    print('''\n_________________\nInput your answer in this form:
    Use 1 for knight, 0 for knave.
    ({Here goes the identity for A},{Here goes the identity for B},{Here goes the identity for C},{Here goes the identity for D},{Here goes the identity for E},{Here goes the identity for F},{Here goes the identity for G})
    For example (1,1,1,1,1,1,1) for all of them being knight\n''')
    print(b)
    counter=4
    if len(b)>5:
        tem=[]
        for i in range(5):
            res1=input('Your answer\n____________\n')
            value, used=check_answer(res1,b)
            if value:
                print(f'you get it right\nThere are {counter} more to go')
                tem.append(True)
                b.pop(b.index(used))
                counter-=1
            else:
                tem.append(False)
                print('Wrongg')
                break
        if all(tem):
            print('''you get it right!!!!!!!!!
            ______________________________
             here is your flag and the last puzzle for you:
             knight: 'either flag{what_is_the_flag} is wrong or 2+2=3.'
             knave: 'the flag is not wrong but the statement must be true, so 2+2=3.'
             What's wrong with it?
             ''')
        else:
            print('try again')
    else:
        tem=[]
        for i in range(len(b)):
            res1=input('Your answer\n____________\n')
            value, used=check_answer(res1,b)
            if value:
                print('you get it right\n Next answer')
                b.pop(b.index(used))
                tem.append(True)
            else:
                tem.append(False)
                print('Wrongg')
                break
        if all(tem):
            print('''you get it right!!!!!!!!!
            ______________________________
             here is your flag and the last puzzle for you:
             knight: 'either flag{what_is_the_flag} is wrong or 2+2=3.'
             knave: 'the flag is not wrong but the statement must be true, so 2+2=3.'
             What's wrong with it?
             ''')
        else:
            print('Try again')
            
if __name__ == "__main__":
    main()