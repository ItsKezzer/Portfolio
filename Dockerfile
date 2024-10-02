FROM python:3.11-slim as build
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN reflex init
RUN reflex export --frontend-only --no-zip

FROM nginx:alpine
COPY --from=build /app/.web/_static/ /usr/share/nginx/html
EXPOSE 80
