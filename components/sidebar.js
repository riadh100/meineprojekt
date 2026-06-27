/**
 * =====================================================
 * AI Empire Pro V8
 * Component - Sidebar
 * Datei: components/sidebar.js
 * =====================================================
 */

const Sidebar = {

    items: [

        { id: "dashboard", icon: "📊", title: "Dashboard" },
        { id: "assistant", icon: "🤖", title: "AI Assistant" },
        { id: "trading", icon: "💰", title: "Trading" },
        { id: "telegram", icon: "📨", title: "Telegram" },
        { id: "video", icon: "🎬", title: "Video Studio" },
        { id: "game", icon: "🎮", title: "Games" },
        { id: "tools", icon: "🛠️", title: "Tools" },
        { id: "setup", icon: "⚙️", title: "Einstellungen" }

    ],

    render(containerId = "sidebar") {

        const container = document.getElementById(containerId);

        if (!container) return;

        let html = `

            <div class="sidebar-logo">

                <h2>👑 AI Empire</h2>

            </div>

            <ul class="sidebar-menu">

        `;

        this.items.forEach(item => {

            html += `

                <li>

                    <button
                        class="sidebar-item"
                        onclick="Router.navigate('${item.id}')">

                        <span>${item.icon}</span>

                        <span>${item.title}</span>

                    </button>

                </li>

            `;

        });

        html += `

            </ul>

        `;

        container.innerHTML = html;

    }

};

window.Sidebar = Sidebar;
