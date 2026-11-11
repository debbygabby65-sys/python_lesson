document.addEventListener("DOMContentLoaded", function () {

    const navLinks = document.querySelectorAll(".navbar nav a");

    const sections = document.querySelectorAll(
        "#about, #toolkit, #projects, #philosophy, #services, #contact"
    );

    const observer = new IntersectionObserver(function (entries) {

        entries.forEach(function (entry) {

            if (entry.isIntersecting) {

                navLinks.forEach(function (link) {
                    link.classList.remove("active");
                    link.removeAttribute("aria-current");
                });

                const activeLink = document.querySelector(
                    `.navbar nav a[href="#${entry.target.id}"]`
                );

                if (activeLink) {
                    activeLink.classList.add("active");
                    activeLink.setAttribute("aria-current", "location");
                }

            }

        });

    }, {
        threshold: 0,
        rootMargin: "-20% 0px -70% 0px"
    });

    sections.forEach(function (section) {
        observer.observe(section);
    });

});