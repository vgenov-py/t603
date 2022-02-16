
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

    const iframe = document.createElement("iframe");
    

    //CLASES

    card.className = "card";
    img.className = "card-img-top";
    card_body.className = "card-body";
    card_title.className = "card-title";
    card_text.className = "card-text";
    btn.className = "btn btn-success";

    //DATOS

    //https://www.google.com/maps/@40.4379543,-3.6795367,20z
    //https://www.google.com/maps/dir/40.4332016051035,-3.676176514124818/40.433104599698716,-3.674807358572504
    //                                user_lat        , user_lon         /dea_lat           , dea_lon
    //<iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-3.7043666839599614%2C40.39937482950296%2C-3.69540810585022%2C40.40292073117573&amp;layer=mapnik" style="border: 1px solid black"></iframe><br/><small><a href="https://www.openstreetmap.org/#map=18/40.40115/-3.69989">Ver mapa más grande</a></small>
    const dea_test = data["data"][2];
    card_title.innerText = dea_test.address;
    card_text.innerText = `A ${parseInt(dea_test.distance)} metros`;
    btn.href = `https://www.google.com/maps/dir/${lat},${lon}/${dea_test.latlon[0]},${dea_test.latlon[1]}`;
    btn.innerText = "Maps";
    btn.target = "_blank";
    iframe.width = 350;
    iframe.height = 275;
    const dif_lat = 0.002425;
    const dif_lon = 0.000334;
    iframe.src = `https://www.openstreetmap.org/export/embed.html?bbox=${dea_test.latlon[1]-dif_lon}%2C${dea_test.latlon[0]-dif_lat}%2C${dea_test.latlon[1]+dif_lon}%2C${dea_test.latlon[0]+dif_lat}&amp;layer=mapnik`;

    console.log(`https://www.openstreetmap.org/export/embed.html?bbox=${dea_test.latlon[1]-dif_lon}%2C${dea_test.latlon[0]-dif_lat}%2C${dea_test.latlon[1]+dif_lon}%2C${dea_test.latlon[0]+dif_lat}&amp;layer=mapnik`);
    //APPEND

    card_body.append(card_title);
    card_body.append(card_text);
    card_body.append(btn);
    card.append(img);
    card.append(card_body);
    main.append(iframe);
    main.append(card);


});

// async () => {};
// const fun = async () => {};
// async function name_func() {};
// document.createElement("h1");
// const body = document.querySelector("body");
// Element(body).append()