const grade_test = async () => {
    const result = [];
    const inputs = document.querySelector("#test").getElementsByTagName("input");
    for (let i = 0; i < inputs.length; i ++) {
        let radio = inputs[i];
        if (radio.checked) {
            result.push([radio.name, radio.value]); // [id question - id option] 
        };
    };
    const res = await fetch("http://localhost:5000/api/grade", {
        method:"POST",             
        headers : {
            "content-type": "application/json",
        },
        body: JSON.stringify(result) // json.dumps
    });
    const data = await res.json();
    for (o_b of Object.entries(data.answers)) {
        radio = document.getElementById(o_b[0]);
        let radio_container = radio.parentElement;
        o_b[1] ? radio_container.style.backgroundColor = "#4bdf4b" : radio_container.style.backgroundColor =  "#e34747";
    };
    document.getElementById("grade").innerText = `Grade: ${data.grade}`
};
