# This is the Dockerfile for Oracle WebLogic Server 12.2.1.x.x 
# 
# REQUIRED FILES TO BUILD THIS IMAGE
# ----------------------------------
# For generic build: fmw_12.2.1.x.x_wls_Disk1_1of1.zip 
# Or for developer build: fmw_12.2.1.x.x_wls_quick_Disk1_1of1.zip 
#
# Download WebLogic Server Infrastructure  Installer 12.2.1.2
# # - http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-for-dev-1703574.html 
#
# The zip archive used must be available at a URL specified in FMW_BASEURL.
# If you do not have a web server, you can use a Caddy Server in OpenShift, see https://github.com/rbaumgar/rhel-caddy
#
# Build Variables
# ---------------
# The following environment variables are required:
#
# FMW_BASEURL - URL from which to download the weblogic zip archive.
# FMW_VERSION - Set to the desired version as matching zip archive (eg: 12.2.1.1.0)
# FMW_QUICK   - If set then the quick/developer version of weblogic will be used.
# 
# The resulting image of this Dockerfile contains a empty Oracle WebLogic Domain.
#
FROM rhel7-OracleJDK

MAINTAINER Robert Baumgartner <robert.baumgartner@redhat.com>

# WLS Configuration (editable during build time)
# ------------------------------
ARG ADMIN_PASSWORD

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
ENV FMW_PKG=fmw_${FMW_VERSION}_wls${FMW_QUICK:+_quick}_Disk1_1of1.zip \
    FMW_JAR=fmw_${FMW_VERSION}_wls${FMW_QUICK:+_quick}_quick.jar \
    SCRIPT_FILE=/u01/oracle/createAndStartEmptyDomain.sh \
    ORACLE_HOME=/u01/oracle \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    DEBUG_FLAG=true \
    PRODUCTION_MODE=dev \
    DOMAIN_NAME="${DOMAIN_NAME:-base_domain}" \
    DOMAIN_HOME=/u01/oracle/user_projects/domains/${DOMAIN_NAME:-base_domain} \
    ADMIN_PORT="${ADMIN_PORT:-7001}" \
    ADMIN_USERNAME="${ADMIN_USERNAME:-weblogic}" \
    ADMIN_NAME="${ADMIN_NAME:-AdminServer}" \
    ADMIN_PASSWORD="${ADMIN_PASSWORD:-""}" \

    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin

# Copy packages
# -------------
ADD ${FMW_BASEURL}/${FMW_PKG} /u01/
COPY install.file oraInst.loc /u01/
COPY container-scripts/createAndStartEmptyDomain.sh container-scripts/create-wls-domain.py /u01/oracle/

# Setup filesystem and oracle user
# Install and configure Oracle JDK
# Adjust file permissions, go to /u01 as user 'oracle' to proceed with WLS installation
# ------------------------------------------------------------
RUN chmod a+xr /u01 && \
    chmod +xr $SCRIPT_FILE && \
    useradd -b /u01 -M -s /bin/bash oracle && \
    chown oracle:oracle -R /u01 && \
    echo oracle:oracle | chpasswd && \
    cd /u01 && $JAVA_HOME/bin/jar xf /u01/$FMW_PKG && cd - && \
    su -c "$JAVA_HOME/bin/java -jar /u01/$FMW_JAR -silent -responseFile /u01/install.file -invPtrLoc /u01/oraInst.loc -jreLoc $JAVA_HOME -ignoreSysPrereqs -force -novalidation ORACLE_HOME=$ORACLE_HOME INSTALL_TYPE=\"WebLogic Server\"" - oracle && \
    rm /u01/$FMW_JAR /u01/$FMW_PKG /u01/oraInst.loc /u01/install.file && \
    find /u01 -user oracle -exec chmod a+rwX /u01 {} ';'

# Expose Node Manager default port, and also default for admin and managed server 
# oc new-app does not like variables used in ports.
#EXPOSE $NM_PORT $ADMIN_PORT $MS_PORT $DEBUG_PORT
EXPOSE 5556 8001 7001 8453

WORKDIR ${ORACLE_HOME}

# Define default command to start script. 
CMD ["/u01/oracle/createAndStartEmptyDomain.sh"]
