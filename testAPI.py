import os
import shutil
class testAPI():
    directory = str(input("ENTER DIRECTORY"))
    def delete_existingsurfire(self):
        # #CHECK IF DIRECTORY EXISTS IN C DRIVE
        path="C:/"+self.directory+"/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports"
        shutil.rmtree(path, ignore_errors=True)
    def change_directory(self):
        path=fr"C:\{self.directory}\alfresco-enterprise-repo\amps\ags\rm-automation\rm-automation-enterprise-rest-api"
        os.chdir(path)
        cwd = os.getcwd()
        print("Current working directory is:", cwd)

    def run_test(self):
        api_number=4
        return_code = os.system('mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false')
        print("RETURN CODE IS:", return_code)
        #SEND REPORT TO SLACK
        return return_code

    # def evaluate_return_value(self,return_value):
    #     return_code=return_value
    #
    #     if (return_code == 1):
    #         # CHECK IF SURFIRE ISGENERATED
    #         if (os.path.isdir(path)):
    #             print("SURFIRE REPORT IS GENERATED")
    #             # DELETE IF DIRECTORY ALREADY PRESENT
    #             src_dir = path
    #             path = "C:/Users/ashiva/Downloads/REPORT/API4"
    #             shutil.rmtree(path, ignore_errors=True)
    #             # move surfire report contents to Downloads
    #             # path to source directory
    #             # # path to destination directory
    #             dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'
    #
    #             # getting all the files in the source directory
    #             # files = os.listdir(path)
    #
    #             shutil.copytree(src_dir, dest_dir)
    #             print("COPIED SURFIRE CONTENT TO DESTINATION")
    #             # SEND TO SLACK
    #         else:
    #             print("ENVIRONMENT ISSUE TRY RUNNING AGAIN")
    #             # RE-RUN TEST
    #             # os.path.isdir(path).
    #     else:
    #         print("TEST WAS SUCCESSFUL")
    #         path = "C:/" + self.directory + "/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports"
    #         # DELETE IF DIRECTORY ALREADY PRESENT
    #         src_dir = path
    #         path = "C:/Users/ashiva/Downloads/REPORT/API4"
    #         shutil.rmtree(path, ignore_errors=True)
    #         # move surfire report contents to Downloads
    #         # path to source directory
    #
    #         # # path to destination directory
    #         dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'
    #
    #         # getting all the files in the source directory
    #         # files = os.listdir(path)
    #
    #         shutil.copytree(src_dir, dest_dir)


o=testAPI()
o.delete_existingsurfire()
o.change_directory()
return_value=o.run_test()
print(return_value)
#o.evaluate_return_value(return_value)
