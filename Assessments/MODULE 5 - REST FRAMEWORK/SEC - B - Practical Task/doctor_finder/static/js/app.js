let nextUrl = "/api/doctors/";
let prevUrl = null;

// LOAD DOCTORS
async function loadDoctors(url = "/api/doctors/") {

    let search = document.getElementById("searchInput").value;

    if (search) {
        url = `/api/doctors/?search=${search}`;
    }

    let res = await fetch(url);
    let data = await res.json();

    nextUrl = data.next;
    prevUrl = data.previous;

    let html = "";

    data.results.forEach(doc => {
        html += `
        <div class="bg-white p-5 rounded shadow">
            <h2 class="font-bold text-xl">${doc.name}</h2>
            <p>${doc.specialization}</p>
            <p>${doc.city}</p>

            <button onclick="deleteDoctor(${doc.id})"
            class="bg-red-500 text-white px-3 py-1 mt-2">
                Delete
            </button>
        </div>
        `;
    });

    document.getElementById("doctorList").innerHTML = html;
}

// DELETE
async function deleteDoctor(id) {
    await fetch(`/api/doctors/${id}/`, {
        method: "DELETE"
    });

    loadDoctors();
}

// ADD DOCTOR
async function saveDoctor() {

    let data = {
        name: document.getElementById("name").value,
        specialization: document.getElementById("specialization").value,
        city: document.getElementById("city").value,
        hospital: document.getElementById("hospital").value,
        experience: document.getElementById("experience").value
    };

    await fetch("/api/doctors/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    closeModal();
    loadDoctors();
}

// OPEN MODAL
function openAddModal() {
    document.getElementById("modal").classList.remove("hidden");
}

// CLOSE MODAL
function closeModal() {
    document.getElementById("modal").classList.add("hidden");
}

// INITIAL LOAD
loadDoctors();