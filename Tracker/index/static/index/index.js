// script to show and hide profile dropdown


let profileDropdownButton = document.querySelector(".profile-dropdown-button");

profileDropdownButton.addEventListener("click", () => {

    profileDropdownButton.classList.toggle("active");
})

document.querySelectorAll(".error").forEach((error) => {
    error.style.visibility = "visible"
    error.style.opacity = 1;

    setTimeout(() => {
        error.style.opacity = 0;
        error.style.visibility = "hidden";
    }, 1000)
})

const extendButton = document.querySelectorAll(".project-extend")

extendButton.forEach((button) => {
    button.addEventListener("click", () => {
        button.parentElement.parentElement.parentElement.classList.toggle("active")
    })
})

const projectMenu = document.querySelectorAll(".three-dot")

projectMenu.forEach((button) => {
    button.addEventListener("click", () => {
        button.parentElement.classList.toggle("active")
    })
})