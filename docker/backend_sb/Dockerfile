FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get -yq install net-tools nginx

COPY backend_sb /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/backend_sb /etc/nginx/sites-enabled/

EXPOSE 9110

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]