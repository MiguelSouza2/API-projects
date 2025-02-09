let latitude = -24.503541;
let longitude = -47.848328;
let currentDate = new Date();
let currentHour = currentDate.getHours();
let currentMinutes = currentDate.getMinutes();

const apiBaseUrl = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&daily=temperature_2m_max,temperature_2m_min&hourly=wind_speed_10m&timezone=auto`;

async function getForecast() {
  const response = await fetch(apiBaseUrl);
  const obj = await response.json();

  let forecast = {
    day: obj.hourly.time[currentHour],
    temperatureMax: parseFloat(obj.daily.temperature_2m_max[0]),
    temperatureMin: parseFloat(obj.daily.temperature_2m_min[0]),
    windSpeed: obj.hourly.wind_speed_10m[currentHour],
    temperatureMedium: (
      (parseFloat(obj.daily.temperature_2m_max[0]) +
        parseFloat(obj.daily.temperature_2m_min[0])) /
      2
    ).toFixed(1),
  };

  document.getElementById("day-detail").innerHTML = forecast.day;
  document.getElementById("temperature-max-detail").innerHTML =
    forecast.temperatureMax;
  document.getElementById("temperature-min-detail").innerHTML =
    forecast.temperatureMin;
    document.getElementsByClassName("temperature")[0].innerHTML = forecast.temperatureMedium + "°C";
}
