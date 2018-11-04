# Dockerfile for libc debugging

FROM 32bit/ubuntu:16.04
RUN apt-get update
RUN apt-get install -y socat
#RUN apt-get install -y file ltrace strace
#RUN apt-get install -y gcc vim
COPY ./share /home/test/
RUN chmod 755 /home/test/
WORKDIR /home/test
# ENTRYPOINT ["/bin/bash"]
# ENTRYPOINT ["./run.sh"]
ENTRYPOINT ["socat","TCP-L:10001,reuseaddr,fork","EXEC:\"env LD_PRELOAD=./libc.so.6 ./noals\""]

# socat TCP-L:10001,reuseaddr,fork EXEC:"env LD_PRELOAD=./libc_32.so.6 ./noals"

# $ ls dock/
# Dockerfile  share

# sudo docker build -t lib_test .
# sudo docker run -p 10001:10001 -it lib_test


