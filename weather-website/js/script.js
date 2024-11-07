let latitude = -24.503541;
let longitude = -47.848328;
let currentDate = new Date();
let currentHour = currentDate.getHours();
let currentMinutes = currentDate.getMinutes();

const apiBaseUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto`;




async function getForecast() {
    const response = await fetch(apiBaseUrl);
    const obj = await response.json();

    const day = obj.daily.time[0];
    const temperatureMax = obj.daily.temperature_2m_max[0];
    const temperatureMin = obj.daily.temperature_2m_min[0];


    document.getElementById("day-detail").innerHTML = day;
    document.getElementById("temperature-max-detail").innerHTML = temperatureMax;
    document.getElementById("temperature-min-detail").innerHTML = temperatureMin;

}

