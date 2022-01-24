
from random import randint
import numpy as np

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

def algorithm(dict, h_ranking_students, s_ranking_hospitals, iterations, hospital, n):
        if G.isInDictValues(dict, None):
            #print(dict)
            #print(h_ranking_students)
            #print(s_ranking_hospitals)
            h = str(hospital) #0
            s = dict.get(h)
            # if no student is assigned to a hospital and hospital hasn't proposed to this specific student yet
            if (s == None and len(G.getValueByKey(h_ranking_students, h)) != 0):
                #assign student to the first student on the hospital ranking list
                s = G.getFirstStudent(h_ranking_students, h)
                # if the student has no offers yet, accep this offer
                if G.isInDictValues(dict,s) == False:
                    #match student
                    dict[h] = s
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
                else:
                    iterations = iterations + 1
                    print(dict)
                    #print(dict)
                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    return algorithm(dict, h_ranking_students, s_ranking_hospitals, iterations,hospital,n)


                
                iterations = iterations + 1 #increment iterations
                print(dict)
                #print(dict)
                #increment hospital index and run again
                if (hospital == n-1):
                    hospital = 0
                else: hospital = hospital+1
                return algorithm(dict, h_ranking_students, s_ranking_hospitals, iterations,hospital,n)

            else:
            #increment hospital index and run algorithm again
                if (hospital == n-1):
                        hospital = 0
                else: hospital = hospital+1
                return algorithm(dict, h_ranking_students, s_ranking_hospitals, iterations,hospital,n)

        else: return iterations   

if __name__ == "__main__" :

    #You can test my Gale-Shapley!
    #Just enter any data in the following form:

    #Leave this dictionary as it is, 
    #stable matchings will be stored in this dictionary
    dict = {
        "0": None,
        "1": None,
        "2": None}
     
    #hospital rankings of students 
    #hospitals are keys, and arrays with student rankings are values 
    h_ranking_students = {
        "0": ["0", "1", "2"],
        "1": ["1", "0", "2"],
        "2": ["1", "0", "2"],
    } 
    #student rankings of hospitals
    #hospitals are values, and arrays with student rankings are key
    s_ranking_hospitals = {
        "0": ["2", "1", "0"],
        "1": ["2", "1", "0"],
        "2": ["2", "1", "0"]
    } 

    iterations = 0
    hospital = 0
    n = 3
    print(algorithm(dict, h_ranking_students, s_ranking_hospitals, iterations,hospital,n))


        
        
        