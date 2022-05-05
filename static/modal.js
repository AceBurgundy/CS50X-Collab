const showModal = document.querySelector(".show-modal-button");
const projectModal = document.querySelector(".project-modal-container");
const xButton = document.querySelector(".x-button");
const cancelButton = document.querySelector(".close-button");
const modalBackdrop = document.querySelector(".backdrop");

showModal.addEventListener("click", () => {
    modalBackdrop.style.visibility = "visible";
    projectModal.style.visibility = "visible";
})

xButton.addEventListener("click", () => {
    modalBackdrop.style.visibility = "hidden";
    projectModal.style.visibility = "hidden";
})

cancelButton.addEventListener("click", () => {
    modalBackdrop.style.visibility = "hidden";
    projectModal.style.visibility = "hidden";
})

function validate() {
    let titleCounter = document.querySelector(".character-counter");
    const projectTitle = document.querySelector(".project-input").value.length;
    
    if (projectTitle <= 30) {
    titleCounter.textContent = projectTitle;
    }
    else {
        return false;
    }
}

function loading() {
    const modalForm = document.querySelector(".add-project-form");
    modalForm.reset();
}