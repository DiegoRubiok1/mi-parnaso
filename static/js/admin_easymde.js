document.addEventListener("DOMContentLoaded", function() {
    const mdField = document.getElementById("id_content_md");
    if (mdField) {
        const easyMDE = new EasyMDE({
            element: mdField,
            spellChecker: false,
            autosave: {
                enabled: true,
                uniqueId: "admin_post_content"
            },
            hideIcons: ["guide", "heading"],
            showIcons: ["strikethrough", "code", "table", "redo", "heading", "undo", "heading-bigger", "heading-smaller"]
        });
    }
});
