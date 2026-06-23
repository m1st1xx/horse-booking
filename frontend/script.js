const API_URL = "http://127.0.0.1:8000";

async function loadSlots(){

    const gender =
        document.getElementById("gender").value;

    const people =
        document.getElementById("people_count").value;

    const duration =
        document.getElementById("duration").value;

    const response = await fetch(
        `${API_URL}/bookings/available-slots?gender=${gender}&people_count=${people}&duration=${duration}`
    );

    const slots = await response.json();

    const select =
        document.getElementById("booking_time");

    select.innerHTML = "";

    slots.forEach(slot=>{

        const option =
            document.createElement("option");

        option.value = slot;
        option.textContent = slot;

        select.appendChild(option);
    });
}

document
.getElementById("gender")
.addEventListener(
    "change",
    loadSlots
);

document
.getElementById("people_count")
.addEventListener(
    "change",
    loadSlots
);

document
.getElementById("duration")
.addEventListener(
    "change",
    loadSlots
);

document
.getElementById("booking-form")
.addEventListener(
"submit",
async function(e){

    e.preventDefault();

    const data = {

        client_name:
            document.getElementById(
                "client_name"
            ).value,

        phone:
            document.getElementById(
                "phone"
            ).value,

        gender:
            document.getElementById(
                "gender"
            ).value,

        people_count:
            Number(
                document.getElementById(
                    "people_count"
                ).value
            ),

        duration:
            Number(
                document.getElementById(
                    "duration"
                ).value
            ),

        booking_time:
            document.getElementById(
                "booking_time"
            ).value
    };

    const response = await fetch(
        `${API_URL}/bookings/`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }
    );

    const result =
        document.getElementById("result");

    if(response.ok){

        result.innerHTML =
            "✅ Заявка отправлена";

    }else{

        const error =
            await response.json();

        result.innerHTML =
            "❌ " + error.detail;
    }
});

loadSlots();