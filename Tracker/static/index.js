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

let profileDropdownButton = document.querySelector(".profile-dropdown-button");
let profile = document.querySelector(".profile");

profileDropdownButton.addEventListener("click", () => {

    profile.classList.toggle("active");
}) 



const modalForm = document.querySelector(".add-project-form");

function validate() {
    let titleCounter = document.querySelector(".counter-for-title");
    let descriptionCounter = document.querySelector(".counter-for-description");
    const projectTitle = document.querySelector(".project-input").value;
    const projectDescription = document.querySelector(".project-description").value;
    let violated = 0;

    if (projectDescription.length <= 50) {
        descriptionCounter.textContent = projectDescription.length
    }

    else if (projectTitle.length <= 30) {
        titleCounter.textContent = projectTitle.length
    }
    else {
        return false;
    }

    modalValidate = [
    (projectTitle.search(/[$&+,.;:=?@#1-10':"><}{!%^*)(]/) > -1),
    (projectTitle.search(" ") > -1),
    (projectDescription.search(/[$&+,.;:=?@#1-10':"><}{!%^*)(]/) > -1),
    (projectDescription.search(" ") > -1) 
]

    violated = modalValidate.reduce((acc, cur) => acc + cur)
    
    console.log(violated); 

    modalForm.addEventListener('submit', (Event) => {
        if (violated > 0) {
            Event.preventDefault();
        } else {
            return true;
        }
    })
}



function loading() {
    let mainContent = document.getElementById("main-content");
    modalForm.reset();

    mainContent.style.height = "90vh"


}
