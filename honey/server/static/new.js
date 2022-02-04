function new_register_on_table() {
    let uri = window.location.href;
    const t_n = uri.split("/")[uri.split("/").length - 1];
    const name = document.querySelector("#name");
    console.log(name.value);
    const email = document.querySelector("#email");
    console.log(email.value);
    
    const form = new FormData();
    form.append("name", name.value);
    form.append("email", email.value);
    if (name.value && email.value) {
        fetch("http://localhost:3000/api/collectors", {
            method: "PUT",
            body:form
        });
        window.location.replace(`http://localhost:5000/js/${t_n}`)
    }
    
    else{
        alert("Rellena todos los campos!");
    };
};