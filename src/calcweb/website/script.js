form = document.querySelector("#Form")
calc_input = document.querySelector("#CalcInput")
calc_output = document.querySelector("#CalcOutput")

BaseUrl = window.location.origin

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    response = await fetch(BaseUrl + "/execute", {
        method: "POST",
        body: JSON.stringify({
            "command": calc_input.value
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
    console.log(response)
    if (response.status == 200) {
        data = await response.json();
        calc_output.innerHTML = data.command + " = " + data.result;
    }
    if (response.status == 400) {
        data = await response.json();
        calc_output.innerHTML = data.Error.message;
    }
});
