import os
import shutil
import logging

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
#ASSERT STATUS CODE
if(return_code==1):
    #CHECK IF SURFIRE ISGENERATED
    if(os.path.isdir(path)):
        # move surfire report contents to Downloads
        # path to source directory
        src_dir = 'fol1'

        # path to destination directory
        dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'

        # getting all the files in the source directory
        files = os.listdir(path)

        shutil.copytree(path, dest_dir)

        # SEND TO SLACK
    else:
        print("ENVIRONMENT ISSUE TRY RIUNNING AGAIN")
        #RE-RUN TEST
        #os.path.isdir(path)
