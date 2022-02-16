
window.navigator.geolocation.getCurrentPosition(async(gp) => {
    let lat = gp.coords.latitude;
    let lon = gp.coords.longitude;
    const res = await fetch(`http://localhost:5000/finder?lat=${lat}&lon=${lon}`, {
        method:"POST"
    });
    const data = await res.json();
    console.log(data);

    // CREACIONES

    const card = document.createElement("div");
    const img = document.createElement("img");
    const card_body = document.createElement("div");
    const card_title = document.createElement("h5");
    const card_text = document.createElement("p");
    const btn = document.createElement("a");
    
    const main = document.querySelector("#main");

    //CLASES

    card.className = "card";
    img.className = "card-img-top";
    card_body.className = "card-body";
    card_title.className = "card-title";
    card_text.className = "card-text";
    btn.className = "btn btn-success";

    //DATOS

    //https://www.google.com/maps/@40.4379543,-3.6795367,20z

    card_title.innerText = data["data"][0].address;
    btn.href = `https://www.google.com/maps/${data["data"][0]["latlon"]}`;
    btn.innerText = "Maps"
    //APPEND

    card_body.append(card_title);
    card_body.append(card_text);
    card_body.append(btn);
    card.append(img);
    card.append(card_body);
    main.append(card);


});

// async () => {};
// const fun = async () => {};
// async function name_func() {};
// document.createElement("h1");
// const body = document.querySelector("body");
// Element(body).append()