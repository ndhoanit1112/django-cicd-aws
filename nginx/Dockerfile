FROM --platform=linux/amd64 nginx:stable-alpine
COPY default.conf /etc/nginx
COPY default.conf /etc/nginx/conf.d
EXPOSE 80

RUN mkdir -p /var/run/gunicorn
VOLUME gunicorn:/var/run/gunicorn

CMD nginx -g 'daemon off;'