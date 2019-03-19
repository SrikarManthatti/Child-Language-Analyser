"""
Created by : Manthatti Srikar
Created time : 9th October 2018
Program name: 29803306_task2.py
Description: This python program is used to calculate the number of errors, no of repeating  numbers, number of retracing numbers, size of vocabulary and etc.,
"""

import os
class DataAnalyze:

    """size_of_vocabulary_list = []
    len_of_transcript_list = []
    repeating_words_list = []
    retracting_words_list = []
    grammatical_errors_list = []
    pauses_list = []"""
    """This initiator function is used to initialize the few variables"""
    def __init__(self):
        self.file=''
        self.len_of_transcript=0
        self.size_of_vocabulary=0
        self.repeating_words=0
        self.retracing_words=0
        self.grammatical_errors=0
        self.pauses=0
        #self.results=[]
    """This string function is an override function which will return the inbuilt return string"""
    def __str__(self):
        return """
        Name of the file -- %s
        length of the transcript is -- %d
        Size of the vocabulary is -- %d
        Number of repetition for certain words or phrases —- %d
        Number of retracing for certain words or phrases —- %d
        Number of grammatical errors detected —- %d
        Number of pauses made —- %d"""%(self.file,self.len_of_transcript,self.size_of_vocabulary, self.repeating_words,self.retracing_words,self.grammatical_errors,self.pauses)
        #return self.results

    """The analyse script is used to find the number of len-of_transcipt, repeating_words, retracing_words, grammatical_errors, pauses. 
    The function will take two arguments, one is self which represents the object and the cleaned_file which will represent the file which has been cleaned in taks 1"""

    def analyse_script(self,cleaned_file):
        self.file=cleaned_file
        #print("now reading", self.file)
        with open(self.file,  encoding="utf8", errors='ignore') as f:
            for line in f:
                words=line.split()
                myset=set(words)
                self.size_of_vocabulary+=len(myset)

                for i in range(len(words)):
                    if words[i]=='.' or words[i]=='?' or words[i]=='!':
                        self.len_of_transcript +=1

                    elif words[i]=='[/]':
                        self.repeating_words +=1

                    elif words[i]=='[//]':
                        self.retracing_words +=1

                    elif words[i]=='[*':
                        self.grammatical_errors +=1

                    elif words[i]=='(.)':
                        self.pauses +=1

        """DataAnalyze.size_of_vocabulary_list.append( self.size_of_vocabulary )
        DataAnalyze.len_of_transcript_list.append( self.len_of_transcript )
        DataAnalyze.repeating_words_list.append( self.repeating_words )
        DataAnalyze.retracting_words_list.append( self.retracing_words )
        DataAnalyze.grammatical_errors_list.append( self.grammatical_errors )
        DataAnalyze.pauses_list.append( self.pauses )"""
        return [self.file, self.len_of_transcript,self.size_of_vocabulary,self.repeating_words,self.retracing_words,self.grammatical_errors,self.pauses]


    """The count class will create the objects of analyse class and will call the analyse_script fucntion to calculate the required variables."""

class Count:
    if __name__ == '__main__':
        SLI_file_path="/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-SLI/"
        TD_file_dest = "/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-TD/"
        analyse_obj_sli=DataAnalyze() #creating the object to send SLI files as an argument to the analyse_script fucntion
        analyse_obj_td = DataAnalyze() #creating the object to send TD files as an argument to the analyse_script fucntion
        for sli_file in os.listdir(SLI_file_path): #accessign the SLI files with the help of OS module and passign them for further processing
            if not sli_file.startswith('.'):
                sli_path=SLI_file_path+sli_file
                analyse_obj_sli.analyse_script(sli_path)
            print(analyse_obj_sli)
        #print(DataAnalyze.len_of_transcript_list)
        for td_file in os.listdir(TD_file_dest):  #accessign the TD files with the help of OS module and passign them for further processing
            if not td_file.startswith('.'):
                td_path=TD_file_dest+td_file
                analyse_obj_td.analyse_script(td_path)
            print(analyse_obj_td)
        #print( DataAnalyze.len_of_transcript_list )




