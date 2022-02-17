
window.navigator.geolocation.getCurrentPosition(async(gp) => {
    let lat = gp.coords.latitude;
    let lon = gp.coords.longitude;
    const res = await fetch(`http://localhost:5000/finder?lat=${lat}&lon=${lon}`, {
        method:"POST"
    });
    const data = await res.json();
    console.log(data);
    
    const main = document.querySelector("#main");

    data.data.forEach((dea) => {

         // CREACION DE ELEMENTOS

        const card = document.createElement("div");
        const map_div = document.createElement("div");
        const card_body = document.createElement("div");
        const card_title = document.createElement("h5");
        const card_text = document.createElement("p");
        const btn = document.createElement("a");
        const iframe = document.createElement("iframe");

         //APLICAR LOS ESTILOS DE BOOTSTRAP

        card.className = "card";
        map_div.className = "card-img-top";
        card_body.className = "card-body";
        card_title.className = "card-title";
        card_text.className = "card-text";
        btn.className = "btn btn-success";
        card.style.marginTop = "2.5em";
        // card.style.marginBottom = "2.5em";

        //DATOS
        // int() == parseInt()
        card_title.innerText = dea.address;
        card_text.innerText = `A ${parseInt(dea.distance)} metros`;
        btn.href = `https://www.google.com/maps/dir/${lat},${lon}/${dea.latlon[0]},${dea.latlon[1]}`;
        btn.innerText = "Maps";
        btn.target = "_blank";
        iframe.width = 350;
        iframe.height = 275;
        const dif_lat = 0.002425;
        const dif_lon = 0.000334;
        iframe.src = `https://www.openstreetmap.org/export/embed.html?bbox=${dea.latlon[1]-dif_lon}%2C${dea.latlon[0]-dif_lat}%2C${dea.latlon[1]+dif_lon}%2C${dea.latlon[0]+dif_lat}&amp;layer=mapnik&amp;marker=${dea.latlon[0]}%2C${dea.latlon[1]}`;
    
        //APPEND

        card_body.append(card_title);
        card_body.append(card_text);
        card_body.append(btn);
        card.append(map_div);
        card.append(card_body);
        map_div.append(iframe);
        main.append(card);
    });
   

    
    

   

    

    

    

    


});

// async () => {};
// const fun = async () => {};
// async function name_func() {};
// document.createElement("h1");
// const body = document.querySelector("body");
// Element(body).append()