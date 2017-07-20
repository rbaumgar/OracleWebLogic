# OracleWebLogic
Create OpenShift images for Oracle WebLogic Server(WLS)

This is based on the Docker examples provided by Oracle at https://github.com/oracle/docker-images.

But with one very significant difference:
The domain will be created when the container is started. 

This gives the advantage, that you need to create only on container per application and at the start time you can define 
DOMAIN_NAME, ADMIN_USER, ADMIN_PASSWORD, ... So you can run the **SAME** image in development, test and production. 
And this is one requirement for DevOps.


