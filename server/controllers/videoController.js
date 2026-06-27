/**
 * =====================================================
 * AI Empire Pro V8
 * Video Controller
 * Datei: server/controllers/videoController.js
 * =====================================================
 */

const VideoProject = require("../models/VideoProject");
const RenderJob = require("../models/RenderJob");

class VideoController {

    async dashboard(req, res) {

        try {

            const projects = await VideoProject.find()
                .sort({ updatedAt: -1 })
                .limit(20);

            const renders = await RenderJob.find()
                .sort({ createdAt: -1 })
                .limit(20);

            return res.json({

                success: true,

                projects,

                renders

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Video Dashboard konnte nicht geladen werden."

            });

        }

    }

    async createProject(req, res) {

        try {

            const project = await VideoProject.create(req.body);

            return res.status(201).json({

                success: true,

                project

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Projekt konnte nicht erstellt werden."

            });

        }

    }

    async updateProject(req, res) {

        try {

            const project = await VideoProject.findByIdAndUpdate(

                req.params.id,

                req.body,

                {

                    new: true

                }

            );

            if (!project) {

                return res.status(404).json({

                    success: false,

                    message: "Projekt nicht gefunden."

                });

            }

            return res.json({

                success: true,

                project

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Projekt konnte nicht aktualisiert werden."

            });

        }

    }

    async deleteProject(req, res) {

        try {

            const project = await VideoProject.findByIdAndDelete(

                req.params.id

            );

            if (!project) {

                return res.status(404).json({

                    success: false,

                    message: "Projekt nicht gefunden."

                });

            }

            return res.json({

                success: true,

                message: "Projekt gelöscht."

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Projekt konnte nicht gelöscht werden."

            });

        }

    }

    async createRender(req, res) {

        try {

            const render = await RenderJob.create({

                ...req.body,

                status: "queued",

                progress: 0

            });

            return res.status(201).json({

                success: true,

                render

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Renderjob konnte nicht erstellt werden."

            });

        }

    }

    async updateRender(req, res) {

        try {

            const render = await RenderJob.findByIdAndUpdate(

                req.params.id,

                req.body,

                {

                    new: true

                }

            );

            if (!render) {

                return res.status(404).json({

                    success: false,

                    message: "Renderjob nicht gefunden."

                });

            }

            return res.json({

                success: true,

                render

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Renderjob konnte nicht aktualisiert werden."

            });

        }

    }

    async history(req, res) {

        try {

            const renders = await RenderJob.find()

                .sort({

                    createdAt: -1

                });

            return res.json({

                success: true,

                renders

            });

        }

        catch (error) {

            console.error(error);

            return res.status(500).json({

                success: false,

                message: "Render-Historie konnte nicht geladen werden."

            });

        }

    }

}

module.exports = new VideoController();
