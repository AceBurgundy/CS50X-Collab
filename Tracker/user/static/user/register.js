import { eyeToggle } from "/static/helper.js";

const toLogin = document.querySelector("#to-login");
const cover = document.querySelector("#register-cover");

eyeToggle(
    document.getElementById("regpassword-icon-container"),
    document.getElementById("regpassword"),
    document.getElementById("regeye"),
    document.getElementById("reg-eye-off")
)

window.addEventListener("load", () => {
    if (screen.width > 1024) {
        cover.style.right = "-140%"
    } else if (screen.width <= 500) {
        document.querySelector(".form-register").style.marginTop = "0rem";
        document.querySelector(".form-register").style.opacity = 1;
    } else if (screen.width > 500 && screen.width < 1025) {
        cover.style.left = "-50%"
        cover.style.top = "-50%"
        document.querySelector(".form-register").style.marginTop = "0rem";
        document.querySelector(".form-register").style.opacity = 1;
    }
    var formContainer = document.querySelector('.register');
    cover.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });
    formContainer.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });

    function preventKeyBoardScroll(e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    }
})

toLogin.addEventListener("click", () => {
    if (screen.width > 1025) {
        cover.style.right = "-60%"
    } else if (screen.width > 500 && screen.width < 1025) {
        cover.style.top = "50%"
        document.querySelector(".form-register").style.opacity = 0;
    } else if (screen.width <= 500) {
        document.querySelector(".form-register").style.marginTop = "2rem";
        document.querySelector(".form-register").style.opacity = 0;
    }
    setTimeout(() => {
        window.location = "/login"
    }, 500);
})

document.querySelector("#form-register").addEventListener(("keyup"), () => {

    let form = document.getElementById('form-register');
    const userName = document.getElementById('username').value;
    const regPassword = document.getElementById('regpassword');
    const email = document.getElementById('register-email').value;
    const pattern = /(where)|(select)|(update)|(delete)|(.schema)|(from)|(drop)|[0-9]|[!@#$%^&*()_+}{":?></*+[;'./,]|-/gi;
    /* Dot Icons */
    const userNameCircle = document.getElementById('first-name-circle');

    const emailCircle = document.getElementById('email-circle');

    validations = [
        (userName.length > 2 ? userNameCircle.style.fill = "green" : userNameCircle.style.fill = "red"),
        (userName.length < 30 ? userNameCircle.style.fill = "green" : userNameCircle.style.fill = "red"),
        (userName.match(pattern) || userName.trim() === "" ? userNameCircle.style.fill = "red" : userNameCircle.style.fill = "green"),
        (email.match(/[@]/) && email.match(".com") ? emailCircle.style.fill = "green" : emailCircle.style.fill = "red"),
        (regPassword.value.match(/(where)|(select)|(update)|(delete)|(.schema)|(from)|(drop)|-/gi) ? regPassword.style.color = "red" : regPassword.style.color = "green")
    ]

    form.addEventListener('submit', (Event) => {
        if (validations.includes('red')) {
            Event.preventDefault();
        } else {
            return true;
        }
    })
})

window.onload = function() {
    document.querySelector(".username").value = "AceBurgundy"
    document.querySelector(".email").value = "Samadriansabalo99@gmail.com"
    document.querySelector("#regpassword").value = "Adrian2001."
}