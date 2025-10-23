FROM python:3.10.3

RUN pip install https://files.kemt.fei.tuke.sk/models/spacy/sk_core_web_md-3.4.1.tar.gz
RUN python -m pip install rasa

WORKDIR /app
COPY . .

RUN rasa train

USER 1001

ENTRYPOINT [ "rasa" ]

CMD [ "run", "--enable-api","--cors", "*","--port", "8080" ]
