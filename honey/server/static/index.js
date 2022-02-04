// const h2 = document.querySelector("h2");
// h2.innerText = "Collector";

//lambda a: a
//(a) => {a}; 
// const uri_collectors = "http://localhost:3000/api/collectors";
// console.log(fetch(uri_collectors));
// fetch(uri_collectors)
//     .then((res) => res.json())
//     .then((data) => {for (let collector of data["data"]) {
//                     console.log(collector)
// }});
// data = req.get(uri).json()
// const data_out = [];
// async function get_data(uri) {
//     const res = await fetch(uri); //threading.join()
//     const data = await res.json();
//     for (let value of data["data"]) {
//         data_out.push(value)
//     }
// };

// get_data(uri_collectors);
// console.log(data_out);



const uri = "http://localhost:3000/api/collectors";
async function get_data(uri) {
    const res = await fetch(uri);
    const pre_data = await res.json();
    const data = await pre_data["data"];
    const fields = Object.keys(data[0]);
    const h_tr = document.createElement("tr");
    for (let field of fields) {
        const th = document.createElement("th");
        th.innerText = field;
        h_tr.append(th);

    };
    const thead = document.querySelector("#thead");
    thead.append(h_tr);
    // data.forEach((collector) => {
    //     const tr = document.createElement("tr");
    //     Object.values(collector).forEach((value) => {
    //         const td = document.createElement("td");
    //         td.innerText = value;
    //     });
    // });

    for (let collector of data) {
        const tr = document.createElement("tr");
        for (let value of Object.values(collector)) {
            const td = document.createElement("td");
            td.innerText = value;
            tr.append(td);
        };
        document.querySelector("#tbody").append(tr);
    };
};

get_data(uri);