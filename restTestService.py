import os
import shutil
"""
SETUP
"""
#DELETE EXISTING SURFIRE REPORT
directory = "surefire-reports"
# Parent Directory
parent = "C:/ags2/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/"
# Path
path = os.path.join(parent, directory)
shutil.rmtree(path, ignore_errors=True)
#CHANGE DIRECTORY TO POINT TO REST API ROOT
os.chdir(r"C:\ags2\alfresco-enterprise-repo\amps\ags\rm-automation\rm-automation-enterprise-rest-api")
cwd = os.getcwd()
print("Current working directory is:", cwd)

"""
RUN API TEST AND ASSERT RETURN CODE
"""
#RUN TEST
return_code = os.system('mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false')
print("RETURN CODE IS:", return_code)
# #ASSERT STATUS CODE
if(return_code==1):
    #CHECK IF SURFIRE ISGENERATED
    if(os.path.isdir(path)):
        print("SURFIRE REPORT IS GENERATED")
        #DELETE IF DIRECTORY ALREADY PRESENT
        src_dir = path
        path="C:/Users/ashiva/Downloads/REPORT/API4"
        shutil.rmtree(path, ignore_errors=True)
        # move surfire report contents to Downloads
        # path to source directory


        # # path to destination directory
        dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'

        # getting all the files in the source directory
        #files = os.listdir(path)

        shutil.copytree(src_dir, dest_dir)
        print("COPIED SURFIRE CONTENT TO DESTINATION")
        # SEND TO SLACK
    else:
        print("ENVIRONMENT ISSUE TRY RUNNING AGAIN")
        #RE-RUN TEST
        #os.path.isdir(path).
else:
    print("TEST WAS SUCCESSFUL")
    # DELETE IF DIRECTORY ALREADY PRESENT
    src_dir = path
    path = "C:/Users/ashiva/Downloads/REPORT/API4"
    shutil.rmtree(path, ignore_errors=True)
    # move surfire report contents to Downloads
    # path to source directory

    # # path to destination directory
    dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'

    # getting all the files in the source directory
    # files = os.listdir(path)

    shutil.copytree(src_dir, dest_dir)

    # SEND TO SLACK

