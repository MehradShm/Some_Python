# Wanted To Implement An Imaginary Class of Dota 2 Heroes :)

class Hero:
    type = "Hero"
    levelUpThreshold = [10 , 25 , 45 , 70 , 100 , 135 , 175 , 220 , 270 , 325]
    itemList = []
    status = "Alive"
    respawnTime = 0
    currentMoney = 600
    netWorth = currentMoney
    def __init__(self , str , agil , intel , ar , as , bh , bd , pa , lvl , bm , sg , ag , ig , hr , mr , xp):
        self.strength         = str
        self.agility          = agil
        self.intelligence     = intel
        self.armor            = ar
        self.attackSpeed      = as
        self.baseHealth       = bh
        self.baseDamage       = bd
        self.primaryAttribute = pa
        self.level            = lvl
        self.baseMana         = bm
        self.strengthGain     = sg
        self.agilityGain      = ag
        self.intelligenceGain = ig
        self.healthRegenerate = hr
        self.manaRegenerate   = mr
        self.experience       = xp

    def calculateRespawnTime(self):
        self.respawnTime = 3 + ((self.level-1) * 2)

    def showItems(self):
        for item in itemlist:
            print(item.name , end= " , ")
        print("")

    def primaryAmount(self):
        if self.primaryAttribute   = "Strength":
            return self.strength
        elif self.primaryAttribute = "Agility":
            return self.agility
        else
            return self.intelligence

    def getGold(self , target):
        if target.type == "Hero":
            temp = min(250 , target.currentMoney)
            self.currentMoney += temp
            self.netWorth += temp
        elif target.type == "Creep":
            if target.attackType == "Melee":
                self.currentMoney += 15
                self.netWorth += 15
            else :
                self.currentMoney += 30
                self.netWorth += 30

    def getExperience(self , target):
        if target.type == "Hero"
            self.experience += target.level * 10

        elif target.type == "Creep":
            if target.attackType == "Melee":
                self.experience += 2
            else :
                self.experience += 6

    def NormalAttack(self , target):
        target.baseHealth -= max(target.baseHealth , (self.baseDamage + self.primaryAmount))
        if target.baseHealth == 0 :
            target.dies();
            getExperience(self , target)
            getGold(self, target)

    def addItemAttributes(self , Item):
        self.strength         += Item.strength
        self.agility          += Item.strength
        self.intelligencfe    += Item.intelligenceGain
        self.healthRegenerate += Item.healthRegenerate
        self.manaRegenerate   += Item.manaRegenerate


    def buyItem(self , Item):
        if self.currentMoney >= Item.Price :
            self.currentMoney -= Item.Price
            self.itemList.append(Item)
            self.addItemAttributes(Item)

    def dies(self):
        self.status = "Dead"
        temp = min(250 , self.currentMoney)
        self.currentMoney -= temp
        self.netWorth -= temp
        calculateRespawnTime()
