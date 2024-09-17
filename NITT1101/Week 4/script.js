function addition() {
    // ref to DOM elements
    let num1ref = document.getElementById('num1');
    let num2ref = document.getElementById('num2');
    let resultref = document.getElementById('result');

    // get the values from the DOM elements
    let num1 = Number(num1ref.value);
    let num2 = Number(num2ref.value);

    // add the numbers
    let result = parseFloat(num1) + parseFloat(num2);

    // update answer to DOM
    resultref.innerHTML = result;
    
}