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

function loading() {
    let login = document.getElementById('login');
    let register = document.getElementById('register');

    document.getElementsByTagName("input").value = "";
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

function validate() {
    let inner = document.getElementById("password-validate");
    let password = document.getElementById("regpassword").value;
    let form = document.getElementById('form-register');

    /* Mao ni magcheck sa input */
    validations = [
        (password.length > 5 ? inner.children[0].style.color = "green" : inner.children[0].style.color = "red"),
        (password.match(/[A-Z]/) ? inner.children[1].style.color = "green" : inner.children[1].style.color = "red"),
        (password.match(/[0-9]/) ? inner.children[2].style.color = "green" : inner.children[2].style.color = "red"),
        (password.match(/[$&+,.;:=?@#]/) ? inner.children[3].style.color = "green" : inner.children[3].style.color = "red"),
    ]

    form.addEventListener('submit', (Event) => {
        if (validations.includes('red')) {
            Event.preventDefault();
        } else {
            return true;
        }
    })
}