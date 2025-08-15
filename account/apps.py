from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

<!DOCTYPE html>
<html lang = "en">
<head>
<meta charset = "UTF-8">
<title> 404 Not Found </title>
<style>
     body{
        font-family: Arial,sans-serif;
        text-align: center;
        padding: 50px;
     }
     h1{
        font-size: 40px;
        color: red;
     }
     p{
        font-size: 18px;
     }
     a{
        color:blue;
        text-decoration: none;
     }
     a:hover{
        text-decoration: underline;
     }

</style>
</head>
<body>
     <h1> 404 </h1>
     <p> Oops! The page you are looking for , does not exist. </p>
     <p><a href = "/"> Go back to home </a></p>
</body>
</html>
