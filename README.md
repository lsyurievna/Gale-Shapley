This is my take on the implementation of Gale-Shapley algorithm that forms stable pairs between hiring hospitals and med-school students. 

####### PART 0 | HOW TO RUN THIS CODE 
(see bonus PART 0.1 if you want to see how to TEST this code)

1) Open GS.py file in any text editor that can compile Python (I wrote it in VSCode so it definetely will work)
2) Compile and run the code
3) You will be prompted to enter the values of k number of lists, n number of students and hospitals, and number of input files you want to create (the prompts are interactive so you won't get lost). Enter numbers as integers. I didn't add verification for the types of values you enter since I trust you are a responsible user.
4) That's it. Step 4 is to admire (I hope) the output, which is the average number 
of GS iterations for the specified k, n and number of input files.
5) Bonus step: give me an A in this course........... or not, A+ is okay too!

####### PART 0.1 | HOW TO TEST THIS CODE (BONUS)

1) Open GS_copy.py n any text editor that can compile Python (I wrote it in VSCode so it definetely will work)
2) Go to line 146. It is the main section, and is situated under my very humble:

########## MAIN ###########
########## TEST HERE #########

comment lines. 
3)Follow the instructions I provided in that section to create your custom input.
4)Compile and run the code. 
5) The output for this one is a stable matching dictionary state after every iteration along with the total number of iterations. 


######## BELOW I GIVE A GENERAL BASIC OUTLINE OF THE ENTIRE GS.PY FILE,  ########
######## YOU DON'T HAVE TO READ IT UNLESS YOU REALLY WANT TO             ########

####### PART 1 | INPUT FORMAT ##########

The first part of the program creates a specified number of input files in the following format:

2 // k number of preference lists that can be formed
3 // n number of students and hospitals

// k possible preference lists for hospitals (H)
0 1 2 // list 0 of hospitals ranking stuents
0 2 1 // list 1 of hospitals ranking stuents

// n possible reference lists for students (S)
1 0 2 // list 0 of students ranking hospitals
0 2 1 // list 1 of hospitals ranking stuents

//HI encoding which hospital has which preference list
1 0 1 // hospital 0 uses list 1, hospital 1 uses list 0, hospital 2 uses list 1
1 1 1 // student 0 uses list 1, student 1 uses list 1, student 2 uses list 1


####### PART2 | READING FILES: HOW IT WORKS ##########

The second part of the program reads the files, and for each file creates 3 dictionaries:

The first dictionary is where the stable pairs will be stored after Gale-Shapely algorithm inplementation

The second dictionary with students as keys and hospitals ranking arrays as values 

The third dictionary with hospitals as keys and students ranking arrays as values 


####### PART 3 | GS #######

Gale-Shapely is performed, returning the number of iterations after each file is processed


 
 
