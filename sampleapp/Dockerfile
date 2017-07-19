
# Pull base image
# ---------------
FROM rhel7-weblogic

# Maintainer
# ----------
MAINTAINER Robert Baumgartner <robert.baumgartner@redhat.com>

# Define variables
ENV APP_NAME="sample" \
    APP_FILE="sample.war" \
    APP_DIR="/u01/oracle"

# Copy files and deploy application in WLST Offline mode
COPY container-scripts/* /u01/oracle/

# RUN wlst.sh /u01/oracle/app-deploy.py
