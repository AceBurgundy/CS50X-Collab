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


function coverToRight() {
    let register = document.getElementById('register');
    let cover = document.getElementById('cover');
    let login = document.getElementById('login');

    login.style.visibility = "hidden";
    register.style.visibility = "visible";
    cover.style.transform = "translateX(100%)";
    register.style.marginLeft = "13%";
    login.style.marginRight = "7%";
    login.style.transition = "0.9s";
}

function coverToLeft() {
    let register = document.getElementById('register');
    let cover = document.getElementById('cover');
    let login = document.getElementById('login');

    register.style.visibility = "hidden";
    login.style.visibility = "visible";
    register.style.transition = "0.8s";
    register.style.marginLeft = "7%";
    login.style.marginRight = "13.5%";
    cover.style.transform = "translateX(-1%)";
    login.style.transition = "1.5s ease-in-out";
    register.style.transition = "1.7s ease-in-out";
}