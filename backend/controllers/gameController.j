/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Game Controller
 * Datei: backend/controllers/gameController.js
 * =====================================================
 */

exports.getGame = (req, res) => {

    res.json({

        success: true,

        data: {

            level: 1,

            xp: 0,

            achievements: [],

            dailyMissions: [],

            rewards: []

        }

    });

};

exports.getAchievements = (req, res) => {

    res.json({

        success: true,

        data: []

    });

};

exports.unlockAchievement = (req, res) => {

    res.json({

        success: true,

        message: `Achievement ${req.params.id} freigeschaltet.`

    });

};

exports.getDailyMissions = (req, res) => {

    res.json({

        success: true,

        data: []

    });

};

exports.completeMission = (req, res) => {

    res.json({

        success: true,

        message: `Mission ${req.params.id} abgeschlossen.`

    });

};

exports.getRewards = (req, res) => {

    res.json({

        success: true,

        data: []

    });

};

exports.claimReward = (req, res) => {

    res.json({

        success: true,

        message: `Belohnung ${req.params.id} eingelöst.`

    });

};

exports.addXP = (req, res) => {

    const xp = Number(req.body.xp || 0);

    res.json({

        success: true,

        message: `${xp} XP hinzugefügt.`

    });

};
