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
    let form = document.getElementById('form-register');

    form.reset();
}

function validate() {
    let inner = document.getElementById("password-validate");
    let form = document.getElementById('form-register');

    /* Input Classes */
    const firstName = document.getElementById('first-name').value;
    const lastName = document.getElementById('last-name').value;
    const telephone = document.getElementById('telephone').value;
    let password = document.getElementById("regpassword").value;
    const confirmPasswordVal = document.getElementById('confirm-password').value;
    const email = document.getElementById('email').value;


    /* Dot Icons */
    const firstNameCircle = document.getElementById('first-name-circle');
    const lastNameCircle = document.getElementById('last-name-circle');
    const telephoneCircle = document.getElementById('telephone-circle');
    const confirmPasswordCircle = document.getElementById('conpass-circle');
    const emailCircle = document.getElementById('email-circle');

    validations = [
        (
            firstName.length > 2 &&
            firstName.length < 30 &&
            !firstName.match(/[$&,.[;:=?@#]/) ||
            firstName === null ?

            firstNameCircle.style.color = "green" : firstNameCircle.style.color = "red"
        ),

        (
            lastName.length > 2 &&
            lastName.length < 30 &&
            !lastName.match(/[$&,.[;:=?@#]/) ||
            lastName === null ?

            lastNameCircle.style.color = "green" : lastNameCircle.style.color = "red"
        ),

        (
            email.match(/[@]/) && email.match(".com") ?

            emailCircle.style.color = "green" : emailCircle.style.color = "red"
        ),

        (
            telephone.length > 2 &&
            !telephone.match(/[$&,.[;:=?@#]/) &&
            !telephone.match(/[A-Z]/) &&
            !telephone.match(/[a-z]/) ||
            telephone === null ?

            telephoneCircle.style.color = "green" : telephoneCircle.style.color = "red"
        ),

        (password.length > 5 ? inner.children[0].style.color = "green" : inner.children[0].style.color = "red"),

        (password.match(/[A-Z]/) ? inner.children[1].style.color = "green" : inner.children[1].style.color = "red"),

        (password.match(/[0-9]/) ? inner.children[2].style.color = "green" : inner.children[2].style.color = "red"),

        (password.match(/[$&+,.;:=?@#]/) ? inner.children[3].style.color = "green" : inner.children[3].style.color = "red"),

        (password === confirmPasswordVal ? confirmPasswordCircle.style.color = "green" : confirmPasswordCircle.style.color = "red"),
    ]

    form.addEventListener('submit', (Event) => {
        if (validations.includes('red')) {
            Event.preventDefault();
        } else {
            return true;
        }
    })
}