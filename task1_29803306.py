"""
Created by : Srikar Manthatti
Created time : 7th October 2018 14:20:00
program_name : 29803306_task1.py
Description: This python program will be used to clean the ENNI datasets. These cleaned ENNI datasets will be used for further data analysis
"""



"""
Importing os module to iterate through the files in a particular folder
Importing shutil module to remove a middle directory

"""
import os
import shutil

"""
Here we are defining the paths where the raw data sets and the cleaned datasets will be stored
"""


SLI_file_path="/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/SLI/"
SLI_file_dest="/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-SLI/"
Middlefolder="/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Middlefolder/"
TD_file_path = "/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/TD/"
TD_file_dest = "/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-TD/"



"""
The below first cleaning function is used to extract the data from the raw datasets and will extract only those statments starting with *CHI
This function accepts two paths as the arguments.
frompath:- this argument will contain the location of the raw data sets
topath:- after extracting the statments starting with only *CHI will be stored in the respective file names in topath location.
As we have two types  of datasets SLI and TD, after cleaning the SLI dataset the cleaned files will be stored in the Middle folder. Again while going to the TD folder a check 
will be done and with the help of shutil.rmtree we will remove the Middlefolder and again will created it.  
"""


def first_cleaning(frompath,topath):
    if os.path.exists(Middlefolder):    # we are checking for the existance of middle folder
        shutil.rmtree(Middlefolder)     # if exists then we will remove the middlefolder
        os.makedirs(Middlefolder)       # after removing the middle folder again we are creating it.
    else:
        os.makedirs(Middlefolder)
    for file in os.listdir(frompath):   #this part of for loop will be used to extract files from the source location
        intial_file=frompath+file
        #print("----------------------------------------------------------------------------",intial_file)
        destination_file=Middlefolder+file
        with open(intial_file, encoding="utf8", errors='ignore') as f:
            with open(destination_file,'w') as f1:      #opening each and every file in the source location
                #for line in f:
                line=f.readlines()
                line=[x.strip('\n') for x in line]      #stripping each lines in the file and storing in the line list
                i=0
                while i < len( line ):
                    #print( i )

                    if '*CHI' in line[i]:               #in the line list if *CHI in the line list then extract the line and store in the new file at destination folder
                        #print( line[i] )

                        f1.writelines( line[i] )
                        f1.writelines( '\n' )
                        i += 1
                        # print(line[i])
                        if '\t' in line[i] and '%mor' not in line[i]: #if the next line in the list after reading *CHI is starting with a \t then it will also be read
                            #print( line[i] )
                            f1.writelines( line[i] )
                            f1.writelines( '\n' )

                    i += 1

                #print( "completed" )
                f1.close()
                f.close()
    second_cleaning(Middlefolder,topath);           #after cleaning the *CHI data and storing in the destination folder  we will call the second_cleaning function

""" 
The below second cleaning function is used to extract the data from the middle folder and will remove the certain pattersn from the data for cleaning
This function accepts two paths as the arguments.
frompath:- this argument will contain the location of the first stage cleaned files
topath:- By considering certain patterns these files will be cleaned
"""

def second_cleaning(frompath,topath):
    for file in os.listdir(frompath):
        initial_file=frompath+file
        destination_file=topath+file
        #print(destination_file)
        with open(initial_file,'r') as f:               #we open the first stage cleaned files here
            with open( destination_file, 'w' ) as f1:   #we open the destination file and write data to them
                for line1 in f:                         #reading the each line in the file
                    line=line1
                    words=line.split()                  #lines will splitted into words list
                    #print(words)
                    for j in range(len(words)):         #for each if we have *CHI in the statement, then replacing the *chi with null value
                        if words[j]=='*CHI:':
                            words[j]=''

                        elif words[j].startswith('['):  #if any word in the list is starting with the '[' the we need remove those expect the following [//], [/], [*
                            if words[j] != '[//]' and words[j] !='[/]' and words[j] !='[*':
                                print("[*")
                                words[j]=''
                        elif (words[j].endswith(']') and words[j]!='m:+ed]'):
                            print("ends with ]")
                            words[j]=''
                        elif (words[j].startswith('<')): #Retaining those words that have either ‘<’ as prefix or ‘>’ as suffix but these two symbols are removed
                            if (words[j].endswith('>')):
                                letter = list(words[j])
                                letter.pop(len(letter) - 1)
                                poped_str=letter.pop(0)
                                print("popped str is:", poped_str)
                                words[j] = ''.join(str(k) for k in letter) #after cleanign the < > we are again joining the word to the list
                            else:
                                letter = list(words[j])
                                letter.pop(0)
                                words[j] = ''.join(str(k) for k in letter)
                        elif ('(' in words[j]):         #Retain those words that have either ‘(’ as prefix or ‘)’ as suffix but these two symbols are removed
                            print("in curly braclets")
                            if (words[j] != '(.)'):
                                letter = list(words[j])
                                for k in range(0,len(letter)):
                                    if letter[k] == '(':
                                        letter[k] = ''
                                    elif letter[k] == ')':
                                        letter[k] = ''
                                    words[j]= ''.join(str(l) for l in letter) #after cleanign the < > we are again joining the word to the list
                        elif (words[j].startswith('&') or words[j].startswith("+")): # replacing  the words which are starting with & anf + in the list
                            words[j] = ''
                        elif (words[j].endswith('>')):
                            letter = list(words[j])
                            letter.pop(len(letter) - 1)
                            words[j] = ''.join(str(k) for k in letter)
                        else:
                            print("its a word")
                    line = ' '.join(str(k) for k in words) # after cleaning the whole data we are again joining the list
                    line += '\n'
                    #print("after line are:", line)
                    f1.writelines(line)  # wiritng the final line to the file




first_cleaning(SLI_file_path,SLI_file_dest)
first_cleaning(TD_file_path,TD_file_dest)






