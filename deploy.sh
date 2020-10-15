
heroku create $YOUR_HEROKU_PROJECT_NAME

heroku container:push web --app $YOUR_HEROKU_PROJECT_NAME

heroku container:release web --app $YOUR_HEROKU_PROJECT_NAME

heroku logs --app $YOUR_HEROKU_PROJECT_NAME --tail
