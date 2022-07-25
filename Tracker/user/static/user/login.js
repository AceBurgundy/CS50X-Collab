import { eyeToggle } from "/static/helper.js";

const toRegister = document.querySelector("#to-register");
// const toLogin = document.querySelector("#to-login");
const cover = document.querySelector("#login-cover");

eyeToggle(
    document.getElementById('logpassword-icon-container'),
    document.getElementById('logpassword'),
    document.getElementById('logeye'),
    document.getElementById('log-eye-off')
)

window.addEventListener("load", () => {
    if (screen.width > 1025) {
        cover.style.left = "-140%"
    } else if (screen.width <= 500) {
        document.querySelector(".form-login").style.marginTop = "0rem";
        document.querySelector(".form-login").style.opacity = 1;
    } else if (screen.width > 500 && screen.width < 1025) {
        cover.style.left = "-50%"
        cover.style.top = "50%"
        document.querySelector(".form-login").style.marginTop = "0rem";
        document.querySelector(".form-login").style.opacity = 1;
    }

    var formContainer = document.querySelector('.login');
    cover.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });
    formContainer.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });

    function preventKeyBoardScroll(e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    }
})

toRegister.addEventListener("click", () => {
    if (screen.width > 1025) {
        cover.style.left = "10%"
    } else if (screen.width > 500 && screen.width < 1025) {
        cover.style.top = "-50%"
        document.querySelector(".form-login").style.opacity = 0;
    } else if (screen.width <= 500) {
        document.querySelector(".form-login").style.marginTop = "2rem";
        document.querySelector(".form-login").style.opacity = 0;
    } else if (screen.height < 1000) {
        cover.style.left = "150%"
    }
    setTimeout(() => {
        window.location = "/register"
    }, 300);
})