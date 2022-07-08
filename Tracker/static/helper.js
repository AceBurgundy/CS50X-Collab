// A function that counts the length of the input and changes the value of a span element 0/value

/* 
 Ex: 
 
    Input: Lorem ipsum

    Counter: 11/value

    For this to work, add this to your input

    counter(id-of-input, id-of-counter, limit-of-input)

    your html elements should look like this,

    <p id="id-of-counter"><span>0</span>/ (limit-of-input) </p>
    <input type="text" id="id-of-input" onkeyup="counter('id-of-input','id-of-counter',limit-of-input)" maxlength="30">
 
*/

// use default only on one function or class
export function counter(inputId, counterId, restrict) {

    const limit = restrict

    inputId.addEventListener('keyup', () => {

        inputId.value.length <= limit ? counterId.children[0].textContent = inputId.value.length : counterId.style.color = "red";
    })
}