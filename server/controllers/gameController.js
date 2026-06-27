/**
 * =====================================================
 * AI Empire Pro V8
 * Game Controller
 * Datei: server/controllers/gameController.js
 * =====================================================
 */

const Player = require("../models/Player");
const Achievement = require("../models/Achievement");
const Mission = require("../models/Mission");
const Reward = require("../models/Reward");

class GameController {

    async dashboard(req, res) {

        try {

            const player = await Player.findOne();

            const achievements = await Achievement.find({

                unlocked: true

            }).sort({

                unlockedAt: -1

            });

            const missions = await Mission.find({

                completed: false

            });

            const rewards = await Reward.find();

            return res.json({

                success: true,

                player,

                achievements,

                missions,

                rewards

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Game Dashboard konnte nicht geladen werden."

            });

        }

    }

    async addXP(req, res) {

        try {

            const {

                amount

            } = req.body;

            const player = await Player.findOne();

            if (!player) {

                return res.status(404).json({

                    success: false,

                    message: "Spieler nicht gefunden."

                });

            }

            player.xp += Number(amount);

            while (

                player.xp >= player.nextLevelXP

            ) {

                player.xp -= player.nextLevelXP;

                player.level++;

                player.nextLevelXP = Math.round(

                    player.nextLevelXP * 1.25

                );

            }

            await player.save();

            return res.json({

                success: true,

                player

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "XP konnten nicht aktualisiert werden."

            });

        }

    }

    async completeMission(req, res) {

        try {

            const mission = await Mission.findById(

                req.params.id

            );

            if (!mission) {

                return res.status(404).json({

                    success: false,

                    message: "Mission nicht gefunden."

                });

            }

            mission.completed = true;

            mission.completedAt = new Date();

            await mission.save();

            return res.json({

                success: true,

                mission

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Mission konnte nicht abgeschlossen werden."

            });

        }

    }

    async unlockAchievement(req, res) {

        try {

            const achievement = await Achievement.findById(

                req.params.id

            );

            if (!achievement) {

                return res.status(404).json({

                    success: false,

                    message: "Achievement nicht gefunden."

                });

            }

            achievement.unlocked = true;

            achievement.unlockedAt = new Date();

            await achievement.save();

            return res.json({

                success: true,

                achievement

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Achievement konnte nicht freigeschaltet werden."

            });

        }

    }

    async claimReward(req, res) {

        try {

            const reward = await Reward.findById(

                req.params.id

            );

            if (!reward) {

                return res.status(404).json({

                    success: false,

                    message: "Belohnung nicht gefunden."

                });

            }

            reward.claimed = true;

            reward.claimedAt = new Date();

            await reward.save();

            return res.json({

                success: true,

                reward

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Belohnung konnte nicht eingelöst werden."

            });

        }

    }

}

module.exports = new GameController();
