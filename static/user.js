function showHide(jpassword, jeye) {
    let eye = document.getElementById(jeye);
    let password = document.getElementById(jpassword);

    if (password.type == "text") {
        password.setAttribute("type", "password");
        eye.classList.replace("fa-eye", "fa-eye-slash");
    } else {
        password.setAttribute("type", "text");
        eye.classList.replace("fa-eye-slash", "fa-eye");
    }
}

function hideRegister() {
    let login = document.getElementById('login');
    let register = document.getElementById('register');

    register.style.visibility = "hidden";
    login.style.marginRight = "13.2%";
}