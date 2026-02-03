// front_office/static/front_office/js/age-calculator.js
document.addEventListener('DOMContentLoaded', function() {
    console.log("Age calculator loaded successfully!");
    
    const dobField = document.getElementById('id_date_of_birth');
    const ageYears = document.getElementById('age-years');
    const ageMonths = document.getElementById('age-months');
    const ageDays = document.getElementById('age-days');

    console.log("DOB Field:", dobField);
    console.log("Age Elements:", ageYears, ageMonths, ageDays);

    // Check if all elements exist
    if (!dobField || !ageYears || !ageMonths || !ageDays) {
        console.error("Missing required elements for age calculator!");
        return;
    }

    // Calculate age when date changes
    dobField.addEventListener('change', calculateAge);
    
    // Also calculate if DOB is already filled (for edit mode)
    if (dobField.value) {
        calculateAge();
    }

    function calculateAge() {
        console.log("Calculating age...", dobField.value);
        
        const dobString = dobField.value;
        
        if (!dobString) {
            console.log("No date selected");
            clearAgeFields();
            return;
        }

        try {
            const dob = new Date(dobString);
            const today = new Date();
            
            // Validate date is not in future
            if (dob > today) {
                alert("Date of birth cannot be in the future!");
                clearAgeFields();
                return;
            }

            let years = today.getFullYear() - dob.getFullYear();
            let months = today.getMonth() - dob.getMonth();
            let days = today.getDate() - dob.getDate();

            console.log("Raw calculation:", years, months, days);

            // Adjust for negative days
            if (days < 0) {
                months--;
                // Get days in the previous month
                const lastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
                days += lastMonth.getDate();
                console.log("Adjusted days:", days);
            }

            // Adjust for negative months
            if (months < 0) {
                years--;
                months += 12;
                console.log("Adjusted months:", months);
            }

            // Update the age fields
            ageYears.value = years > 0 ? years + ' Year' + (years !== 1 ? 's' : '') : '';
            ageMonths.value = months > 0 ? months + ' Month' + (months !== 1 ? 's' : '') : '';
            ageDays.value = days > 0 ? days + ' Day' + (days !== 1 ? 's' : '') : '';

            console.log("Final age:", ageYears.value, ageMonths.value, ageDays.value);
            
            // Visual feedback
            highlightAgeFields();

        } catch (error) {
            console.error("Error calculating age:", error);
            clearAgeFields();
        }
    }

    function clearAgeFields() {
        ageYears.value = '';
        ageMonths.value = '';
        ageDays.value = '';
        console.log("Age fields cleared");
    }

    function highlightAgeFields() {
        const fields = [ageYears, ageMonths, ageDays];
        fields.forEach(field => {
            field.style.backgroundColor = '#e8f5e8';
            setTimeout(() => {
                field.style.backgroundColor = '#f8f9fa';
            }, 500);
        });
        console.log("Age fields highlighted");
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const departmentSelect = document.getElementById("id_department");
    const doctorSelect = document.getElementById("id_doctor_name");
  
    if (departmentSelect) {
      departmentSelect.addEventListener("change", function () {
        const url = departmentSelect.getAttribute("data-url");
        const departmentId = departmentSelect.value;
  
        fetch(`${url}?department_id=${departmentId}`)
          .then(response => response.json())
          .then(data => {
            doctorSelect.innerHTML = ""; // clear old options
            doctorSelect.insertAdjacentHTML("beforeend", `<option value="">--Select--</option>`);
            data.forEach(doctor => {
              doctorSelect.insertAdjacentHTML(
                "beforeend",
                `<option value="${doctor.id}">${doctor.name}</option>`
              );
            });
          });
      });
    }
  });
  