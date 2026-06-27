/**
 * =====================================================
 * AI Empire Pro V8
 * Video Page
 * Datei: pages/video.js
 * =====================================================
 */

const VideoPage = {

    render(containerId = "app") {

        const app = document.getElementById(containerId);

        if (!app) return;

        app.innerHTML = `

            <div class="page video-page">

                <div class="page-header">

                    <h1>Video Studio</h1>

                </div>

                <div class="dashboard-cards">

                    ${Card.create({
                        id: "video-projects",
                        title: "Projekte",
                        value: ProjectManager.getAll().length,
                        subtitle: "Gesamt",
                        icon: "🎬"
                    })}

                    ${Card.create({
                        id: "video-render",
                        title: "Render Queue",
                        value: RenderQueue.getAll().length,
                        subtitle: "Aufträge",
                        icon: "⚙️"
                    })}

                    ${Card.create({
                        id: "video-exports",
                        title: "Exports",
                        value: ExportManager.getAll().length,
                        subtitle: "Dateien",
                        icon: "📦"
                    })}

                </div>

                <h2>Projekte</h2>

                <div id="projects-table"></div>

                <h2>Render Queue</h2>

                <div id="render-table"></div>

                <h2>Exports</h2>

                <div id="exports-table"></div>

            </div>

        `;

        this.renderProjects();

        this.renderQueue();

        this.renderExports();

    },

    renderProjects() {

        const rows = ProjectManager.getAll().map(project => [

            project.name,

            project.status,

            project.created,

            project.updated

        ]);

        Table.render(
            "projects-table",
            ["Name", "Status", "Erstellt", "Aktualisiert"],
            rows
        );

    },

    renderQueue() {

        const rows = RenderQueue.getAll().map(job => [

            job.projectId,

            job.quality,

            job.format,

            job.status,

            job.progress + "%"

        ]);

        Table.render(
            "render-table",
            ["Projekt", "Qualität", "Format", "Status", "Fortschritt"],
            rows
        );

    },

    renderExports() {

        const rows = ExportManager.getAll().map(job => [

            job.projectId,

            job.format,

            job.quality,

            job.status,

            job.fileName || "-"

        ]);

        Table.render(
            "exports-table",
            ["Projekt", "Format", "Qualität", "Status", "Datei"],
            rows
        );

    }

};

window.VideoPage = VideoPage;
