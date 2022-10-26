FROM yukimina/ctf_create_img

RUN adduser noob
COPY chall /
COPY flag.txt /
WORKDIR /

RUN chmod 777 ./chall

EXPOSE 3137
USER noob
CMD tcpserver -t 50 -RHl0 0.0.0.0 3137 ./chall