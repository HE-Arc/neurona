FROM alpine

RUN apk update
RUN apk add npm nodejs

WORKDIR /data

CMD sh -c "npm install && npm run dev"
