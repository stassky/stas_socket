FROM python:3
ADD 1.py /
EXPOSE 30080
CMD [ "python3", "./1.py" ]
