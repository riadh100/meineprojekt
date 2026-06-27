/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Table
 * Datei: components/table.js
 * =====================================================
 */

const Table = {

    render(containerId, columns = [], rows = []) {

        const container = document.getElementById(containerId);

        if (!container) return;

        let html = `
            <table class="table">
                <thead>
                    <tr>
        `;

        columns.forEach(column => {

            html += `<th>${column}</th>`;

        });

        html += `
                    </tr>
                </thead>
                <tbody>
        `;

        rows.forEach(row => {

            html += "<tr>";

            row.forEach(cell => {

                html += `<td>${cell}</td>`;

            });

            html += "</tr>";

        });

        html += `
                </tbody>
            </table>
        `;

        container.innerHTML = html;

    },

    clear(containerId) {

        const container = document.getElementById(containerId);

        if (container) {

            container.innerHTML = "";

        }

    },

    appendRow(containerId, row = []) {

        const table = document.querySelector(
            `#${containerId} tbody`
        );

        if (!table) return;

        const tr = document.createElement("tr");

        row.forEach(cell => {

            const td = document.createElement("td");

            td.innerHTML = cell;

            tr.appendChild(td);

        });

        table.appendChild(tr);

    }

};

window.Table = Table;
