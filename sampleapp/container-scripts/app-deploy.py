# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
#
# WLST Offline for deploying an application under APP_NAME packaged in APP_PKG_FILE located in APP_PKG_LOCATION
# It will read the domain under DOMAIN_HOME by default
#
# author: Bruno Borges <bruno.borges@oracle.com>
# since: December, 2015
#
# updated by Robert Baumgartner <robert.baumgartner@redhat.com>
#
import os

# Deployment Information 
domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
admin_name   = os.environ.get('ADMIN_NAME', 'AdminServer')
app_name     = os.environ.get('APP_NAME', 'sample')
app_file     = os.environ.get('APP_FILE', 'sample.war')
app_dir      = os.environ.get('APP_DIR', '/u01/oracle')
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

print('domain_name     : [%s]' % domain_name);
print('admin_name      : [%s]' % admin_name);
print('app_name        : [%s]' % app_name);
print('app_file        : [%s]' % app_file);
print('app_dir         : [%s]' % app_dir);
print('cluster_name    : [%s]' % cluster_name);

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Application
# ==================
cd('/')
app = create(appname, 'AppDeployment')
app.setSourcePath(appdir + '/' + apppkg)
app.setStagingMode('nostage')
 
# Assign application to AdminServer
# =================================
assign('AppDeployment', appname, 'Target', admin_name)
# assign('AppDeployment', appname, 'Target', cluster_name)

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
