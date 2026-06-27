/**
 * =====================================================
 * AI Empire Pro V8
 * Backend - Dashboard Controller
 * Datei: backend/controllers/dashboardController.js
 * =====================================================
 */

exports.getDashboard = (req, res) => {

    res.json({

        success: true,

        data: {

            balance: 0,

            profit: 0,

            trades: 0,

            users: 1,

            signals: 0,

            notifications: 0,

            updated: new Date().toISOString()

        }

    });

};

exports.getKPIs = (req, res) => {

    res.json({

        success: true,

        data: {

            balance: 0,

            profit: 0,

            winRate: 0,

            trades: 0,

            users: 1

        }

    });

};

exports.getActivity = (req, res) => {

    res.json({

        success: true,

        data: []

    });

};

exports.getMissions = (req, res) => {

    res.json({

        success: true,

        data: []

    });

};
