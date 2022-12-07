let testCheckbox = document.getElementsByClassName("form-check-input")
let nextBtn = document.getElementById("test_next_btn")

if(nextBtn == undefined) {
    window.localStorage.setItem('correct', 0)
    window.localStorage.setItem('incorrect', 0)
}

var num = JSON.parse(localStorage.getItem('num'))

console.log(nextBtn.textContent == "Submit")

nextBtn.addEventListener("click", function() {

    count = 0
    for (let i = 0; i < testCheckbox.length; i++) {
        if (testCheckbox[i].checked && testCheckbox[i].value == "True") {
            
            new_value = parseInt(localStorage.getItem('correct'))
            console.log(new_value)
            if (new_value) {
                window.localStorage.setItem('correct', new_value + 1)
            }
            else {
                window.localStorage.setItem('correct', 1);
            }
            count++
            
        }
    }
    if (count == 0) {
        new_value = parseInt(localStorage.getItem('incorrect'))
        if (new_value) {
            window.localStorage.setItem('incorrect', new_value + 1)
        }
        else {
            window.localStorage.setItem('incorrect', 1);
        }
    }

    if (nextBtn.textContent == "Submit") {
        let correctAnswers = localStorage.getItem('correct')
        let incorrectAnswers = localStorage.getItem('incorrect')
        

        window.location.replace("http://localhost:8000/results/" + String(correctAnswers) + "/" + String(incorrectAnswers))
    }
})
