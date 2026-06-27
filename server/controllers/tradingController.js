/**
 * =====================================================
 * AI Empire Pro V8
 * Trading Controller
 * Datei: server/controllers/tradingController.js
 * =====================================================
 */

const Trade = require("../models/Trade");
const Portfolio = require("../models/Portfolio");

class TradingController {

    async dashboard(req, res) {

        try {

            const portfolio = await Portfolio.findOne();

            const trades = await Trade.find()
                .sort({ createdAt: -1 })
                .limit(20);

            const stats = await this.calculateStats();

            return res.json({

                success: true,

                portfolio,

                trades,

                stats

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Trading-Daten konnten nicht geladen werden."

            });

        }

    }

    async history(req, res) {

        try {

            const trades = await Trade.find()
                .sort({ createdAt: -1 });

            return res.json({

                success: true,

                trades

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Trade-Historie konnte nicht geladen werden."

            });

        }

    }

    async createTrade(req, res) {

        try {

            const trade = await Trade.create(req.body);

            return res.status(201).json({

                success: true,

                trade

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Trade konnte nicht erstellt werden."

            });

        }

    }

    async updateTrade(req, res) {

        try {

            const trade = await Trade.findByIdAndUpdate(

                req.params.id,

                req.body,

                {

                    new: true

                }

            );

            if (!trade) {

                return res.status(404).json({

                    success: false,

                    message: "Trade nicht gefunden."

                });

            }

            return res.json({

                success: true,

                trade

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Trade konnte nicht aktualisiert werden."

            });

        }

    }

    async deleteTrade(req, res) {

        try {

            const trade = await Trade.findByIdAndDelete(

                req.params.id

            );

            if (!trade) {

                return res.status(404).json({

                    success: false,

                    message: "Trade nicht gefunden."

                });

            }

            return res.json({

                success: true,

                message: "Trade gelöscht."

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Trade konnte nicht gelöscht werden."

            });

        }

    }

    async calculateStats() {

        const trades = await Trade.find();

        const totalTrades = trades.length;

        const wins = trades.filter(

            trade => trade.profit > 0

        ).length;

        const losses = totalTrades - wins;

        const totalProfit = trades.reduce(

            (sum, trade) =>

                sum + (trade.profit || 0),

            0

        );

        return {

            totalTrades,

            wins,

            losses,

            winRate:

                totalTrades > 0

                    ? ((wins / totalTrades) * 100).toFixed(2)

                    : 0,

            totalProfit

        };

    }

}

module.exports = new TradingController();
