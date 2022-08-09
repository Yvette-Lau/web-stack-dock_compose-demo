FROM python:3.7-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN mkdir /code
WORKDIR /code
COPY . /code
# uwsgi setup
RUN apk add python3-dev build-base linux-headers pcre-dev
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN sed -i 's/\r$//g' /code/entrypoint.sh
# RUN chmod +x /code/entrypoint.sh
# RUN /code/entrypoint.sh
CMD ["uwsgi", "--ini", "/code/mysite_uwsgi.ini"]
