<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clima Agora</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <header class="header">
        <h1 class="site-title">Clima Agora</h1>
        <p class="location">Registro, SP</p>
    </header>

    <main class="content">
        <section class="weather-today">
            <div class="temperature">25°C</div>
            <div class="conditions">Ensolarado</div>
        </section>

        <section class="weather-details">
            <div class="detail-item">
                <span>Umidade</span>
                <span id="humidity-detail"></span>
            </div>
            <div class="detail-item">
                <span>Vento</span>
                <span id="wind-detail">15 km/h</span>
            </div>
            <div class="detail-item">
                <span>Pressão</span>
                <span id="pressure-detail">1015 hPa</span>
            </div>
        </section>

        <section class="forecast">
            <div class="forecast-item">
                <span id="day-detail">day-detail</span>
                <span id="temperature-max-detail">temperature-max-detail</span>
            </div>
            <div class="forecast-item">
                <span id="day-detail">day-detail</span>
                <span id="temperature-min-detail">temperature-min-detail</span>
            </div>

            <button onclick="getForecast()">submit</button>

        </section>
    </main>

    <script src="js/script.js"></script>
</body>

</html>