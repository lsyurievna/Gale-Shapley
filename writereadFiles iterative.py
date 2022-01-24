
from random import randint
import numpy as np

#### FUNCTIONS FOR WRITING FILES ######

#Get user input for 
# n - number of students and hospitals and
# k - number of possible preference lists for students and hospitals
#If no input for k is detected, k = n
#@ return k, n user input
#
def userPrompt():
    n = input("Enter the number of students and hospitals: ")
    k = input("Enter the number of possible ways to rank hospitals and students (k): ")
    #maybe add test later to check if n and k are natural numbers
    if (k == ""):
        k=n
    return (k,n)

#The following two functions implement Fisher-Yates shuffle algorithm

#This funtion creates a vector of length n, and fills it with 
#natural numbers from 1 to n in increasing order (so for n = 5, v = [1,2,3,4,5])
# @n natural number 
#
def generateRandom(n,f):
    v = [0]*n
    for i in range(n):
        v[i] = i
    
    while (len(v)):
        result = getNum(v)
        result = str(result)
        f.write(result + " ")

#Return a random number from 1 to n and then pops it from the array, so that if it is called again with the same
#vector, a different number would be produced
# @v array of numbers [1, 2, ..., n]
# @return num any random number from v
#
def getNum(v):
    n = len(v)
    index = randint(0, n-1)
    num = v[index]
    v[index], v[n-1] = v[n-1], v[index]
    v.pop()
    return(num)

#Create a list of n random numbers from 0 to k-1 and add them one by one separated by an empty space to a .txt file
# @n,k natural numbers
#
def randomizer(n,k,f):
    for i in range(n):
        number = randint(0,k-1)
        number = str(number)
        f.write(number + " ")

##### FUNCTIONS FOR READING FILES ######


#Reads the k lines with either students ranking hospitals or hospitals ranking 
#students, convert the lines to arrays, and add them to an approprite lists
#to make a 2D matrix
# @lists is either student or hospital ranking list
# @k number of permutations
# @f file to be read
#
def readRankings(k, lists, f):
    for i in range (k):
        line = f.readline()
        rankings = line.split(" ") # make line an array of elements
        rankings.pop() #get rid of "\n"
        lists.append(rankings.copy()) #append to either hospital or student ranking lists

#Read one of the last two lines in the input, and populate 
    #a dictionary that contains hospitals as keys with array of student rankings as values
    # and a dictionary that contains students as keys with array of hospital rankings as values
    # @n number of students and hospitals
    # @pref array containing which ranking a student of a hospital will choose 
    # for example if hospital_pref = [2, 0 , 1] it means that hospital 0 will have 
    # ranking list 2, hospital 1 will choose list 0, and hospital 2 will choose list 1
    # @lists with ranks
    # @rank dict the dictionary that makes the student - hospital or hospital - student
    # 2D array, it is later an input to the Gale-Shapeley algorithm
    #
def makeGSinput(n, pref, lists, rank_dict):
    for i in range (n):
        index = int(pref[i])
        rank_dict[str(i)] = lists[index].copy()


class G:
    
    def getKeyByValue(dict, ind):
        return(list(dict.keys())[list(dict.values()).index(ind)])  # Prints george
    
    def getValueByKey(dict, key):
        return dict.get(key)
    
    def getRankingsOfStudents(dict, h):
        return(dict.get(h))
    
    def getFirstStudent(dict, h):

        return dict.get(h).pop(0)
    
    def getHospitalRank(dict, h, s):
        return dict.get(s).index(h)
    
    def isInDictValues(dict, s):
        return (s in dict.values())

    def isInDictKeys(dict, k):
        return (k in dict.keys())



#### GALE - SHAPELEY ALGORITHM FUNCTION #######

def algorithm(dict, h_ranking_students, s_ranking_hospitals, n):

    iterations = 0
    hospital = 0
    h = str(hospital) #0
    s = None
    #if G.isInDictValues(dict, None):
        #print(dict)
        #print(h_ranking_students)
        #print(s_ranking_hospitals)
            
            # if no student is assigned to a hospital and hospital hasn't proposed to this specific student yet
    while (s == None and len(G.getValueByKey(h_ranking_students, h)) != 0):
        if G.isInDictValues(dict, None):
            if dict.get(h) == None:
                #assign student to the first student on the hospital ranking list
                s = G.getFirstStudent(h_ranking_students, h)
                # if the student has no offers yet, accep this offer
                if G.isInDictValues(dict,s) == False:
                    #match student
                    dict[h] = s


                    # print("if")
                    # print(h)
                    

                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1

                    # print(iterations)
                    # print(dict)

                #if student prefers proposed h to matched h
                #current hospital = G.getKeyByValue(dict,s)
                #proposed hospital = h
                #if current hospital index < proposed hospital index
                elif G.getHospitalRank(s_ranking_hospitals, G.getKeyByValue(dict,s), s) > G.getHospitalRank(s_ranking_hospitals, h, s):
                    #print (G.getHospitalRank(s_ranking_hospitals, G.getKeyByValue(dict,s), s))
                    #print (G.getHospitalRank(s_ranking_hospitals, h, s))
                    #cancel the student's previous arrangement
                    dict[G.getKeyByValue(dict,s)] = None
                    #and accept the new offer
                    dict[h] = s
                    
                    # print("eflif")
                    # print(h)
                    

                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1

                    
                    # print(iterations)
                    # print(dict)

                else: 

                    # print("else")
                    # print(h)

                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1

                    # print(iterations)
                    # print(dict)
            else: 
                
                # print("else2")
                # print(h)

                if (hospital == n-1):
                    hospital = 0
                else: hospital = hospital+1
                h = str(hospital)
                s = None
                #iterations = iterations + 1

                # print(iterations)
                # print(dict)

                
        else:
           return iterations 


                
                
        
def writeFiles(amt, k, n):
    n_this_time = n
    k = int(k)
    n = int(n)

    for i in range (amt):

        f= open("file" + str(i+1) + "_n=" + n_this_time + ".txt","w+") #filei_n=n.txt
        f.write(str(k) + "\n" + str(n) + "\n") 
        f.write("\n")
        
        #generate k permutations of lengths n - lists of students' rankings of hospitals
        for i in range(k):
            generateRandom(n,f)
            f.write("\n")
        f.write("\n")
        
        #generate k permutatios of lengths n - lists of hospitals' rankings of students
        for i in range(k):
            generateRandom(n,f)
            f.write("\n")
        f.write("\n")
    
        #assign preference lists to hospitals
        randomizer(n,k,f)
        
        f.write("\n")
        
        #assign preference lists to students
        randomizer(n,k,f)
        
        f.close()
#MAIN

if __name__ == "__main__" :
    
    total_rounds = 0
    #### WRITING FILE #######
    k, n = userPrompt() 
    amt = 10
    writeFiles(amt,k,n)

    

    for i in range (amt):

        dict = {} #stable matchings will be stored in this dictionary
        h_ranking_students = {} #hospitals are keys, and arrays with student rankings are values 
        s_ranking_hospitals = {} #hospitals are values, and arrays with student rankings are keys


        with open("file" + str(i+1) + "_n=" + str(n) + ".txt") as f:

            k = f.readline() #k number of possible preference lists for students and hospitals
            k = int(k) #convert to integer

            n = f.readline() #n number of students and hospitals
            n = int(n)

            i = 0
            while (i < n):
                key = i
                key = str(key)
                dict.update({key : None})
                h_ranking_students.update({key : None})
                s_ranking_hospitals.update({key : None})
                i = i + 1
            
            f.readline() #empty line
            h_lists = [] 
            readRankings(k,h_lists,f)
            f.readline() #empty line
            s_lists = []
            readRankings(k,s_lists,f)
            f.readline() #empty line
            line = f.readline()
            h_pref = line.split(" ")
            h_pref.pop()
            makeGSinput(n, h_pref, h_lists, h_ranking_students)
            
            
            line = f.readline()
            s_pref = line.split(" ")
            s_pref.pop()
            makeGSinput(n, s_pref.copy(), s_lists, s_ranking_hospitals) 

            #print(s_ranking_hospitals)
            #print(h_ranking_students)


            #iterations = 0
            hospital = 0
            rounds = (algorithm(dict, h_ranking_students, s_ranking_hospitals, n))
            print (rounds)

            total_rounds = total_rounds + rounds
    print(total_rounds)
    average = total_rounds / amt
    print(average)




        