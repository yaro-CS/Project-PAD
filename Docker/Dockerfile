FROM php:7.0-apache
COPY ./public-html/ /var/www/html
COPY ./conf/ /etc/apache2/sites-available
EXPOSE 80

RUN apt -y update
RUN apt -y install libapache2-mod-wsgi-py3
RUN mkdir /var/www/wsgi

COPY ./wsgi/ /var/www/wsgi

RUN chmod -R --preserve-root 755 /var
RUN chmod -R --preserve-root 711 /var/wsgi
RUN chmod -R --preserve-root 755 /etc/apache2/sites-available/website.conf

RUN a2dissite 000-default
RUN a2ensite website
RUN service apache2 stop
RUN service apache2 start