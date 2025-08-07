glassbottle = 9
plasticbottle = 7
returnamountglass = 5
print("Glass bottle : " , glassbottle)
print("Plastic bottle : " , plasticbottle)
print("Return amount for the glass bottle :  " , returnamountglass)
availablebal = int(input("amount"))
glassbottlesreq = int(input("Number of glass bottles u need :"))
Plasticbottlesreq = int(input("Number of Plastic bottles u need :"))
nnumberofglassbottles = 0
nnumberofplasticbottles = 0


while availablebal>glassbottle:
    availablebal = availablebal-glassbottle
    availablebal = availablebal+returnamountglass
    nnumberofglassbottles +=1

while availablebal > plasticbottle:
    availablebal = availablebal - plasticbottle
    nnumberofplasticbottles += 1

if(nnumberofglassbottles>glassbottlesreq) :
    print("U can buy ",glassbottlesreq , "glass bottles")
else :
    print("U can cant buy ",glassbottlesreq , "glass bottles & u can only buy " , nnumberofglassbottles , "with ur availbale amount")

if(nnumberofplasticbottles>Plasticbottlesreq) :
    print("U can buy ",Plasticbottlesreq , "plastic bottles")
else :
    print("U can cant buy ",Plasticbottlesreq , "plastic bottles  u can only buy " , nnumberofplasticbottles , "with ur availbale amount")



