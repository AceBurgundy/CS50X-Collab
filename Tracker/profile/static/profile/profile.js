import { counter, eyeToggle } from "/static/helper.js"

const profileSection = document.getElementById('profile-section')
const profileCancelButton = document.querySelector(".profile-close-button");
const profileXButton = document.querySelector(".profile-x-button");
let background = document.querySelector(".background")

window.addEventListener("load", () => {
    if ((document.querySelector(".error")) === null) {
        if (document.readyState == "complete") {
            background.classList.toggle("active")
            profileSection.classList.toggle("active")
        }
    }
})

window.addEventListener("DOMContentLoaded", () => {
    if ((document.querySelector(".error")) !== null) {
        profileSection.style.transform = "translate(-50%, -50%)"
        background.style.transition = "-10ms"
        background.style.height = "100vh"
        profileSection.style.transition = "-10ms"
        profileSection.style.opacity = "1"
    }
})

profileXButton.addEventListener('click', () => {
    if (profileSection.classList.contains("active")) {
        profileSection.classList.remove("active")
        setTimeout(() => {
            window.history.back();
        }, 300);
    } else {
        profileSection.style.transition = "500ms"
        profileSection.style.transform = "translate(-50%, -40%)"
        profileSection.style.opacity = "0"
        setTimeout(() => {
            window.history.back();
        }, 300);
    }
})



profileCancelButton.addEventListener('click', () => {
    if (profileSection.classList.contains("active")) {
        profileSection.classList.remove("active")
        setTimeout(() => {
            window.history.back();
        }, 300);
    } else {
        profileSection.style.transition = "500ms"
        profileSection.style.transform = "translate(-50%, -40%)"
        profileSection.style.opacity = "0"
        setTimeout(() => {
            window.history.back();
        }, 300);
    }
})

document.querySelector(".image-background").addEventListener("click", () => {
    document.querySelector(".new-password-modal").classList.remove("active")
})

counter(
    document.getElementById("first-name"),
    document.getElementById("first-name-counter"),
    60
)

counter(
    document.getElementById("last-name"),
    document.getElementById("last-name-counter"),
    60
)

counter(
    document.getElementById("address"),
    document.getElementById("address-counter"),
    300
)

counter(
    document.getElementById("skills"),
    document.getElementById("skills-counter"),
    200
)

counter(
    document.getElementById("motto"),
    document.getElementById("motto-counter"),
    200
)

// script to dynamically resize the textarea height
const profileTextarea = document.querySelector("#motto");

profileTextarea.addEventListener("input", e => {
    profileTextarea.style.height = `${e.target.scrollHeight}px`
})

/*------------- hides and shows the dropdown-------------*/

const countryDropdownSwitch = document.querySelector(".country-select-switch")

const countryDropDownMenu = document.querySelector("#country-dropdown")

countryDropdownSwitch.addEventListener("click", () => {

    countryDropDownMenu.classList.toggle("active")
})




/*------------- shows flag of each countries-------------*/

const flag = document.querySelectorAll(".flag")

flag.forEach(flag => {
    let countryVal = flag.parentNode.getAttribute("value").toLowerCase();
    /* To get the value of country, we have to use parentNode as it is
    the parent element of flag */

    // flag.src = "./static/flags/".concat(countryVal, '.svg');
    flag.src = "https://flagcdn.com/16x12/".concat(countryVal, '.png');
})

/*-------------simulates select actions-------------*/

const selectedCountry = document.getElementById("selected-country-span");

const inputCountry = document.getElementById("country-input");

let countryName = document.querySelectorAll(".country-name");

countryName.forEach(country => {
    country.parentNode.addEventListener('click', () => {
        countryDropDownMenu.classList.remove("active");
        selectedCountry.textContent = country.textContent;
        inputCountry.value = country.textContent;
        inputCountry.setAttribute("value", country.textContent);
    })
})

/* While looping through each country name
   
   add an event listener (click) to the parent element
   when the parent is clicked,
       hide the dropdown
       change the text content of the dropdown toggle to the content of the list item
       change the value and the value attribute of the input with type "hidden" to the content of the list item
   */




/*------------- Simulates autocomplete-------------*/

const countrySearch = document.querySelector("#country-search");

countrySearch.addEventListener("input", () => {
    countryName.forEach(country => {
        let text = country.textContent.toLowerCase();
        let search = countrySearch.value.toLowerCase();
        let found = text.indexOf(search);

        if (found != -1) {
            country.parentNode.style.display = "grid";
        } else {
            country.parentNode.style.display = "none";
        }
    })
});

document.querySelector("#save-button").addEventListener("submit", function(event) {
    event.preventDefault();

    const profileSection = document.getElementById('profile-section')

    profileSection.classList.toggle("active")
})

const newPasswordModal = document.querySelector(".new-password-modal")
const changePasswordButton = document.querySelector(".change-password")

changePasswordButton.addEventListener(("click"), () => {
    newPasswordModal.classList.add("active")
})

const newPasswordModalCloseButton = document.querySelector("#new-password-close-button");

newPasswordModalCloseButton.addEventListener(("click"), () => {
    newPasswordModal.classList.remove("active")
})

eyeToggle(
    document.getElementById("verify-eyes-icon-container"),
    document.querySelector("#old-password-input"),
    document.querySelector("#verify-eye"),
    document.querySelector("#verify-eye-off")
)

eyeToggle(
    document.getElementById("new-password-eyes-icon-container"),
    document.querySelector("#old-password-input"),
    document.querySelector("#verify-eye"),
    document.querySelector("#verify-eye-off")
)