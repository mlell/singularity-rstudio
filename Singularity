BootStrap: shub
From: mlell/singularity-r

%labels
  Maintainer Moritz Lell
  RStudio_Version 1.2.5033

%help
  This will run RStudio Server

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
  install -Dv \
    rstudio_auth.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth
  install -Dv \
    rstudio_auth_file.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth_file
  install -Dv \
    ldap_auth.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/ldap_auth
  install -Dv \
    rstudio-passwd.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio-passwd

%post
  # Software versions
  export RSTUDIO_VERSION=1.3.1056

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # Add support for LDAP authentication
  wget \
    --no-verbose \
    -O get-pip.py \
    "https://bootstrap.pypa.io/get-pip.py"
  python3 get-pip.py
  rm -f get-pip.py
  pip3 install ldap3

  apt-get install -y libxml2-dev git

  # Do not let OpenBLAS launch a thread per core, that exhausts resource
  # limits when running many workers on machines with many cores
  # RStudio server does not honor environment variables, so I need to
  # set it here as well
  echo "OMP_NUM_THREADS=1" >> /etc/R/Renviron.site

  # Clean up
  rm -rf /var/lib/apt/lists/*
