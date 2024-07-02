FROM python:3.12 as build-dependencies

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    APP_INSTALL_PATH=/the-app
ENV PYTHONPATH=$APP_INSTALL_PATH

# Copy only the dependency files
COPY /pyproject.toml /poetry.lock $APP_INSTALL_PATH/

RUN pip3 install --no-cache-dir poetry==1.8.2 && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-directory --no-ansi --only main,prod --directory $APP_INSTALL_PATH

FROM build-dependencies as build-api

COPY /scripts/start-backend.sh /scripts/gunicorn_conf.py $APP_INSTALL_PATH/
RUN chmod +x $APP_INSTALL_PATH/start-backend.sh

FROM build-api AS api

COPY /api $APP_INSTALL_PATH/api

WORKDIR $APP_INSTALL_PATH

EXPOSE 80

CMD ["./start-backend.sh"]
