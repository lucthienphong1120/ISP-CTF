FROM ctf_create_img

RUN adduser noob
COPY chall /
WORKDIR /

RUN chmod 777 ./chall

EXPOSE 3136
USER noob
CMD tcpserver -t 50 -RHl0 0.0.0.0 3136 ./chall