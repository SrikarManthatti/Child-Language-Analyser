"""
Created by : Manthatti Srikar
Created time : 9th October 2018
Program name: 29803306_task3.py
Description: This python program will import the task2 DataAnalyze function.
            importing os module to read the files in a particular function
            importing numpy module to calculate the averages of the function and also to arange the values
            importing matplotlib to represent the values in the plot
"""


from task2_29803306 import DataAnalyze
import os
import numpy
import matplotlib.pyplot as m



SLI_file_path="/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-SLI/"       #this varibale holds the folder location of SLI
TD_file_dest = "/Users/srikarmanthatti/Desktop/FIT9133/Assignment_2/ENNI Dataset/Cleaned-TD/"       #this variable holds the folder location of TD

class Visualize:
    """This initiator function is used to initialize the few variables. This init function will take two arguments, one is self which is th eobject itself.
    The other argument is the datalist which will be returned in the DataAnalyse call of task2.py module"""

    def __init__(self,datalist):
        self.datalist=datalist
        self.file = ''
        self.vocab_avg = 0
        self.words_repeat_avg = 0
        self.words_retrace_avg = 0
        self.grammar_errors_avg = 0
        self.pauses_avg = 0
        self.statements_avg = 0

    """This compute_averages will be used to calculate the averages. The datalist will be used to calculate the averages"""

    def compute_averages(self):
        for data in self.datalist:  #in this for loop, each data in the datalist will be sent in the function and will be used to calculate the average

            """Since the return statement in the function will return the filename, statements_avg, vocabavg, words_repeat_avg, words_retrace_avg, grammar_errors_avg, Pauses_avg respectively"""

            self.file=data[0]
            self.statements_avg +=data[1]
            self.vocab_avg +=data[2]
            self.words_repeat_avg +=data[3]
            self.words_retrace_avg +=data[4]
            self.grammar_errors_avg +=data[5]
            self.pauses_avg +=data[6]
        self.statements_avg = self.statements_avg / 10
        self.vocab_avg += self.vocab_avg/10
        self.words_repeat_avg += self.words_repeat_avg/10
        self.words_retrace_avg += self.words_retrace_avg/10
        self.grammar_errors_avg += self.grammar_errors_avg/10
        self.pauses_avg += self.pauses_avg/10



    """The below visualise_statistics function will be used to plot the bar graph"""

    def visualise_statistics(self):
        names=['statements','vocabulary','repeats','retraces','grammar errors','pauses']  #in the names list, the order which will be stored is the same as the return values
        values=[self.statements_avg,self.vocab_avg,self.words_repeat_avg,self.words_retrace_avg,self.grammar_errors_avg,self.pauses_avg]
        i = numpy.arange(len(names))
        figure, axis = m.subplots()
        axis.bar(i,values,color="red")
        m.xlabel("Statistics", fontsize=10)
        m.ylabel("Average values", fontsize=10)
        axis.set_xticks(i)
        axis.set_xticklabels(names,rotation=5)
        m.title(Legend)
        m.show()



sli_avg_values = []         # this list will be used to store the average values of the SLI average values
td_avg_values = []             # this list will be used to store the average values of the TD average values
SLI_legend="SLI bar graph"
TD_legend="TD bar graph"
obj=DataAnalyze()           #creating the object for the task2 class to call the function

for sli_file in os.listdir(SLI_file_path):  # this for loop will be used to iterate through the files in the SLI folder
    if not sli_file.startswith( '.' ):      #this if loop will be used to ignore .DSstore file
        initial_file=SLI_file_path+sli_file
        data=obj.analyse_script(initial_file)   #here we are calling the analyse_script fuction and storing the return values into data list
        sli_avg_values.append(data)

for td_file in os.listdir(TD_file_dest):     # this for loop will be used to iterate through the files in the TD folder
    if not td_file.startswith( '.' ):        ##this if loop will be used to ignore .DSstore file
        initial_file=TD_file_dest+td_file
        data=obj.analyse_script(initial_file)   #here we are calling the analyse_script fuction and storing the return values into data list
        td_avg_values.append(data)

Legend="SLI Statistics"
obj2=Visualize(sli_avg_values)  #creating the object for Visualize class for SLI values
obj2.compute_averages()
obj2.visualise_statistics()

Legend="TD Statistics"

obj3=Visualize(td_avg_values)   #creating the object for Visualize class for TD values
obj3.compute_averages()
obj3.visualise_statistics()

