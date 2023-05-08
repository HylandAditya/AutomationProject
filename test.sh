#!/usr/bin/env sh
#echo "Hello World"
#for (( i=60; i>0; i--)); do
#  sleep 1 &
#  printf "  $i \r"
#  wait
#done

echo "Building alfresco-enterprise-repo..."
cd C:/ags2/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api
echo $?
mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false
echo $?
cp C:/ags2/alfresco-enterprise-repo/amps/ags/rm-automation/rm-automation-enterprise-rest-api/target/surefire-reports/emailable-report.html C:/Users/ashiva/Downloads
echo $?
mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api2.xml -Dskip.automationtests=false
echo $?
#mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api3.xml -Dskip.automationtests=false
#mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api4.xml -Dskip.automationtests=false
#mvn clean test -Dsurefire.suiteXmlFiles=src/test/resources/enterprise-rest-api5.xml -Dskip.automationtests=false
popd