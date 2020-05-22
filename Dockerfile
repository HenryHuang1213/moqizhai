FROM python:3.6
LABEL maintaner="Henry Huang <henryhuang1213@gmail.com>"
COPY moqizhai /moqizhai/
WORKDIR /moqizhai
RUN pip install pipenv \
	&& pipenv install 
EXPOSE 8000
CMD [ "pipenv", "run", "python", "moqizhai.py" ]