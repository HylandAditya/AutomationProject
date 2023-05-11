import shutil
import slack
import os
from dotenv import load_dotenv
from slack.errors import SlackApiError

class testAPI():
    directory = str(input("ENTER DIRECTORY WHERE AGS IS CLONED:"))
    env_path = ".env"
    load_dotenv(env_path)
    client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])
    count=1
    def delete_existingsurfire(self):
        # #CHECK IF DIRECTORY EXISTS IN C DRIVE
        path="C:/"+self.directory+"/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports"
        shutil.rmtree(path, ignore_errors=True)
    def change_directory(self):
        path=fr"C:\{self.directory}\alfresco-enterprise-repo\amps\ags\rm-automation\rm-automation-enterprise-rest-api"
        os.chdir(path)
        cwd = os.getcwd()
        print("Current working directory is:", cwd)

    def run_test_api4(self):

        return_code = os.system('mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false')
        print("RETURN CODE IS:", return_code)
        path = "C:/" + self.directory + "/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports"
        if (return_code == 1):
            # CHECK IF SURFIRE ISGENERATED
            print("RETURNED 1")
            if (os.path.isdir(path)):
                print("SURFIRE REPORT IS GENERATED")
                # DELETE IF DIRECTORY ALREADY PRESENT
                src_dir = path
                path = "C:/Users/ashiva/Downloads/REPORT/API4"
                shutil.rmtree(path, ignore_errors=True)
                # move surfire report contents to Downloads
                dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API4'
                # getting all the files in the source directory
                # files = os.listdir(path)
                shutil.copytree(src_dir, dest_dir)
                print("COPIED SURFIRE CONTENT TO DESTINATION")
                # SEND TO SLACK
                self.UloadFileToSlack(4)
                count=1
            else:
                print("ENVIRONMENT ISSUE TRY RUNNING AGAIN")
                self.count +=1
                if(self.count<=3):
                    print("TEST RUNNING FOR :",self.count," time")
                    self.run_test_api4()
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
            #SEND FILE TO SLACK
            self.UloadFileToSlack(4)
            print("FILE UPLOAD TO SLACK SUCCESSFUL")

    def run_test_api5(self):

        return_code = os.system(
            'mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api5.xml -Dskip.automationtests=false')
        print("RETURN CODE IS:", return_code)
        path = "C:/" + self.directory + "/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports"
        if (return_code == 1):
            # CHECK IF SURFIRE ISGENERATED
            print("RETURNED 1")
            if (os.path.isdir(path)):
                print("SURFIRE REPORT IS GENERATED")
                # DELETE IF DIRECTORY ALREADY PRESENT IN DOWNLOADS
                src_dir = path
                path = "C:/Users/ashiva/Downloads/REPORT/API5"
                shutil.rmtree(path, ignore_errors=True)
                # move surfire report contents to Downloads
                dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API5'
                # getting all the files in the source directory
                # files = os.listdir(path)
                shutil.copytree(src_dir, dest_dir)
                print("COPIED SURFIRE CONTENT TO DESTINATION")
                # SEND TO SLACK
                self.UloadFileToSlack(5)
            else:
                print("ENVIRONMENT ISSUE TRY RUNNING AGAIN")
                self.count += 1
                if (self.count <= 3):
                    print("TEST RUNNING FOR :", self.count, " time")
                    self.run_test_api5()
        else:
            print("TEST WAS SUCCESSFUL")
            # DELETE IF DIRECTORY ALREADY PRESENT
            src_dir = path
            path = "C:/Users/ashiva/Downloads/REPORT/API5"
            shutil.rmtree(path, ignore_errors=True)
            # move surfire report contents to Downloads
            # path to source directory
            # # path to destination directory
            dest_dir = 'C:/Users/ashiva/Downloads/REPORT/API5'
            # getting all the files in the source directory
            # files = os.listdir(path)
            shutil.copytree(src_dir, dest_dir)
            # SEND FILE TO SLACK
            self.UloadFileToSlack(5)
            print("FILE UPLOAD TO SLACK SUCCESSFUL")

    def UloadFileToSlack(self,api_no):
        # env_path = ".env"
        # load_dotenv(env_path)
        # client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])

        if(api_no==4):
            self.client.chat_postMessage(channel="#hackathontest",
                                         text="TEST REPORT FOR API 4")
            try:
                filepath = "C:/Users/ashiva/Downloads/REPORT/API4/emailable-report.html"
                response = self.client.files_upload(channels='#hackathontest', file=filepath)
                assert response["file"]  # the uploaded file
            except SlackApiError as e:
                assert e.response["ok"] is False
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
        elif(api_no==5):
            self.client.chat_postMessage(channel="#hackathontest",
                                         text="TEST REPORT FOR API 5")
            try:
                filepath = "C:/Users/ashiva/Downloads/REPORT/API5/emailable-report.html"
                response = self.client.files_upload(channels='#hackathontest', file=filepath)
                assert response["file"]  # the uploaded file
            except SlackApiError as e:
                assert e.response["ok"] is False
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
        else:
            print("PROVIDE CORRECT API NUMBER")


o=testAPI()
o.delete_existingsurfire()
o.change_directory()
o.run_test_api4()
o.run_test_api5()
