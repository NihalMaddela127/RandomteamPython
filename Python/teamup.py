import json
import random

fopen = open("aspirants.json" ,"r")
rdata = json.load(fopen)
fopen.close
asplen=len(rdata['aspirants'])
print asplen
num=input('Enter number of members in team : ')
text_file = open('Result.txt', 'a')
text_file.write("\nReport \n\n")
if((asplen%num!=0)and(asplen%num>0)):
    print "Cannot divide equally"
    print "Do you wish to continue???"
    feed1=raw_input('Y/N : ')
    if(feed1=="y"):
        rem=asplen%num
        temp = num
        team = 1
        for asps in rdata['aspirants'][:]:
            if temp==num:
                print("Team {} has:".format(team))
                text_file.write("Team {} has:".format(team)+"\n")
                if rem!=0:
                    
                    person=random.choice(rdata['aspirants'])
                    text_file.write(", ".join(person.keys())+"\n")
                    print(", ".join(person.keys()))

                    temp+=1
                    rdata['aspirants'].remove(person)
                    rem-=1
                    if not rdata['aspirants']:
                        break
                temp=0
                team+=1     

            person=random.choice(rdata['aspirants'])
            text_file.write(", ".join(person.keys())+"\n")
            print(", ".join(person.keys()))

            temp+=1
            rdata['aspirants'].remove(person)
            if not rdata['aspirants']:
                        break
    else:
        print "ty"
elif (asplen%num==0):
    temp=num
    team=1
    for asps in rdata['aspirants'][:]:
        if temp==num:
            text_file.write("Team {} has:".format(team)+"\n")
            print("Team {} has:".format(team))
            temp=0
            team+=1 
        person=random.choice(rdata["aspirants"])
        text_file.write(", ".join(person.keys())+"\n")
        print(", ".join(person.keys()))
        temp+=1
        rdata['aspirants'].remove(person)
else:
    print"Wrong input"
text_file.close()
