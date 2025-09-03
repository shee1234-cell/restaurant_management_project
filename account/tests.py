<!templates/reservations.html>
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title> {{restaurant_name}} </title>

<style>
body{
    font-family: Arial, sans-serif;
    text-align: center;
    color:black;
}
h1{
    color: red;
    margin-top: 50px;
}
p{
    font-size: 18px;
    margin: 10px 0;
}
img.logo{
    width: 200px;
    margin: 20px auto;
    display: block;
}
</style>
</head>
<body>
    <div class = "contact-box">
    
    <img src = "{% static 'image/logo.png'%}" alt = "logo" class ="logo">
    <p> We Welcome to serve you our delicacy</p>
    <h1> Contact Us </h1>
    <p> Email: support@demo.com </p>
    <p> Phone: +91 0000000000 </p>
    <p> Address: 123 Food street, shanti nagar/p>
    </div>

    <footer style = "text-align: center; padding: 15px; margin-top: 30px; color: #666; font-size: 14px; border-top: 1px solid #ddd;">
    <p>&copy; {{current_year}} ((restaurant_name)). All rights reserved. </p>
    </footer>
</body>
</html>