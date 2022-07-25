import { counter } from "/static/helper.js"

// script to show and hide modal to add new project
const projectModal = document.querySelector(".add-project-modal-container");
const modalXButton = document.querySelector(".modal-x-button");
const modalCancelButton = document.querySelector(".modal-close-button");
const background = document.getElementById('background')

window.addEventListener("DOMContentLoaded", () => {
    if ((document.querySelector(".error")) === null) {
        background.classList.toggle("active")
        projectModal.classList.toggle("active")
    } else {
        projectModal.style.transform = "translate(-50%, -50%)"
        background.style.transition = "-10ms"
        background.style.height = "100vh"
        projectModal.style.transition = "-10ms"
    }
})

modalXButton.addEventListener("click", () => {
    background.style.height = "80vh"
    projectModal.style.opacity = "0"
    projectModal.style.transform = "translate(-50%, -40%)"
    setTimeout(() => {
        window.location = "/";
    }, 300);
})

modalCancelButton.addEventListener("click", () => {
    background.style.height = "80vh"
    projectModal.style.opacity = "0"
    projectModal.style.transform = "translate(-50%, -40%)"
    setTimeout(() => {
        window.location = "/";
    }, 300);
})

counter(
    document.getElementById("add-project-input"),
    document.getElementById("counter-for-title"),
    200
)

counter(
    document.getElementById("add-project-description"),
    document.getElementById("counter-for-description"),
    200
)

const projectDescriptionTextArea = document.querySelector("#add-project-description");

projectDescriptionTextArea.addEventListener("input", e => {
    projectDescriptionTextArea.style.height = `${e.target.scrollHeight}px`
})

$('add-button').bind('submit', function(e) {
    e.preventDefault()
})