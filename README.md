# EmailExtraction

## enviroment

runs on `Python 3.8.5` and `flask 1.1.2`

## usage

target url route `:5000/email_extrac`

Support both `PUT` and `POST` method to get the total number of the email addresses in the `raw_text` field in your request. (Use `json` format for the `post` request). Then it will reply a json with the answer in `total_email_ids`

### example

when it runs on the local  host `127.0.0.1`

- POST

```
curl --location --request POST '127.0.0.1:5000/email_extract' \
--header 'Content-Type: application/json' \
--data-raw '{
    "raw_text":"abc@qq.com fahfia@qq.com fafa@1"
}'
# reply
{
    "total_email_ids": 2
}
```

- PUT

```
curl --location --request PUT '127.0.0.1:5000/email_extract?raw_text=11@qq.com'
# reply
{
    "total_email_ids": 1
}
```

## TODO

- Could use some authentication system in front of the service, maybe use encrypted cookies and sessions to maintain the log in status
- Could use Conda or Docker to solve the problem of dependencies for deployment

