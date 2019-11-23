FROM python:3
ADD 1.py /
EXPOSE 65432
CMD [ "python3", "./1.py" ]
