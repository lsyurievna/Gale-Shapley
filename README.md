This is my take on the implementation of Gale-Shapley algorithm that forms stable pairs between hospitals and 
med-school students. 

####### PART 1 ##########

The first part of the program is creating a specified number of input files in the following format:

2 // k number of preference lists that can be formed
3 //n number of students and hospitals

// k possible preference lists for hospitals (H)
0 1 2 list 0 of hospitals ranking stuents, etc. 
0 2 1  

// n possible reference lists for students (S)
1 0 2 list 0 of students ranking hospitals, etc. 
0 2 1 

//HI encoding which hospital has which preference list
1 0 1 // hospital 0 uses list 1, hospital 1 uses list 0, hospital 2 uses list 1
1 1 1 // student 0 uses list 1, student 1 uses list 1, student 2 uses list 1



####### PART 2 ##########

The second part reads the files, and for each file creates 3 dictionaries:

The first dictionary is where the stable pairs will be stored after Gale-Shapely algorithm inplementation

The second dictionary with students as keys and hospitals ranking arrays as values 

The third dictionary with hospitals as keys and students ranking arrays as values 


####### PART 3 #######

Gale-Shapely is performed, printing the state after every iteration, and returning the number of iterations 

{'0': '0', '1': None, '2': None}
{'0': '0', '1': None, '2': None}
{'0': '0', '1': None, '2': None}
{'0': '0', '1': '1', '2': None}
{'0': '0', '1': '1', '2': '2'}

5

 
 
