/**
 * =====================================================
 * AI Empire Pro V8
 * Database Seeder
 * Datei: server/seeds/seed.js
 * =====================================================
 */

require("dotenv").config();

const bcrypt = require("bcryptjs");

const databaseService = require("../services/databaseService");

const User = require("../models/User");
const Portfolio = require("../models/Portfolio");
const AppSettings = require("../models/AppSettings");
const Player = require("../models/Player");
const Achievement = require("../models/Achievement");
const Mission = require("../models/Mission");
const Reward = require("../models/Reward");

async function seed() {

    try {

        console.log("");

        console.log("====================================");

        console.log(" AI Empire Pro V8 Seeder");

        console.log("====================================");

        await databaseService.connect();

        await Promise.all([

            User.deleteMany({}),

            Portfolio.deleteMany({}),

            AppSettings.deleteMany({}),

            Player.deleteMany({}),

            Achievement.deleteMany({}),

            Mission.deleteMany({}),

            Reward.deleteMany({})

        ]);

        const password = await bcrypt.hash(

            "admin123",

            10

        );

        const admin = await User.create({

            username: "admin",

            email: "admin@aiempire.local",

            password,

            role: "admin"

        });

        await Portfolio.create({

            name: "Hauptportfolio",

            balance: 10000,

            invested: 7500,

            profit: 2500,

            currency: "EUR"

        });

        await AppSettings.create({

            appName: "AI Empire Pro",

            version: "8.0.0",

            language: "de"

        });

        await Player.create({

            username: "admin",

            level: 1,

            xp: 0,

            coins: 500

        });

        await Achievement.insertMany([

            {

                title: "Willkommen",

                description: "Erstes Login",

                points: 25

            },

            {

                title: "Trader",

                description: "Ersten Trade erstellen",

                points: 50

            }

        ]);

        await Mission.insertMany([

            {

                title: "Dashboard öffnen",

                rewardXP: 50,

                rewardCoins: 25

            },

            {

                title: "Ersten Chat starten",

                rewardXP: 100,

                rewardCoins: 50

            }

        ]);

        await Reward.insertMany([

            {

                title: "500 Coins",

                type: "coins",

                value: 500

            },

            {

                title: "250 XP",

                type: "xp",

                value: 250

            }

        ]);

        console.log("");

        console.log("Seed erfolgreich abgeschlossen.");

        console.log("");

        console.log("Login:");

        console.log("Benutzer: admin");

        console.log("Passwort : admin123");

        console.log("");

        process.exit(0);

    }

    catch (error) {

        console.error(error);

        process.exit(1);

    }

}

seed();
