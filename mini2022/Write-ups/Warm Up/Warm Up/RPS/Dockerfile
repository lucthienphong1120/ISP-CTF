FROM yukimina/ctf_create_img

RUN adduser noob
COPY RPS /
COPY flag.txt /
WORKDIR /

RUN chmod 777 ./RPS

EXPOSE 3138
USER noob
CMD tcpserver -t 50 -RHl0 0.0.0.0 3138 ./RPS
