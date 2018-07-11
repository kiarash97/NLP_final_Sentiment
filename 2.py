import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from afinn import Afinn
import random
from sklearn.metrics import precision_recall_fscore_support
# from nltk.stem import PorterStemmer
# from nltk.tokenize import word_tokenize

x = open('AFINN-111.txt','r')
polarityLexDict ={}

def preProcessing(text):
    text = text.replace("," , " , ")
    text = text.replace(".", " . ")
    text = text.lower()
    return text

def sentencePolarity(text , dict):
    text = preProcessing(text)
    # lst_word = word_tokenize(text)
    lst_word = text.split(" ")
    count = 0
    notFlag = False
    andFlag = False
    lastWordPolarity = 0
    # ps = PorterStemmer
    for word in lst_word:
        # word = ps.stem(word)
        if word == "and":
            andFlag = True
        if word == "not":
            notFlag = True

        if "," in word or "." in word :
            notFlag = False

        if word in dict and not notFlag:
            count += dict[word]
            lastWordPolarity = dict[word]

        if word in dict and notFlag:
            count += -dict[word]
            lastWordPolarity = dict[word]


        if word not in dict and andFlag:
            andFlag = False
            count += lastWordPolarity

    return count

def drawPlot(timeDict):
    inputday = []
    avg = []
    inputdates = []
    values = []
    for i in timeDict:
        day = int(i.split(" ")[0].split("-")[2])
        month = int(i.split(" ")[0].split("-")[1])
        year = int(i.split(" ")[0].split("-")[0])
        date = datetime.datetime(year, month,day)
        inputdates.append(date)
        values.append(timeDict[i][0])
    plt.subplot(211)
    plt.plot_date(inputdates, values)


    values = []
    day29sum = 0
    day29count = 0
    day30sum = 0
    day30count = 0
    day1sum = 0
    day1count = 0
    day2sum = 0
    day2count = 0
    day3sum = 0
    day3count = 0
    day4sum = 0
    day4count = 0
    day5sum = 0
    day5count = 0
    day6sum = 0
    day6count = 0
    day7sum = 0
    day7count = 0
    for i in timeDict:
        day = int(i.split(" ")[0].split("-")[2])
        if day == 29 :
            day29sum += timeDict[i][0]
            day29count +=1
            day29 = i.split(" ")[0]
        if day == 30 :
            day30sum += timeDict[i][0]
            day30count += 1
            day30 = i.split(" ")[0]
        if day == 1 :
            day1sum += timeDict[i][0]
            day1count += 1
            day1 = i.split(" ")[0]
        if day == 2 :
            day2sum += timeDict[i][0]
            day2count += 1
            day2 = i.split(" ")[0]
        if day == 3 :
            day3sum += timeDict[i][0]
            day3count += 1
            day3 = i.split(" ")[0]
        if day == 4 :
            day4sum += timeDict[i][0]
            day4count += 1
            day4 = i.split(" ")[0]
        if day == 5 :
            day5sum += timeDict[i][0]
            day5count += 1
            day5 = i.split(" ")[0]
        if day == 6 :
            day6sum += timeDict[i][0]
            day6count += 1
            day6 = i.split(" ")[0]
        if day == 7 :
            day7sum += timeDict[i][0]
            day7count += 1
            day7 = i.split(" ")[0]

    values.append(float(day29sum) / float(day29count))
    values.append(float(day30sum) / float(day30count))
    values.append(float(day1sum) / float(day1count))
    values.append(float(day2sum) / float(day2count))
    values.append(float(day3sum) / float(day3count))
    values.append(float(day4sum) / float(day4count))
    values.append(float(day5sum) / float(day5count))
    values.append(float(day6sum) / float(day6count))
    values.append(float(day7sum) / float(day7count))
    inputdates = [day29 , day30, day1, day2, day3, day4, day5, day6, day7]
    plt.subplot(212)
    plt.bar(inputdates, values, width=0.5)

    plt.show()

def afinnOutput(text ):
    classifier = Afinn(language = 'en')
    return classifier.score(text)

def getSamplefromDict(dict , number ):
    outdict = {}
    for i in range(number):
        comment, value = random.choice(list(dict.items()))
        outdict[comment] = value
    return outdict

def evaluate(sampledict ):
    myOutputlst = []
    afinnOutputlst = []
    for i in sampledict :
        myOutputlst.append( stepFunction(sampledict[i][0]) )
        afinnOutputlst.append( stepFunction( afinnOutput(sampledict[i][1])) )

    precision , recall , fscore , support= precision_recall_fscore_support (afinnOutputlst , myOutputlst ,
                                                                             average = 'weighted')

    return precision , recall , fscore

def stepFunction(input ):
    if input > 0 :
        return "pos"
    elif input < 0 :
        return "neg"
    else :
        return "none"

for i in x.readlines():
    i = i.strip()
    a = i.split("\t")
    polarityLexDict[a[0]]=int(a[1])
x.close()

timeDictComment = {}
with open('worldCup.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        timeDictComment[row['time']] = sentencePolarity(row['comment'],polarityLexDict) , row['comment']


sample =  getSamplefromDict(timeDictComment , 100)
precision , recall , fscore = evaluate(sample)

print ("precision = " , precision)
print ("recall = " , recall)
print ("fscore = " , fscore)
drawPlot(timeDictComment)