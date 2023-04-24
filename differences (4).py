import filecmp
import os
#folder: the name, the size, number of files, location

#files: name, size, type, location, content

# class WhatIsTheDifference2:
#
#     def __init__(self, folder1, folder2):
#         self.folder1 = folder1
#         self.folder2 = folder2
#
#     def get_all_discrepancies(self):
#         folder1_content = self.get_folder_content(self.folder1) # ['/blabla1/foo.txt', '/blabla1']
#         folder2_content = self.get_folder_content(self.folder2) # ['/blabla1', '/blabla1/foo.txt', '/bar']
#
#         not_in_second_list = copy.copy(folder2_content)
#         differences_list = []
#         for x in folder1_content:
#             for y in not_in_second_list:
#                 if x not in not_in_second_list:
#                     differences_list.append(x)
#                 else:
#                     not_in_second_list.remove(y)
#                 break
#
#         differences_list.extend(not_in_second_list)
#         return differences_list

class WhatIsTheDifference:

    def __init__(self):

        self.pathToText1 = "C:/Users/TheodorZaharia/PycharmProjects/LearningPython/files_to_compare/New Text Document.txt"
        self.pathToText2 = "C:/Users/TheodorZaharia/PycharmProjects/LearningPython/files_to_compare/New Text Document (2).txt"
        self.pathToFolders = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython'

    def get_all_discrepancies(self, folder1, folder2, report_folder):
        folder1_content = self.get_folder_content(folder1) # ['/blabla1/foo.txt', '/blabla1']
        folder2_content = self.get_folder_content(folder2) # ['/blabla1', '/blabla1/foo.txt', '/bar']

        differences_list = []
        for x in folder1_content:
            if x not in folder2_content:
                #  differencesList = []
                # print(differencesList)
                differences_list.append(x)

        for x in folder2_content:
            if x not in folder1_content:
                #  differencesList = []
                # print(differencesList)
                differences_list.append(x)

        print(f"Different words in file: {differences_list} \n")

#        differences_list.extend(not_in_second_list)
        # Current results: ['/bar'] 
        # Expected results: ['A file or directory is missing: "/bar"', 
        # "File size of file %s and file %s are different", 
        # "Content of file %s and %s are different. Please, see report %s for discrepancies."]
        # every compare where file is A.txt exists on list1 and list2 will lead to a report being generated (if the files are different)



        with open('discrepancies.txt', 'w') as f:
            f.write(f"\nThe size of the folder /venv is: {self.get_size_folder()}")
            f.write(f"\n{self.differenceInFolder()}\n")
            if self.sizeInFile1() != self.sizeInFile2():
                f.write(f"File size of file {self.pathToText1} ({self.sizeInFile1()} bytes) and file {self.pathToText2} ({self.sizeInFile2()} bytes) are different.")
            else:
                with open('discrepancies.txt', 'w') as f:
                    f.write(f"File size of file {self.pathToText1} ({self.sizeInFile1()} bytes) and file {self.pathToText2} ({self.sizeInFile2()} bytes) is equal.")
        return differences_list


    def differenceInFile(self):
        text1=open(self.pathToText1)
        text2=open(self.pathToText2)
        read1 = text1.readlines()
        print(read1)
        read2 = text2.readlines()
        print(read2)

        differencesList = []
        for x in read1:
            if x not in read2:
              #  differencesList = []
                #print(differencesList)
                differencesList.append(x)

        # expected to be put into a file
        # enhance to cover the case where text2 has more content (which is not in text1)

        print(f"Different words in file: {differencesList} \n")

    #diffInFile = differenceInFile.WhatisIs
    def sizeInFile1(self):
        #I would like to make a for to get the size off all the files in the folder
        os.path.getsize(self.pathToText1)
        return os.stat(self.pathToText1).st_size
        # how can I print with the name of the file?
 #   print(f"\nThe size of the file is {sizeInFile()} bytes \n")

    def sizeInFile2(self):
        os.path.getsize(self.pathToText2)
        return os.stat(self.pathToText2).st_size

    def differenceInFolder(self):
        result = filecmp.dircmp("venv","random")
        report = result.report()
        return report



    #differenceInFolder()

    def get_size_folder(self):
        start_path = self.pathToFolders + "/venv"
        start_path2 = self.pathToFolders + "/random"
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)


        return total_size
        #how can I modify this to return sizes for both folders?
    def get_folder_content(self, start_path):
        content = []
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                content.append(fp)

        return content
        #how to print with the name from the start_path?
    #print(f"\nThe size of the folder is: {get_size()}", 'bytes')

if __name__ == '__main__':
    #folder_1 = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython/Random1'
    #folder_2 = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython/Random2'
    report_folder = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython/reports'
    #whatsdifferent = WhatIsTheDifference()
    #discrepancies = whatsdifferent.get_all_discrepancies(folder_1, folder_2, report_folder)
    #print(discrepancies)
    print("Aaaaaaaaaaaaaaaaaa")
    folder1 = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython/Random1'
    folder2 = 'C:/Users/TheodorZaharia/PycharmProjects/LearningPython/Random2'
    whatsdifferent = WhatIsTheDifference()
    discrepancies = whatsdifferent.get_all_discrepancies(folder1, folder2, report_folder)
    folderdiff= whatsdifferent.differenceInFolder()
    print(f"\nA file or directory is missing: {discrepancies}\n")

    print(f"\nThe size of the file is {whatsdifferent.sizeInFile1()} bytes \n")
    print(f"\nThe size of the folder is: {whatsdifferent.get_size_folder()}", 'bytes')
    print(whatsdifferent.differenceInFolder())


        #maybe we can input the address of the files so the program can tell us all the details we need with the folders and files

        #