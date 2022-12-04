"""
 Title:         Progressor
 Description:   For visualising the steps of a process
 Author:        Janzen Choi

"""

# Libraries
import time, os, sys, atexit
import printer

# Constants
START_INDEX     = 1
MIN_PADDING     = 5
INIT_LENGTH     = 30
END_PAD_CHAR    = "."

# For visualising the progress of a process
class Progressor:

    # Constructor
    def __init__(self, fancy=False, title="", verbose=False):

        # Initialise inputs
        self.fancy          = fancy
        self.final_message  = title
        self.verbose        = verbose
        
        # Initialise auxiliary
        self.message_list = []
        self.start_time = time.time()
        self.start_time_string = time.strftime("%y/%m/%d, %H:%M:%S", time.localtime(self.start_time))
        atexit.register(self.__finish__)

    # Print caller depending on fanciness
    def __print__(self, message="", options=[], newline=True):
        if self.fancy:
            printer.print(message, options, newline)
        else:
            end = "\n" if newline else ""
            print(message, end=end)

    # Displays all the messages
    def __display__(self):
        
        # Get auxiliary values
        max_length = max([len(message["message"]) for message in self.message_list])
        max_length = max(INIT_LENGTH, max_length)
        max_index_length = len(str(len(self.message_list)))

        # Print the title
        self.__print__(f"\n  Progress Report ({self.start_time_string}):\n", ["orange"])

        # Print the components
        for i in range(len(self.message_list)):

            # Extract message and duration
            message = self.message_list[i]["message"]
            duration = self.message_list[i]["duration"]
            complete = self.message_list[i]["complete"]

            # Print index and message
            padding_start = (2 + max_index_length - len(str(i+1))) * " "
            padding_end = (MIN_PADDING + max_length - len(message)) * END_PAD_CHAR
            self.__print__(f"{padding_start} {i+1}) ", ["orange"], False)
            self.__print__(f"{message} {padding_end} ", [], False)
            
            # Print progress status
            if complete:
                self.__print__("[Complete] ", ["l_green"], False)
                self.__print__(f"({duration}s)")
            else:
                self.__print__("[Ongoing]", ["l_red"])
                self.__print__("")
    
    # When closing, display end message
    def __finish__(self):

        # If an error was raised, then sys.last_value exists, and leave
        try:
            sys.last_value
            return
        except AttributeError:
            pass

        # Display progress
        self.message_list[-1]["duration"] = round(time.time() - self.curr_time, 2)
        self.message_list[-1]["complete"] = True
        if not self.verbose:
            os.system('cls' if os.name == 'nt' else 'clear')
        self.__display__()

        # Display final message
        total_duration = round(time.time() - self.start_time, 2)
        final_message = f" ({self.final_message})" if self.final_message != "" else ""
        self.__print__(f"\n  Finished in {total_duration}s{final_message}!\n", ["orange"])

    # Adds a component to the process
    def add(self, message):

        # Update duration if not first
        if len(self.message_list) > 0:
            self.message_list[-1]["duration"] = round(time.time() - self.curr_time, 2)
            self.message_list[-1]["complete"] = True
        self.curr_time = time.time()

        # Add message
        self.message_list.append({
            "message": message,
            "duration": 0,
            "complete": False,
        })

        # Clear and display
        if not self.verbose:
            os.system('cls' if os.name == 'nt' else 'clear')
        self.__display__()