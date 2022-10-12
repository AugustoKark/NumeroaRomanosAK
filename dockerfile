FROM python:3
RUN git clone https://github.com/AugustoKark/NumeroaRomanosAK.git
WORKDIR /NumeroaRomanosAK
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]