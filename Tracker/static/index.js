import { counter } from "./helper.js"

// script to show and hide modal to add new project
const showModal = document.querySelector(".show-modal-button");
const projectModal = document.querySelector(".project-modal-container");
const modalXButton = document.querySelector(".modal-x-button");
const modalCancelButton = document.querySelector(".modal-close-button");
const background = document.getElementById('backround')

showModal.addEventListener("click", () => {
    background.style.opacity = "60%"
    background.style.visibility = "visible"
    projectModal.classList.toggle("active")
})

modalXButton.addEventListener("click", () => {
    background.style.opacity = "0"
    background.style.visibility = "hidden"
    projectModal.classList.toggle("active")
})

modalCancelButton.addEventListener("click", () => {
    background.style.opacity = "0"
    background.style.visibility = "hidden"
    projectModal.classList.toggle("active")
})

// script to show and hide profile dropdown
let profileDropdownButton = document.querySelector(".profile-dropdown-button");

profileDropdownButton.addEventListener("click", () => {

    profileDropdownButton.classList.toggle("active");
})

// script to validate inputs in add project modal
const modalForm = document.querySelector(".add-project-form");

modalForm.addEventListener("keyup", () => {
    let titleCounter = document.querySelector(".counter-for-title");
    let descriptionCounter = document.querySelector(".counter-for-description");
    const projectTitle = document.querySelector(".project-input").value;
    const projectDescription = document.querySelector(".project-description").value;
    let violated = 0;

    if (projectDescription.length <= 50) {
        descriptionCounter.textContent = projectDescription.length
    } else if (projectTitle.length <= 30) {
        titleCounter.textContent = projectTitle.length
    } else {
        return false;
    }

    let modalValidate = [
        (projectTitle.search(/[$&+,.;:=?@#1-10':"><}{!%^*)(]/) > -1),
        (projectTitle.search(" ") > -1),
        (projectDescription.search(/[$&+,.;:=?@#1-10':"><}{!%^*)(]/) > -1),
        (projectDescription.search(" ") > -1)
    ]

    violated = modalValidate.reduce((acc, cur) => acc + cur)

    modalForm.addEventListener('submit', (Event) => {
        if (violated > 0) {
            Event.preventDefault();
        } else {
            return true;
        }
    })
});


const profileCancelButton = document.querySelector(".profile-x-button");
let profile = document.getElementById("profile-picture-main")

profile.addEventListener('click', () => {
    background.style.opacity = "60%"
    background.style.visibility = "visible"
    profileSection.classList.toggle("active")
})

background.addEventListener('click', () => {
    background.style.opacity = "0"
    background.style.visibility = "hidden"
    profileSection.classList.remove("active")
    projectModal.classList.remove("active")
})

profileXButton.addEventListener('click', () => {
    background.style.opacity = "0"
    background.style.visibility = "hidden"
    profileSection.classList.remove("active")
})

profileCancelButton.addEventListener('click', () => {
    background.style.opacity = "0"
    background.style.visibility = "hidden"
    profileSection.classList.remove("active")
})

const firstName = document.getElementById("first-name")
const firstNameCounter = document.getElementById("first-name-counter")
const lastName = document.getElementById("last-name")
const lastNameCounter = document.getElementById("last-name-counter")
const address = document.getElementById("address")
const addressCounter = document.getElementById("address-counter")
const skills = document.getElementById("skills")
const skillsCounter = document.getElementById("skills-counter")
const motto = document.getElementById("motto")
const mottoCounter = document.getElementById("motto-counter")
counter(firstName, firstNameCounter, 60);
counter(lastName, lastNameCounter, 60);
counter(address, addressCounter, 100);
counter(motto, mottoCounter, 200)

/*------------- hides and shows the dropdown-------------*/

const countryDropdownSwitch = document.querySelector(".country-select-switch")
    // dropdown toggle

const countryDropDownMenu = document.querySelector("#country-dropdown")
    // actual dropdown

countryDropdownSwitch.addEventListener("click", () => {

    countryDropDownMenu.classList.toggle("active")
})




/*------------- shows flag of each countries-------------*/

let country = document.querySelectorAll(".country");
// li class="country"

const flag = document.querySelectorAll(".flag")
    // img class="flag"

flag.forEach(flag => {
        let countryVal = flag.parentNode.getAttribute("value").toLowerCase();
        /* To get the value of country, we have to use parentNode as it is
        the parent element of flag */

        // flag.src = "./static/flags/".concat(countryVal, '.svg');
        flag.src = "https://flagcdn.com/16x12/".concat(countryVal, '.png');
    })
    /* 
        flag.src = "./static/flags/".concat(countryVal, '.svg');
        Since all flags are named after their 2 character country code,
             we will use concat to join the current value of countryVal and join it with .svg
             
             ex:
             
             countryVal = ph
             .concat(countryVal, '.svg') === ph.svg
             
             flag.src = ./static/flags/ph.svg
             */




/*-------------simulates select actions-------------*/

const selectedCountry = document.getElementById("selected-country-span");
// displays the country that you had select

const inputCountry = document.getElementById("country-input");
// input with type hidden used to pass value to your backend server (I use flask).

let countryName = document.querySelectorAll(".country-name");
// text content in each list which are the actual country names

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

/* Add event listener (oninput) to the search input element
         While looping through each country name
         set text to the name of the country in lowercase (Using console will log all country names)
         set search to the user input in lowercase
         set found to use indexOf to find the index of search value in country names

         if the value of found is not equal to negative one, set display to grid
             else display none.

         ex: search = 'ph'
             found = the indexOf() countries where "ph" occured in.

             found in index 19
              all countries that are -1 will have a display of none.
         */