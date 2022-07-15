<script>
    let src = "images/blue-circle.png"
</script>

<div class = "login-container">
    <div class = "login-logo-container">
        <!-- <img src = {src} alt = "image"> -->
    </div>
    <h1 class = "header">Welcome!</h1>
    <form class = "login-form" action = "http://127.0.0.1:5000/authenticate-user" method = "POST">
        <div class="login-form-field">
            <label>USERNAME:</label>
            <input type = "text" id = "username">
        </div>
        <div class = "login-form-field">
            <label>PASSWORD:</label>
            <input type = "password" id = "password">
        </div>
        <div class = "login-form-options">
            <a href = "#">Forgot your password?</a>
        </div>
        <button type = "submit">LOGIN</button>
        <div class = "login-form-options">
            New to app <a href = "#"> Create account</a>
        </div>
    </form>
</div>