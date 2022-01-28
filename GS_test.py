
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

def algorithm(dict, h_ranking_students, s_ranking_hospitals, n):

    iterations = 0
    hospital = 0
    h = str(hospital)
    s = None
   
    # if no student is assigned to a hospital and hospital hasn't proposed to this specific student yet
    while (s == None and len(G.getValueByKey(h_ranking_students, h)) != 0):
        # If there are students that are not matched (there is a value of None in dict)
        if G.isInDictValues(dict, None):
            # If for a specific chosen hospital there is no matching yet (we only count rounds when a hospital
            # proposes, if a hospital is already matched, we should skip it)
            if dict.get(h) == None:
                #assign student to the first student on the hospital ranking list
                s = G.getFirstStudent(h_ranking_students, h)
                # if the student has no offers yet, accep this offer
                if G.isInDictValues(dict,s) == False:
                    dict[h] = s
                    
                    #Increase the number of iteratons and go to the next hospital
                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1
                    print (iterations, ") ", dict)


                #if student prefers proposed hospital to matched hospital
                #(if current hospital index < proposed hospital index)
                elif G.getHospitalRank(s_ranking_hospitals, G.getKeyByValue(dict,s), s) > G.getHospitalRank(s_ranking_hospitals, h, s):
                    #cancel the student's previous arrangement
                    dict[G.getKeyByValue(dict,s)] = None
                    #and accept the new offer
                    dict[h] = s

                    #Increase the number of iteratons and go to the next hospital
                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1
                    print (iterations, ") ", dict)

                #A hospital proposes so we count this as an iteration
                #A student refuses however since they are happy with their
                #current matching, so we just return to the beginning of the algorithm
                else: 

                    #Increase the number of iteratons and go to the next hospital
                    if (hospital == n-1):
                        hospital = 0
                    else: hospital = hospital+1
                    h = str(hospital)
                    s = None
                    iterations = iterations + 1
                    print (iterations, ") ", dict)

            #The hospital is already matched : no increase in the number of iterations,
            #go to next hospital
            else: 
                
                #Increase the number of iteratons and go to the next hospital
                if (hospital == n-1):
                    hospital = 0
                else: hospital = hospital+1
                h = str(hospital)
                s = None

        #When everyone has been matched (no None values in the stable matchings dictionary)  
        else:
           return iterations

########## MAIN ###########
########## TEST HERE #########

if __name__ == "__main__" :

    #You can test my Gale-Shapley by specifying your own input file!
    #Just enter your data in the following format:

    #Leave this dictionary as it is, 
    #stable matchings will be stored in this dictionary
    dict = {
        "0": None,
        "1": None,
        "2": None}
     
    #This is hospitals' rankings of students 
    # Enter hospitals are keys, and arrays with student rankings as values
    h_ranking_students = {
        "0": ["0", "1", "2"], #for example, hospital "0" prefers students in the following order: "0", "1", "2"
        "1": ["1", "0", "2"],
        "2": ["1", "0", "2"],
    } 
    #This is students' rankings of hospitals
    #Enter students as keys and arrays with hospital rankings as values
    s_ranking_hospitals = {
        "0": ["2", "1", "0"], #for example, hospital "0" prefers students in the following order: "2", "1", "0"
        "1": ["2", "1", "0"],
        "2": ["2", "1", "0"]
    } 
    
    #Leave these as they are
    iterations = 0
    hospital = 0
    
    #Let the computer know how many students and hospitals (n) you are working with
    n = 3
    
    #The number of GS iterations will be printed along with 
    # the state of stable matchings dictionary after each step
    # Thank you for testing my GS!
    print("Number of GS iterations: ", algorithm(dict, h_ranking_students, s_ranking_hospitals, n))
    print("Thank you for testing my GS!")

        
        
        