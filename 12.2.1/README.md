# Oracle WebLogic Server on OpenShift

Prerequsits:
- download WebLogic software from Oracle
- copy download to your web server. If you don't have one use Caddy Server, see https://github.com/rbaumgar/rhel-caddy
- create RHEL-OracleJDK image, see https://github.com/rbaumgar/rhel-OracleJDK/

Create Oracle WebLogic image

    oc create -f https://raw.githubusercontent.com/rbaumgar/OracleWebLogic/master/12.2.1/weblogic.yaml
    oc start-build rhel7-weblogic -e FMW_BASEURL=http://caddy-abc.192.168.122.111.xip.io -e FMW_VERSION=12.2.1.2.0 -e FMW_QUICK=""

    FMW_BASEURL is the URL of your web server(Caddy)
    FMW_VERSION is the exact version of the Oracle WebLogic download, e.g. fmw_12.2.1.2.0_wls_Disk1_1of1.zip -> 12.2.1.2.0
    FMW_QUICK is true if you want to use the quick installer, e.g. fmw_12.2.1.2.0_wls_quick_Disk1_1of1.zip

Check log of the build
    
    oc log rhel7-weblogic-2-build -f
    
If this is successful, you can create an application (with an empty domain), by
    
    oc new-app --name=mywls --image-stream=rhel7-weblogic:v12.2.1
    oc expose svc mywls --port=7001 -e ADMIN_PASSWORD=welcome1
    
With following command you will find the URL (under HOST/PORT)

    oc get route mywls

Open the URL with /console ... Done!


When you are finished, you can remove the WebLogic Server with

    oc delete dc,svc,route mywls
    
Delete the image with
    oc delete is rhel7-weblogic
