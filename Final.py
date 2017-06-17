#############
# Aidan dill#
# Python A1 #
# 9/14/2016 #
#############
#calls main
#calls main
import tkinter
def main(): # defines main
    Dic={} # empty dictionary
    e = int(input("Enter a test score"))#asks user for input
    Dic['hey']= e # adds user input to dictionary
    if Dic['hey'] >= 90: #uses dictionary to calculate letter grade
        print("The grade is an A")
    elif Dic['hey'] <=89 and Dic['hey'] >=80:
        print("the  grade is a B")
    elif Dic['hey'] <=79 and Dic['hey'] >=70:
        print("the grade is a C")
    elif Dic['hey'] <=69 and Dic['hey'] >=60:
        print("the grade is a D")
    elif Dic['hey'] < 60:
        print("the grade is an F")#prints
    okf=better(e)
def better(e):
     while e <80: # while loop 
        print("Get a better grade!!")
        e = int(input("Did you get a better grade? enter the better grade now.(an 80 or above)"))
     else:
        print("congratulations, you have amazing grades! Here's a tkinter program that will calculate your average test score!")    

main()
class TestAvg():
    def __init__(self):
        #Creates the main window
        self.main_window = tkinter.Tk()
        #Creates five frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.test4_frame = tkinter.Frame(self.main_window)
        self.test5_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.labell_frame=tkinter.Frame(self.main_window)
        
        #explanation of program
        self.labell_label = tkinter.Label(self.labell_frame, \
                        text='Welcome to a program that calculates your average test score.')
        self.labell = tkinter.StringVar() # 
        self.rs_label = tkinter.Label(self.labell_frame, \
                                    textvariable=self.labell)
        self.rs_label.pack(side='top')
        self.labell_label.pack(side='top')
        
        # Create and pack widgets for test 1
        self.test1_label = tkinter.Label(self.test1_frame, \
                        text='Enter the score for your tests again to calculate average:')
        self.test1_entry = tkinter.Entry(self.test1_frame, \
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')
        
        #second test
        self.test2_label = tkinter.Label(self.test2_frame, \
                        text='Enter the score for your tests again to calculate average:')
        self.test2_entry = tkinter.Entry(self.test2_frame, \
                                         width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        
        #third
        self.test3_label = tkinter.Label(self.test3_frame, \
                        text='Enter the score for your tests again to calculate average:')
        self.test3_entry = tkinter.Entry(self.test3_frame, \
                                         width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')
        
        #fourth
        self.test4_label = tkinter.Label(self.test4_frame, \
                        text='Enter the score for your tests again to calculate average:')
        self.test4_entry = tkinter.Entry(self.test4_frame, \
                                         width=10)
        self.test4_label.pack(side='left')
        self.test4_entry.pack(side='left')

        
        #fifth
        self.test5_label = tkinter.Label(self.test5_frame, \
                        text='Enter the score for your tests again to calculate average:')
        self.test5_entry = tkinter.Entry(self.test5_frame, \
                                         width=10)
        self.test5_label.pack(side='left')
        self.test5_entry.pack(side='left')

        
        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.avg_frame, \
                        text='Average:')
        self.avg = tkinter.StringVar() # Updating avg
        self.avg_label = tkinter.Label(self.avg_frame, \
                                    textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')
        
        # quit and calc button
        self.calc_button = tkinter.Button(self.button_frame, \
                                     text='Average', \
                                     command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, \
                                text='Quit', \
                                command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')


        
        # Pack the frames.
        self.labell_frame.pack()
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.test4_frame.pack()
        self.test5_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()
        

        # Start the main loop.
        tkinter.mainloop()
        
    def calc_avg(self):
        # Get the five test scores and store them in variables.
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.test4 = float(self.test4_entry.get())
        self.test5 = float(self.test5_entry.get())
        # Calculate the average.
        self.average = (self.test1 + self.test2 + \
                        self.test3 + self.test4 + self.test5) / 5.0

        #updating in Stringvar

        self.avg.set(self.average)

# instance of TestAvg class.
test_avg = TestAvg()

















    
