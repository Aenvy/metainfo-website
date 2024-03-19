FROM ktm384.gre.hpecorp.net:18446/library/node:lts-alpine as frontend
LABEL maintainer "cms5gsiths@hpe.com"

ARG ROOT_CA_CERT=HPE_PrivateRootCA.base64.zip
ARG SSL_CA_CERT=HP_ENT_Private_SSL_CA.base64.zip

WORKDIR /usr/local/share/ca-certificates
# Copy certifcates archives into the image
COPY HPE_resources/${ROOT_CA_CERT} HPE_resources/${SSL_CA_CERT} ./

RUN env | sort && \
    apk add --no-cache \
    curl && \
    for cert in ${ROOT_CA_CERT} ${SSL_CA_CERT}; do \
      unzip ${cert}; \
    done && \
    rm *.zip && \
    update-ca-certificates

WORKDIR /frontend/

COPY mc5g-metainfo-website-frontend /frontend/

RUN npm install

RUN npm run build

FROM python:3.12-alpine

RUN mkdir -p /app
WORKDIR /app

COPY mc5g-metainfo-website-backend/ /app/
COPY --from=frontend /frontend/build/*.js* /app/frontend/static/
COPY --from=frontend /frontend/build/*.png /frontend/build/*.svg /frontend/build/*.ico /frontend/build/*.json /frontend/build/*.txt /app/frontend/
COPY --from=frontend /frontend/build/index.html \
    /app/frontend/
COPY --from=frontend /frontend/build/static/. /app/frontend/static/

RUN rm -rf $(cat mc5g-metainfo-website-frontend/.dockerignore | grep -v '^#' | sed 's/^!//')

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/backend.py"]
