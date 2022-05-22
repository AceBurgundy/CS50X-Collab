const toRegister = document.querySelector("#to-register");
const toLogin = document.querySelector("#to-login");
const formsContainer = document.querySelector(".forms-container");
const cover = document.querySelector(".cover");
 
toRegister.addEventListener('click', () => {
    formsContainer.classList.add("to-register");
    cover.classList.add("to-register");
})

toLogin.addEventListener('click', () => {
    formsContainer.classList.remove("to-register");
    cover.classList.remove("to-register");
})

function showHide(password, eye, eyeSlash) {
    let eyeClose = document.getElementById(eyeSlash);
    let eyeOpen = document.getElementById(eye);
    let Inputpassword = document.getElementById(password);

    if (Inputpassword.type == "text") {
        Inputpassword.setAttribute("type", "password");
        eyeOpen.style.display = "none";
        eyeClose.style.display = "block";
    } else {
        Inputpassword.setAttribute("type", "text");
        eyeOpen.style.display = "block";
        eyeClose.style.display = "none";
    }
}

window.onload = function() {
    document.getElementById('username').value = "AACaps";
    document.getElementById('email').value = "aacaps@gmail.com";
    document.getElementById('regpassword').value = "aac12345";
}

function loading() {
    var cover = document.querySelector('.cover');
    var formsContainer = document.querySelector('.forms-container');
    cover.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });
    formsContainer.addEventListener('touchmove', preventKeyBoardScroll, { passive: false });

    function preventKeyBoardScroll(e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    }

    let form = document.getElementById('form-register');
    form.reset();
}

function validate() {
    
    let form = document.getElementById('form-register');
    const userName = document.getElementById('username').value;
    const regPassword = document.getElementById('regpassword');
    const email = document.getElementById('email').value;
    const pattern = /(where)|(select)|(update)|(delete)|(.schema)|(from)|(drop)|[0-9]|[!@#$%^&*()_+}{":?></*+[;'./,]|-/gi;
    /* Dot Icons */
    const userNameCircle = document.getElementById('first-name-circle');

    const emailCircle = document.getElementById('email-circle');

    validations = [
        (userName.length > 2 ? userNameCircle.style.fill = "green" : userNameCircle.style.fill = "red" ),
        (userName.length < 30 ? userNameCircle.style.fill = "green" : userNameCircle.style.fill = "red" ),
        (userName.match(pattern) || userName.trim() === "" ? userNameCircle.style.fill = "red" : userNameCircle.style.fill = "green" ),
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
}