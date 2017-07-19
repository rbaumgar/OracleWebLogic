# Oracle WebLogic Server with a sample application on OpenShift

Prerequsits:
- create the rhel7-weblogic image as described in the 12.2.1 directory

Create sampleapp image

    oc create -f https://raw.githubusercontent.com/rbaumgar/OracleWebLogic/master/sampleapp/sampleapp.yaml
    oc start-build sampleapp


Check log of the build
    
    oc logs sampleapp-1-build -f
    
If this is successful, you can create an application (with an empty domain), by
    
    oc new-app --name=mysample --image-stream=sampleapp:v1
    oc expose svc mysample --port=7001 -e ADMIN_PASSWORD=welcome1 -e DOMAIN_NAME=demo
    
With following command you will find the URL (under HOST/PORT)

    oc get route mysample

Open the URL with /sample ... Done!


When you are finished, you can remove the WebLogic Server with

    oc delete dc,svc,route mysample
    
Delete the image with

    oc delete is sampleapp
