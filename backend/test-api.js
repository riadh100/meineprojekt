/**
 * =====================================================
 * AI Empire Pro V8
 * Backend API Test
 * Datei: backend/test-api.js
 * =====================================================
 */

const BASE_URL = "http://localhost:3000";

async function request(endpoint) {

    try {

        const response = await fetch(BASE_URL + endpoint);

        const data = await response.json();

        console.log("");
        console.log("GET " + endpoint);
        console.log("--------------------------------");

        console.log(JSON.stringify(data, null, 2));

    } catch (error) {

        console.error("");

        console.error("Fehler bei", endpoint);

        console.error(error.message);

    }

}

async function run() {

    console.log("");
    console.log("==========================================");
    console.log(" AI Empire Pro V8 API Test");
    console.log("==========================================");

    await request("/");

    await request("/api/status");

    await request("/api/health");

    await request("/api/dashboard");

    await request("/api/trading");

    await request("/api/assistant");

    await request("/api/telegram");

    await request("/api/video");

    await request("/api/game");

    console.log("");

    console.log("==========================================");
    console.log("API Test abgeschlossen");
    console.log("==========================================");

}

run();
