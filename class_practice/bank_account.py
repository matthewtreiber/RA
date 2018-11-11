# this class represents a bank account
# we will use this object to be a part of another object called bank


# create class
class student:
    # create class methods
    # init function
    def __init__(self, first, last, id):
        # create class attributes and set some of them to the values passed into function
        self.name_last = last
        self.name_first = first
        self.name_full = first + ' ' + last
        self.student_id = id
        self.year = None
        self.semester_GPA = 0
        self.class_dict = {} # holds current classes and numeric grade in class {"english": 89, "math": 71, ...}

    # for each method/function created, make a function header

    # create methods/functions
    #------------------------------------------------------------------------------------------------------------------#
    #---------------------- these are GET fucntions, they give you the attributes of the object -----------------------#
    def get_first_name(self):

    def get_last_name(self):

    def get_name(self):

    def get_studnet_id(self):

    def get_year(self):

    def get_semester_GPA(self):

    #------------------------------------------------------------------------------------------------------------------#
    # ------------------------- these functions MODIFY/PUT data into the objects attributes ---------------------------#

    def put_year(self, current_year):

    def add_class(self, class_name, grade):

    def get_class_grade(self, class_name):

    def change_class_grade(self, class_name, grade):

    def calc_GPA(self):



