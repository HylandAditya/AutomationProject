import os
import shutil
os.chdir(r"C:\ags2\alfresco-enterprise-repo\amps\ags\rm-automation\rm-automation-enterprise-rest-api")
cwd = os.getcwd()
print("Current working directory is:", cwd)
return_code = os.system('mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false')
print("RETURN CODE IS:", return_code)
assert return_code==0 #returns 1 if failure

if return_code==0:
    print("TEST SUCCESS")
    # path to source directory
    src_dir = 'C:\ACS\alfresco-enterprise-repo\amps\ags\rm-automation\rm-automation-enterprise-rest-api\target\surefire-reports'
    # path to destination directory
    dest_dir = 'C:\Users\ashiva\PycharmProjects\hackathonProject'

    # getting all the files in the source directory
    files = os.listdir(src_dir)

    shutil.copytree(src_dir, dest_dir)





