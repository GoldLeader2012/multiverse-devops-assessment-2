FROM amazon/aws-cli:latest
RUN yum update -y \
    && yum install -y yum-utils shadow-utils unzip zip \
    && yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo \
    && yum install -y terraform
RUN mkdir ~/.aws \
    && echo -e "[default]\nregion = eu-west-2\noutput = json" > /root/.aws/config
ADD aws-credentials /root/.aws/credentials
# need to mount working dir to root
WORKDIR /root
ENTRYPOINT /bin/bash
